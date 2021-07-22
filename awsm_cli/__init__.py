from .awsm_cli import *
import argparse
import sys

__version__ = "0.0.3"


def main(argv=None):
    argv = sys.argv if argv is None else argv
    argparser = argparse.ArgumentParser(
        description="CLI Menu for awesome list https://github.com/sindresorhus/awesome"
    )
    argparser.add_argument(
        "-b", "--browser", help="Custom Browser",
    )
    args = argparser.parse_args()

    awsm_cli = AwsmCLI(args.browser)
    awsm_cli.get_awesome_list_json()
    awsm_cli.domain_prompt()
    awsm_cli.topic_prompt()
    awsm_cli.get_topic_repo_json()
    awsm_cli.item_prompt()
    awsm_cli.open_item_browser()
