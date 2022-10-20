# Welcome to the Yearly Advent of Code

## Advent of Code (AOC) description

> "Advent of Code is an Advent calendar of small programming puzzles for a variety of skill sets and skill levels that can be solved in any programming language you like. People use them as a speed contest, interview prep, company training, university coursework, practice problems, or to challenge each other. You don't need a computer science background to participate - just a little programming knowledge and some problem solving skills will get you pretty far. Nor do you need a fancy computer; every problem has a solution that completes in at most 15 seconds on ten-year-old hardware. If you'd like to support Advent of Code, you can do so indirectly by helping to [Shareon Mastodon] it with others, or directly via PayPal or Coinbase. Advent of Code is a registered trademark in the United States." ([Advent of Code / About](https://adventofcode.com/2021/about))

## Repository description

This repository was created to allow multiple participants to compare both the actual code and score and compete against each others during the AOC time. For this purpose, some scripts and automations have been provided, which should avoid a time-consuming setup.
It has been ensured that the scripts and automations are written as generically as possible, so that they can also be adopted for subsequent years, provided that the AOC course or the structure of the scoreboard API does not change.
In the following, with the help of small code snippets, it is explained how the repository can be prepared for subsequent years.  
All code is executed in [bash instances](https://gitforwindows.org/)  
<span style="color:red">Within the code snippets, `<` and `>` are used to describe a variable that should be changed by the user. the `<` and `>` characters must be removed.
</span>

## Pre requirements

- Each participant must have a [GitHub account](https://github.com/signup?source=login)
- Each participant must have an [AOC account](https://adventofcode.com/2021/auth/login)
- The host must create an account on the [Pythonanywhere website](https://www.pythonanywhere.com/)
- ([GitHub CLI](https://cli.github.com/) installed on device)
- ([Git Bash](https://gitforwindows.org/) installed on device)

## Clone repository

First, the project must be duplicated or cloned in order to work in it as a team. The following alternatives are possible:

### Create Repository from template via GitHub CLI

```bash
gh repo create Advent-of-Code`date +"%Y"` -p https://github.com/Git-Romer/Advent-of-Code.git --public
```

### Create Repository from template via GitHub Web

Navigate to [this page](https://github.com/Git-Romer/Advent-of-Code/generate), choose an appropriate name and set the repository to public. The option to include all branches is not necessary.

## Initialize repository

The repository includes 2 files which have to be executed for initialization by the host.

### [init_repo.py](init_repo.py)

When executing this file, the user is asked for the names of the persons to participate. Several persons can be entered at the same time.  
Example:

```text
$ python init_repo.py
Please enter the participating persons comma separated: user1, user2, user3
```

### [init_django.py](init_django.py)

When this file is executed, the necessary django requirements are created.  
First, the user is asked for the URL to the AOC scoreboard.  
Afterwards, the user is asked for the session cookie. This is necessary for django to authenticate itself on the API request to the scoreboard.  
If you need help retrieving the session cookie you can jump to the [FAQ section](#How-to-retrieve-the-session-cookie) explaining the process.  
Example:

```text
$ python init_django.py
Please enter the URL to your Advent of Code Leaderboard: https://adventofcode.com/****/leaderboard/private/view/*******
Please enter the session cookie to your Advent of Code Leaderboard: 53616c74658e*****************************************************************************************************49ad7acf102791d
```

## FAQ

### How to retrieve the session cookie?

1. Open the Advent of Code Website in your browser.
2. Head to your [private Leaderboard](https://adventofcode.com/leaderboard/private), Click on `[View]`, `[API]` and then `[JSON]`.
3. Once your webbrowser opens the JSON results, press `F12` to open the developer tools.
4. Head to the `Network` tab and reload the page.
5. Select the GET request with the `adventofcode.com` host and head to the `Headers` tab.
6. Scroll down and retrieve the `Cookie` value without the `session=` part.
