from art import *
import requests
import subprocess
import webbrowser
from prompt_toolkit import prompt
from subprocess import PIPE, run
from prompt_toolkit.completion import (
    WordCompleter,
    Completer,
    FuzzyWordCompleter,
)


class Awsm_cli:
    def __init__(self):
        # https://raw.githubusercontent.com/lockys/Awesome.json/master/awesome/awesome.json
        tprint("AWSM-CLI")
        print("Downloading Domain List...\n")
        awesome_list_source = requests.get(
            "https://raw.githubusercontent.com/lockys/Awesome.json/master/awesome/awesome.json"
        )
        self.awesome_list = awesome_list_source.json()

    def select_domain(self):
        """Returns the selected domain
        return: selected_domain
        """
        domains = []

        for key, value in self.awesome_list.items():
            domains.append(key)

        domains_completer = FuzzyWordCompleter(domains)
        selected_domain = prompt("Domain: ", completer=domains_completer)
        return selected_domain

    def select_domain_topic_repo(self, selected_domain):
        """Returns the selected domain topic repo
        return: domain_topic_repo
        """

        # Get the list for chosen domain
        for key, value in self.awesome_list.items():
            if key == selected_domain:
                selected_domain_topics_list = value

        # Build the domain topics list
        selected_domain_topics = []
        selected_domain_topic_repos = []
        for value in selected_domain_topics_list:
            selected_domain_topic_repos.append(value["repo"])
            selected_domain_topics.append(value["name"])

        domain_topics_completer = FuzzyWordCompleter(selected_domain_topics)
        selected_topic = prompt("Topic: ", completer=domain_topics_completer)
        selected_topic_index = selected_domain_topics.index(selected_topic)

        domain_topic_repo = selected_domain_topic_repos[selected_topic_index].replace(
            "/", "-"
        )
        return domain_topic_repo

    def select_awesome_item(self, selected_domain_topic_repo):
        """ Returns the selected item URL
        return: selected_item_url
        """

        # https://raw.githubusercontent.com/lockys/Awesome.json/master/repo-json/vinta-awesome-python.json
        awesome_repo_url = (
            "https://raw.githubusercontent.com/lockys/Awesome.json/master/repo-json/"
            + selected_domain_topic_repo
            + ".json"
        )
        awesome_repo_source = requests.get(awesome_repo_url)
        awesome_repo_json = awesome_repo_source.json()

        item_names = []
        item_descriptions = []
        item_urls = []
        item_names_descriptions = []
        for item_info in awesome_repo_json:
            item_names.append(item_info["name"])

            try:
                item_descriptions.append(item_info["description"])
                item_names_descriptions.append(
                    item_info["name"] + " -> " + item_info["description"]
                )
            except:
                item_descriptions.append("None")
                item_names_descriptions.append(
                    item_info["name"] + " -> " + "No Description"
                )

            item_urls.append(item_info["url"])

        item_completion_list = FuzzyWordCompleter(item_names_descriptions)
        selected_item = prompt("Item: ", completer=item_completion_list)
        selected_item_index = item_names_descriptions.index(selected_item)
        selected_item_url = item_urls[selected_item_index]
        print("\n" + selected_item + "\n")
        return selected_item_url

    def open_browser(self, url, browser=None):
        """Opens the url in given browser"""
        if not browser:
            webbrowser.open(url)
        else:
            command = browser + " " + url
            process = subprocess.Popen(
                command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
            )
