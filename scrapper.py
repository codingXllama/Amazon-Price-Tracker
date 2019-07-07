import requests
from bs4 import BeautifulSoup

URL = "https://www.ebay.ca/itm/FCE1-Soccer-Goal-Net-Football-Net-Post-Training-1-2m-X-1-5m-4x5FT-Match/153220914400?_trkparms=aid%3D111001%26algo%3DREC.SEED%26ao%3D1%26asc%3D20160908105057%26meid%3D192c7cbce53649ce9fce08fcb9029e75%26pid%3D100675%26rk%3D2%26rkt%3D15%26sd%3D391822403112%26itm%3D153220914400&_trksid=p2481888.c100675.m4236&_trkparms=pageci%3Aeafcfed7-a04f-11e9-8809-74dbd180c978%7Cparentrq%3Ac9e0a62f16b0ad48072a6f51ff9f538b%7Ciid%3A1"

# getting information about my browser
headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/75.0.3770.100 Safari/537.36"
}


def PriceChecker():

    page = requests.get(URL, headers=headers)


    soup = BeautifulSoup(page.content, "html.parser")
    # print(soup)
    # print(soup.prettify())

    title = soup.find(id="itemTitle").get_text()
    itemPrice = soup.find(id="prcIsum").get_text()

    # converting the price into a float
    itemPrice = float(itemPrice[3:])

    # removing spaces from the title
    print(title.strip("Details about").strip())

    if itemPrice < 10:
        SendEmail()


# print("The price of item: ", itemPrice)
# print("The length of price var is:", len(itemPrice))

def SendEmail():
    None