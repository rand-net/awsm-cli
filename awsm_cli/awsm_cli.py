from art import tprint
import requests
import subprocess
import webbrowser
from prompt_toolkit import prompt
from prompt_toolkit.completion import FuzzyWordCompleter


class AwsmCLI:
    """Awesome CLI
    CLI to access awesome lists

    JSON Data URLS
    # https://raw.githubusercontent.com/lockys/Awesome.json/master/awesome/awesome.json
    # https://raw.githubusercontent.com/lockys/Awesome.json/master/repo-json/vinta-awesome-python.json
    """

    def __init__(self, browser=None):
        tprint("AWSM-CLI")
        print("Downloading Domain List...\n")
        awesome_list_source = requests.get(
            "https://raw.githubusercontent.com/lockys/Awesome.json/master/awesome/awesome.json"
        )
        self.browser = browser
        self.awesome_list = awesome_list_source.json()
        self.selected_domain = ""
        self.selected_topic = ""
        self.selected_topic_repo = ""
        self.topic_repo_json_url = (
            "https://raw.githubusercontent.com/lockys/Awesome.json/master/repo-json/"
        )
        self.selcted_item_url = ""

    def domain_prompt(self):
        """
        Prompt for domain selection
        """
        domains = [key for key, value in self.awesome_list.items()]
        domains_completer = FuzzyWordCompleter(domains)
        self.selected_domain = prompt("Domain: ", completer=domains_completer)

    def topic_prompt(self):
        """
        Prompt for topic selection
        """
        # Topics for chosen domain
        for key, value in self.awesome_list.items():
            if key == self.selected_domain:
                selected_topics_listdict = value

        # Domain Prompt
        selected_topics = [value["name"] for value in selected_topics_listdict]
        domain_topics_completer = FuzzyWordCompleter(selected_topics)
        selected_topic = prompt("Topic: ", completer=domain_topics_completer)

        selected_topic_index = selected_topics.index(selected_topic)
        self.selected_topic_repo = selected_topics_listdict[selected_topic_index][
            "repo"
        ].replace("/", "-")

    def item_prompt(self):
        """
        Prompt for item selection
        """

        # Get JSON data about repo
        awesome_repo_url = self.topic_repo_json_url + self.selected_topic_repo + ".json"
        awesome_repo_source = requests.get(awesome_repo_url)
        awesome_repo_json = awesome_repo_source.json()

        item_urls = []
        item_names_descriptions = []
        for item_info in awesome_repo_json:
            item_urls.append(item_info["url"])
            try:
                item_names_descriptions.append(
                    item_info["name"] + " -> " + item_info["description"]
                )
            except KeyError:
                item_names_descriptions.append(
                    item_info["name"] + " -> " + "No Description"
                )

        item_completion_list = FuzzyWordCompleter(item_names_descriptions)
        selected_item = prompt("Item: ", completer=item_completion_list)
        selected_item_index = item_names_descriptions.index(selected_item)
        self.selected_item_url = item_urls[selected_item_index]
        print("\n" + selected_item + "\n")

    def open_item_browser(self):
        """
        Opens the item url in the given browser
        """
        if not self.browser:
            webbrowser.open(self.selected_item_url)
        else:
            command = self.browser + " " + self.selected_item_url
            process = subprocess.Popen(
                command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
            )
