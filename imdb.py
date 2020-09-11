import requests
import csv
from bs4 import BeautifulSoup
url="https://www.imdb.com/chart/top/?ref_=nv_mv_250"
r= requests.get(url)
hmtlcontent = r.content
#print(hmtlcontent)
soup = BeautifulSoup(hmtlcontent, 'html.parser')
#print(soup)
#print(soup.prettify)
title= soup.title

f = soup.find("tbody", {"class": "lister-list"}).findAll("tr")
#f1 = soup.find('tbody') 
#print(f)
def main_fun():
    movies_list = []
    for n in f:
        title = n.find("td", {"class":"titleColumn"}).find("a").get_text()

        year = n.find("td", {"class":"titleColumn"}).find("span").get_text()

        rating = n.find("td", {"class":"ratingColumn imdbRating"}).find("strong").get_text()
        rating = float(rating)

        raw_list = [title,year, rating]
        movies_list.append(raw_list)
     
    recomendation(movies_list)
    create_csv(movies_list)

def recomendation(m_list):
    print("Enter you rating for recomendation:")
    user_rating = input()
    user_rating = float(user_rating)
    for x in range(len(m_list)):
        if m_list[x][2]>user_rating:
            print(m_list[x][0])


def create_csv(movies):
    with open('movies.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        row = ['Name', 'year','Rating']
        writer.writerow(title)
        writer.writerow(row)
        for x in range(len(movies)):
            row = movies[x]
            writer.writerow(row)
    csvfile.close()
main_fun()