import urllib
from bs4 import BeautifulSoup
import os

URL = "http://www.ontrac.com/trackingres.asp?tracking_number=D10011045155761&x=12&y=16"
PB_API = "POST https://api.pushbullet.com/v2/pushes"

####
# This token is not available in GitHub because it's uniquely tied to my own
# Pushbullet account. Limited API access is freely avaialble by finding
# your account's token over here: https://www.pushbullet.com/#settings/account.
####
PB_TOKEN = open("pushbullet_access_token.txt").read().strip()

COMMAND = ("""curl --header 'Access-Token:%s' \
     --header 'Content-Type: application/json' \
     --data-binary '{"body":"Blue Apron has been marked as delivered", \
    "title":"Blue Apron Status Change","type":"note"}' \
     --request %s""" % (PB_TOKEN, PB_API))

def main():
  page = urllib.urlopen(URL)
  soup = BeautifulSoup(page, "html.parser")
  trs = soup.find_all("tr")
  for tr in trs:
    #   print tr
      try:
          if tr.td.b.text == "Delivery Status:":
              status = tr.find_all("td")[1].text.strip()
              if status != "IN TRANSIT DETAILS":
                  print "Status has changed."
                  os.system(COMMAND)
              else:
                  print "No status change."

      except Exception as e:
          pass

if __name__ == "__main__":
  main()
