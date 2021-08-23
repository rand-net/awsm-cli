# awsm-cli

CLI menu for awesome list https://github.com/sindresorhus/awesome

![PyPI](https://img.shields.io/pypi/v/awsm-cli?style=flat-square)
![GitHub](https://img.shields.io/github/license/rand-net/awsm-cli?style=flat-square)

## Installation

```
pip install awsm-cli

```

## Usage

```
usage: awsm-cli [-h] [-b BROWSER]

CLI Menu for awesome list https://github.com/sindresorhus/awesome

optional arguments:
  -h, --help            show this help message and exit
  -b BROWSER, --browser BROWSER
                        Custom Browser

```

* Open URL in the default browser.

```
$ awsm-cli

    _    __        __ ____   __  __          ____  _      ___
   / \   \ \      / // ___| |  \/  |        / ___|| |    |_ _|
  / _ \   \ \ /\ / / \___ \ | |\/| | _____ | |    | |     | |
 / ___ \   \ V  V /   ___) || |  | ||_____|| |___ | |___  | |
/_/   \_\   \_/\_/   |____/ |_|  |_|        \____||_____||___|


Downloading Domain List...

Domain:_
         Platforms
         Programming Languages
         Front-End Development
         Back-End Development
         Computer Science
         Big Data
         Theory



```

* Open URL in a custom browser.
```
$ awsm-cli -b Firefox
    _    __        __ ____   __  __          ____  _      ___
   / \   \ \      / // ___| |  \/  |        / ___|| |    |_ _|
  / _ \   \ \ /\ / / \___ \ | |\/| | _____ | |    | |     | |
 / ___ \   \ V  V /   ___) || |  | ||_____|| |___ | |___  | |
/_/   \_\   \_/\_/   |____/ |_|  |_|        \____||_____||___|


Downloading Domain List...
Domain: Programming Languages
Topic: Go
Item: cli -> Feature-rich and easy to use command-line package based on golang struct tags.

cli -> Feature-rich and easy to use command-line package based on golang struct tags.

```
