import sys
import time

import notify2
import requests

if sys.argv[0] is not None and sys.argv[1] is not None:

    match_id = str(sys.argv[1])
    time_gap = int(sys.argv[2])
    url = 'https://www.cricbuzz.com/match-api/' + match_id + '/commentary.json'
    notify2.init('Cricket score')
    n = notify2.Notification('ICC WC', 'Score Update')
    n.show()

    while True:

        response = requests.get(url)

        if response is not None:
            response = response.json()
            match_title = ''
            batting_team = ''
            defending_team = ''
            toss_winner = response['toss']['winner']
            if toss_winner == response['team1']['name']:
                match_title = response['team1']['s_name'] + ' vs ' + response['team2']['s_name']
            elif toss_winner == response['team2']['name']:
                match_title = response['team2']['s_name'] + ' vs ' + response['team1']['s_name']

            batting_id = response['score']['batting']['id']
            if batting_id == response['team1']['id']:
                batting_team = response['team1']['s_name']
                defending_team = response['te am2']['s_name']
            elif batting_id == response['team2']['id']:
                batting_team = response['team2']['s_name']
                defending_team = response['team1']['s_name']

            first_line = batting_team + ' - ' + response['score']['batting']['score'] + ' [' + response['score'][
                'crr'] + ' rpo]'
            second_line = defending_team + ' - ' + response['score']['target']

            n.update(match_title, first_line + '\n' + second_line, icon='/home/padmanabhanmanoharan/Pictures/logo.jpg')

            n.show()
            time.sleep(3)
            n.close()
            time.sleep(time_gap)
