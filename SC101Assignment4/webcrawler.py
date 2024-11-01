"""
File: webcrawler.py
Name: 
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10905209
Female Number: 7949058
---------------------------
2000s
Male Number: 12979118
Female Number: 9210073
---------------------------
1990s
Male Number: 14146775
Female Number: 10644698
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, features="html.parser")

        # ----- Write your code below this line ----- #
        tags = soup.find_all('tbody')
        male = 0
        female = 0
        for tag in tags:
            target = tag.text.split()
            for i in range(len(target)):
                if target[i] == 'Source:':
                    break
                elif i % 5 == 2:
                    male_num = target[i].split(",")
                    male += int(male_num[0])*1000+int(male_num[1])
                elif i % 5 == 4:
                    female_num = target[i].split(",")
                    female += int(female_num[0])*1000+int(female_num[1])
        print("Male Number: "+ str(male))
        print("Female Number: " + str(female))


if __name__ == '__main__':
    main()
