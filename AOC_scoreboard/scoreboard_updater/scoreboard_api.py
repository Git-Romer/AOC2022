import os

def main():
    import requests
    import scoreboard_updater.api_secrets as api_secrets
    from scoreboard.models import jsoncrawler

    def get_scoreboard_json():
        return requests.get(api_secrets.SCOREBOARD_URL, cookies=api_secrets.SESSION_COOKIE)

    def update():

        response = get_scoreboard_json()
        if response.status_code == 200 and response.headers['Content-Type'] == 'application/json':
            response = response.json()
            for member in response["members"].keys():
                member_id = response["members"][member]["id"]
                name = response["members"][member]["name"]
                stars = response["members"][member]["stars"]
                global_score = response["members"][member]["global_score"]
                local_score = response["members"][member]["local_score"]
                last_star_ts = response["members"][member]["last_star_ts"]
                completion_day_level = response["members"][member]["completion_day_level"]
                event = response["event"]

                res = jsoncrawler(
                    member_id=member_id,
                    name=name,
                    stars=stars,
                    global_score=global_score,
                    local_score=local_score,
                    last_star_ts=last_star_ts,
                    completion_day_level=completion_day_level,
                    event=event
                )
                res.save()
            print("Updated scoreboard!")
        elif response.headers['Content-Type'] == 'text/html':
            print("Error: Response is not JSON")
        else:
            print(f"/api/alerts response: {response.status_code}: {response.reason} \n{response.content}")

    update()

if __name__ == "__main__":
    import os, sys
    sys.path.append('./')
    os.environ['DJANGO_SETTINGS_MODULE'] = 'AOC_scoreboard.settings'
    import django
    django.setup()
    main()
