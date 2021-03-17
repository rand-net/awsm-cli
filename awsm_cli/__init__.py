from .awsm_cli import *
import argparse
import sys

__version__ = "0.0.1"


def main(argv=None):
    argv = sys.argv if argv is None else argv
    argparser = argparse.ArgumentParser(
        description="CLI Menu for awesome list https://github.com/sindresorhus/awesome"
    )
    argparser.add_argument(
        "-b", "--browser", help="Custom Browser",
    )
    args = argparser.parse_args()

    if args.browser:
        awsm_cli = Awsm_cli()
        selected_domain = awsm_cli.select_domain()
        domain_topic_repo = awsm_cli.select_domain_topic_repo(selected_domain)
        selected_item_url = awsm_cli.select_awesome_item(domain_topic_repo)
        awsm_cli.open_browser(selected_item_url, args.browser)

    else:
        awsm_cli = Awsm_cli()
        selected_domain = awsm_cli.select_domain()
        domain_topic_repo = awsm_cli.select_domain_topic_repo(selected_domain)
        selected_item_url = awsm_cli.select_awesome_item(domain_topic_repo)
        awsm_cli.open_browser(selected_item_url)
