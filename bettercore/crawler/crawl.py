from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
url = "https://www.kicker.de/bundesliga/vereine"
url1 = "https://www.kicker.de/"


class CrawledPlayer():
    def __init__(self, team, name, position, notes):
        self.team = team
        self.name = name
        self.position = position
        self.notes = notes


class PlayerFetcher():
    def fetch(self):
        url = "https://www.kicker.de/bundesliga/vereine"
        players = []

        while url != "":
            r = requests.get(url)
            doc = BeautifulSoup(r.text, "html.parser")
            for tr in doc.select("tr"):
                for td in tr:
                    if "Kader" in td.text:
                        next_url = td.a.attrs["href"]
                        next_url = urljoin(url1, next_url)

                        r1 = requests.get(str(next_url))
                        doc1 = BeautifulSoup(r1.text, "html.parser")

                        for tr1 in doc1.select("tr"):
                            x = tr1.select_one(".kick__table--resptabelle .kick__table--ranking__rank")
                            if x != None and x.text != "Nr.":
                                y = tr1.select_one(".kick__table--resptabelle .kick__respt-m-w-190")
                                next_url1 = y.a.attrs["href"]
                                next_url1 = urljoin(url1, next_url1)
                                r2 = requests.get(str(next_url1))
                                doc2 = BeautifulSoup(r2.text, "html.parser")

                                team = doc2.select_one(".kick__vita__header--player .kick__vita__header__team-info .kick__vita__header__team-name").text

                                n1 = doc2.select_one(".kick__vita__header--player .kick__vita__header__person-name-medium h2")
                                n2 = n1.span.extract().text
                                n1 = n1.text.strip()
                                name = (n2 + " " + n1)

                                p = doc2.select_one(".kick__vita__header--player .kick__vita__header__person-detail-kvpair .kick__vita__header__person-detail-kvpair-info")
                                p.span.extract()
                                position = p.text

                                for i in doc2.select(".kick__vita__statistic table .kick__js-open-saison-detail"):
                                    n = i.find_all("td")
                                    list = []
                                    for a in n[2]:
                                        list.append(a.text.strip())
                                    notes = list
                                crawled = CrawledPlayer(team, name, position, notes)
                                players.append(crawled)
            url = ""
        return players.