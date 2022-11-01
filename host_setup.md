# Setup guide for the Host of the Advent of Code

Some scripts and automations have been provided, which should avoid a time-consuming setup.
It has been ensured that the scripts and automations are written as generically as possible, so that they can also be adopted for subsequent years, provided that the AOC course and the structure of the scoreboard API does not change.
In the following, with the help of small code snippets, it is explained how the repository can be prepared for subsequent years.  
All code has been tested and executed in [bash shells](https://gitforwindows.org/). Nevertheless any other shell can be used as long as the necessary tools are installed (see [Pre requirements](#pre-requirements)).

<span style="color:red">Within the code snippets, `<` and `>` are used to describe a variable that should be changed by the user. the `<` and `>` characters must be removed.
</span>

---

## Pre requirements

- Creation of a [GitHub account](https://github.com/signup?source=login)
- Creation of an [AOC account](https://adventofcode.com/2021/auth/login)
- Invitation of all participants to the GitHub repository and sharing the [AOC Leaderboard code](#how-to-retrieve-the-leaderboard-invitation-code).
- Creation of an [PythonAnywhere account](https://www.pythonanywhere.com/registration/register/beginner/)
- Installation of Python 3.9.\* to run the initialization scripts. ([Python 3.9.15](https://www.python.org/downloads/release/python-3915/))
- (Installation of [GitHub CLI](https://cli.github.com/) on device)
- (Installation of [Git Bash](https://gitforwindows.org/) on windows device)

---

## Clone repository

First, the project must be duplicated or cloned in order to work in it as a team. The following alternatives are possible among others:

### Create Repository from template via GitHub CLI

```bash
gh repo create Advent-of-Code`date +"%Y"` -p https://github.com/Git-Romer/Advent-of-Code.git --public
```

### Create Repository from template via GitHub Web

Navigate to [this page](https://github.com/Git-Romer/Advent-of-Code/generate) (<span style="color:orange">link only works if logged in to GitHub</span>), choose an appropriate name and set the repository to public. The option to include all branches is not necessary.

---

## Initialize repository

The repository includes 2 files which have to be executed for initialization.

### [init_repo.py](init_repo.py)

This will create a folder for each person and a folder containing one dummy python file for each day.

When executing this file, you will be asked for the names of the persons to participate. Several persons can be entered at the same time.  
Example:

```text
$ python init_repo.py
Please enter the participating persons comma separated: <USER1>, <USER2>, <USER3>
```

### [init_django.py](init_django.py)

When this file is executed, the necessary django requirements are created.

First, the user is asked for the [URL to the AOC scoreboard](#how-to-retrieve-the-leaderboard-url).  
Afterwards, the user is asked for the session cookie. This is necessary for django to authenticate itself on the API request to the scoreboard.  
If you need help retrieving the session cookie you can jump to the [FAQ section](#how-to-retrieve-the-session-cookie) explaining the process.  
Example:

```text
$ python init_django.py
Please enter the URL to your Advent of Code Leaderboard: https://adventofcode.com/<YEAR>/leaderboard/private/view/<HOST_ID>
Please enter the session cookie to your Advent of Code Leaderboard: <SESSION_COOKIE>
```

## Publish website on Pythonanywhere

Once your GitHub repository is ready, you can publish your website on Pythonanywhere. This step can only be done by the host of the repository.

---

## FAQ

### How to retrieve the session cookie?

1. Open the [Advent of Code Website](https://adventofcode.com/) in your browser and make sure you are logged in.
2. Press `F12` to open the developer tools.
3. Head to the `Network` tab and reload the page.
4. Select the GET request with the `adventofcode.com` host and head to the `Cookies` tab.
5. Copy the request cookie.

### How to retrieve the leaderboard invitation code?

Head to the [AOC Leaderboard](https://adventofcode.com/leaderboard/private) and copy the code consisting of your host id and the unique leaderboard key separated by a hyphen.

### How to retrieve the leaderboard URL?

Head to the [AOC Leaderboard](https://adventofcode.com/leaderboard/private), click on `[View]` and copy the URL from the address bar.

### How to invite participants to the Leaderboard?

The participants can join the leaderboard by entering the [Leaderboard code](#how-to-retrieve-the-leaderboard-invitation-code) in the [AOC Leaderboard](https://adventofcode.com/leaderboard/private) page.

### Do I have to re-initialize the repository/django-webserver if I chose to reset the Leaderboard code?

No you do not have to change or reset anything. As long as the host id stays the same, the django-webserver will still be able to retrieve the data from the API.
