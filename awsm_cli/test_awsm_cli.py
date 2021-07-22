from awsm_cli import *
import unittest


class TestAwsmCLI(unittest.TestCase):
    def test_get_awsome_list_json(self):
        print("test_get_awsome_list_json")
        awsm_cli = AwsmCLI()
        awsm_cli.get_awesome_list_json()
        self.assertIsNotNone(awsm_cli.awesome_list)

    def test_get_topic_repo_json(self):
        print("Test_get_topic_repo_json")
        awsm_cli = AwsmCLI()
        awsm_cli.get_awesome_list_json()
        awsm_cli.selected_topic_repo = "vinta-awesome-python"
        self.assertIsNotNone(awsm_cli.awesome_topic_repo_json)


if __name__ == "__main__":
    unittest.main()
