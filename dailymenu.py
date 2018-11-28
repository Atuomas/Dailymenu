from bs4 import BeautifulSoup
import requests
import datetime


def main():
    if datetime.date.today().weekday() == 0:
        writeToFile()
    handleFile()
    
def handleFile(name='menu.txt'):
    day = datetime.date.today().weekday()
    with open(name, 'r') as tFile:
        contents = tFile.read().split('\n\n')
        print(contents[day])
    
def fetchData():
    date = datetime.date.today()
    src = requests.get('https://www.fazerfoodco.fi/api/restaurant/menu/week?language=fi&restaurantPageId=177431&weekDate=' + str(date))
    data = src.json()
    return data

def writeToFile():
    data = fetchData()
    menu = data['LunchMenus']

    with open('menu.txt', 'w') as tFile:
        for i in range (0, len(menu)):
            day = str(menu[i]['DayOfWeek'] + '\n')
            tFile.write(day)
            for j in range (0, len(menu[i]['SetMenus'])):
                for k in range (0, len(menu[i]['SetMenus'][j]['Meals'])):
                    try: 
                        meal = str(menu[i]['SetMenus'][j]['Meals'][k]['Name'] + ' ')
                        diets = str(menu[i]['SetMenus'][j]['Meals'][k]['Diets'])
                        mealsAndDiets = meal + diets + '\n'
                        tFile.write(mealsAndDiets)
                    except Exception:
                        pass
            tFile.write('\n')

if __name__ == "__main__":
    main()