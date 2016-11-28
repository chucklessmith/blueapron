import urllib
from bs4 import BeautifulSoup

URL = "http://www.ontrac.com/trackingres.asp?tracking_number=D10011045155761&x=12&y=16"

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
              else:
                  print "No status change.."

      except Exception as e:
          pass

if __name__ == "__main__":
  main()
