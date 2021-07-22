from .awsm_cli import *
import argparse
import sys

__version__ = "0.0.2"


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
        awsm_cli = AwsmCLI(args.browser)
        selected_domain = awsm_cli.domain_prompt()
        domain_topic_repo = awsm_cli.topic_prompt()
        selected_item_url = awsm_cli.item_prompt()
        awsm_cli.open_item_browser()

    else:
        awsm_cli = AwsmCLI(args.browser)
        selected_domain = awsm_cli.domain_prompt()
        domain_topic_repo = awsm_cli.topic_prompt()
        selected_item_url = awsm_cli.item_prompt()
        awsm_cli.open_item_browser()
