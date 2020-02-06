import requests 
from bs4 import BeautifulSoup
import smtplib
import time

URL ='https://www.amazon.co.uk/Bose-QuietComfort-Wireless-Headphones-Cancelling-Black/dp/B0756CYWWD/ref=sr_1_4?crid=1NBQ271NA5EA8&keywords=bose+headphones&qid=1581013981&sprefix=bose+h%2Caps%2C-1&sr=8-4'

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'}


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id='productTitle').get_text()
    price = soup.find(id='priceblock_ourprice').get_text()
    converted_price = float(price[1:5])

    if(converted_price < 250.0)
        send_mail()

    print(title.strip())
    print(converted_price)

    if(converted_price < 250.0): 
        send_mail()

def send_mail():
    server = smtplib.SMTP('stmp.gmail.com', 587)
    server.ehlo()
    server.starttls
    server.ehlo()

    server.login('email', 'password')

    subject = 'Price has fallen down!'
    body = 'Check the link https://www.amazon.co.uk/Bose-QuietComfort-Wireless-Headphones-Cancelling-Black/dp/B0756CYWWD/ref=sr_1_4?crid=1NBQ271NA5EA8&keywords=bose+headphones&qid=1581013981&sprefix=bose+h%2Caps%2C-1&sr=8-4'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'email', #from email
        'email' #to email
        msg
    )
    print('EMAIL HAS BEEN SENt')

    server.quit


while(True):
    check_price()
    time.sleep(60 * 60 * 24)