from bs4 import BeautifulSoup
import requests
import csv


url1= requests.get('http://quotes.toscrape.com/')
def citas():
    global url1
    file = open('Data.csv', 'w')
    writer = csv.writer(file)
    soup = BeautifulSoup(url1.text, "html.parser")
    cita = soup.findAll("span", attrs={"class":"text"})
    autor = soup.findAll("small", attrs={"class":"author"})
    header = ['Quote', 'Author']
    writer.writerow(header)
    for i in range (len(autor)):
        squote = [cita[i].text, autor[i].text]
        writer.writerow(squote)
    file.close()

citas()