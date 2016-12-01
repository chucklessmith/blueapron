import requests
from bs4 import BeautifulSoup

URL = "http://www.ontrac.com/trackingres.asp?tracking_number=D10011045155761&x=12&y=16"
PB_API = "https://api.pushbullet.com/v2/pushes"

####
# This token is not available in GitHub because it's uniquely tied to my own
# Pushbullet account. Limited API access is freely avaialble by finding
# your account's token over here: https://www.pushbullet.com/#settings/account.
####
PB_TOKEN = open("pushbullet_access_token.txt").read().strip() # no EOL characters

def get_status(page):
    soup = BeautifulSoup(page, "html.parser")
    trs = soup.find_all("tr")
    for tr in trs:
        try:
            if tr.td.b.text == "Delivery Status:":
              status = tr.find_all("td")[1].text.strip()
              return status
        except AttributeError as e:
            pass

def send_notification():
    ### This POST pushes notifications to all devices registered to the account.
    ##  That may or may not be the desired effect, so proceed with caution.
    requests.post(PB_API,
                    headers={"Access-Token":PB_TOKEN},
                    json={"body":"Blue Apron has been marked as delivered",
                          "title":"Blue Apron Status Change","type":"note"})

def main():
    page = requests.get(URL).text
    status = get_status(page)
    message = "No status change."
    if status:
      message = "Status has changed."
      send_notification()
    print '\n' + message

if __name__ == "__main__":
  main()
