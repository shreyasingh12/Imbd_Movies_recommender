# Imbd_Movies_recommender
This is a movie recommender system.

#Requirements-: 1-import BeautifulSoup(python library used for web scrapping.)
2-import html5lib
3-import requests
4-import csv(to create an csv file)

#How the recommender works-:
Step 1:The recommender will fetch all the data from the website with the use of the python library BeautifulSoup.
Step 2:Then with the recommendation function -The user will have to enter the rating of the movie and the list of movies will appear matching to the rating that you have entered.

#Purpose of all the functions created:-
1->def main_function - This function will fetch the name of the movies,its rating and the year of release. 
2->def recommendation - This function is recommending the movies to the user based on the rating that they have entered.
3->def create_cs - This function is collecting all the data and store them in the csv file.
