import secrets
import os

RANDOM_STRING_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def get_random_string(length, allowed_chars=RANDOM_STRING_CHARS):
    """
    Return a securely generated random string.

    The bit length of the returned value can be calculated with the formula:
        log_2(len(allowed_chars)^length)

    For example, with default `allowed_chars` (26+26+10), this gives:
      * length: 12, bit length =~ 71 bits
      * length: 22, bit length =~ 131 bits
    """
    return "".join(secrets.choice(allowed_chars) for i in range(length))

def get_random_secret_key():
    """
    Return a 50 character random string usable as a SECRET_KEY setting value.
    """
    chars = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)"
    return get_random_string(50, chars)


if __name__ == "__main__":
    Prod_key = get_random_secret_key()
    Dev_key = get_random_secret_key()
    aoc_scoreboard_url = input("Please enter the URL to your Advent of Code Leaderboard: ") + ".json"
    while not "adventofcode.com" in aoc_scoreboard_url:
        print("The entered URL to your Advent of Code Leaderboard seems not to be correct. Please try again.")
        aoc_scoreboard_url = input("Please enter the URL to your Advent of Code Leaderboard: ") + ".json"
    aoc_scoreboard_cookie = input("Please enter the session cookie to your Advent of Code Leaderboard: ")

    try:
        if os.path.isfile(r'./AOC_scoreboard/AOC_scoreboard/django_secrets.py'):
            warning = input("Django's secret keys have already been generated.\nAre you sure you want to continue and overwrite the file? [(y)es|(n)o]: ")
            if warning.lower() == "y" or warning.lower() == "yes":
                with open('./AOC_scoreboard/AOC_scoreboard/jango_secrets.py', 'w') as f:
                    f.write(f'PROD_KEY = r"{Prod_key}"\nDEV_KEY = r"{Dev_key}"')
                    f.close()
            else:
                print("Aborded initialization.")
        else:
                with open('./AOC_scoreboard/AOC_scoreboard/jango_secrets.py', 'w') as f:
                    f.write(f'PROD_KEY = r"{Prod_key}"\nDEV_KEY = r"{Dev_key}"')
                    f.close()


        with open('./AOC_scoreboard/scoreboard_updater/pi_secrets.py', 'w') as f:
            f.write(f'SESSION_COOKIE = {{"session" : r"{aoc_scoreboard_cookie}"}}\nSCOREBOARD_URL = r"{aoc_scoreboard_url}"')
            f.close()
    except FileNotFoundError:
        print("Script could not be executed properly. Please make sure you are executing the script from the root folder of the django project (/AOC_Scoreboard/)")