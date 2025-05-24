
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

next_url = "https://uybor.uz/listings?operationType__eq=sale&category__eq=7&isNewBuilding__eq=false&page=1"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

titles = []
rooms = []
areas = []
floors = []
renovations = []
materials = []
prices = []
addresses = []
lifts = []
securities = []
internets = []
playgrounds = []
sewerages = []
bathrooms = []
video_monitors = []
parking_spaces = []
air_conditions = []
furnitures = []

# driver.get(next_url)
counter = 1
for i in range(100):
    driver.get(next_url)
    try:
        next_url = f'https://uybor.uz/en/listings?operationType__eq=sale&category__eq=7&isNewBuilding__eq=false&page={i + 1}'
        print(next_url)
    except:
        print("No next pages")
        break
    float_links = WebDriverWait(driver, 20).until(expected_conditions.presence_of_all_elements_located((By.XPATH, "//a[@class='MuiBox-root mui-style-1vssrzj']")))
    flat_urls = []
    for link in float_links:
        flat_urls.append(link.get_attribute('href'))
    print(flat_urls)
    print(len(flat_urls))

    for furl in flat_urls:
        driver.get(furl)
        try:
            title = driver.find_element(By.XPATH, "//h1[@class='MuiTypography-root MuiTypography-h2 mui-style-1tyknu']").text
        except:
            title = 'No title'
        titles.append(title)
        print(counter)
        print(f"Title: {title}")


        try:
            room = driver.find_element(By.XPATH, "//div[@class='MuiTypography-root MuiTypography-overline mui-style-1xqesu'"
                                                 "and contains(text(), 'Rooms')]"
                                                 "/following-sibling::div").text
        except:
            room = 'No room'
        rooms.append(room)
        print(f"Room: {room}")

        try:
            area = driver.find_element(By.XPATH, "//div[@class='MuiTypography-root MuiTypography-overline mui-style-1xqesu'"
                                                 "and contains(text(), 'Площадь')]"
                                                 "/following-sibling::div").text
        except:
            area = 'No area'
        areas.append(area)
        print(f"Area: {area}")


        try:
            floor = driver.find_element(By.XPATH, "//div[@class='MuiTypography-root MuiTypography-overline mui-style-1xqesu'"
                                                 "and contains(text(), 'Floor')]"
                                                 "/following-sibling::div").text
        except:
            floor = 'No floor'
        floors.append(floor)
        print(f"Floor: {floor}")

        try:
            renovation = driver.find_element(By.XPATH, "//div[@class='MuiTypography-root MuiTypography-overline mui-style-1xqesu'"
                                                 "and contains(text(), 'Ремонт')]"
                                                 "/following-sibling::div").text
        except:
            renovation = 'No renovations'
        renovations.append(renovation)
        print(f"Renovation: {renovation}")

        try:
            material = driver.find_element(By.XPATH, "//div[@class='MuiTypography-root MuiTypography-overline mui-style-1xqesu'"
                                                 "and contains(text(), 'Материал')]"
                                                 "/following-sibling::div").text
        except:
            material = 'No material'
        materials.append(material)
        print(f"Material: {material}")

        try:
            price = driver.find_element(By.XPATH, "//div[@class='MuiTypography-root MuiTypography-h2 mui-style-86wpc3']").text
        except:
            price = 'No price'
        prices.append(price)
        print(f"Price: {price}")


        try:
            address = driver.find_element(By.XPATH, "//div[@class='MuiTypography-root MuiTypography-body2 mui-style-31fjox']").text
        except:
            address = 'No address'
        addresses.append(address)
        print(f"Address: {address}")

        try:
            lift = driver.find_element(By.XPATH, "//div[@class='MuiTypography-root MuiTypography-body3 mui-style-xckitu' and contains(text(), 'Лифт')]").text
            lift = 1
        except:
            try:
                if int(floor.split('/')[1]) > 5:
                    lift = 1
                else:
                    lift = 0
            except:
                lift = 0
        lifts.append(lift)
        print(f"Lifts: {lift}")

        try:
            security = driver.find_element(By.XPATH, "//div[@class='MuiTypography-root MuiTypography-body3 mui-style-xckitu' and contains(text(), 'Охрана')]").text
            security = 1
        except:
            security = 0
        securities.append(security)
        print(f"Security: {security}")

        try:
            internet = driver.find_element(By.XPATH, "//div[@class='MuiTypography-root MuiTypography-body3 mui-style-xckitu' and contains(text(), 'Интернет')]").text
            internet = 1
        except:
            internet = 0
        internets.append(internet)
        print(f"Internet: {internet}")

        try:
            playground = driver.find_element(By.XPATH, "//div[@class='MuiTypography-root MuiTypography-body3 mui-style-xckitu' and contains(text(), 'Детская площадка')]").text
            playground = 1
        except:
            playground = 0
        playgrounds.append(playground)
        print(f"Playground: {playground}")


        try:
            sewerage = driver.find_element(By.XPATH, "//div[@class='MuiTypography-root MuiTypography-body3 mui-style-xckitu' and contains(text(), 'Канализация')]").text
            sewerage = 1
        except:
            sewerage = 0
        sewerages.append(sewerage)
        print(f"Sewerage: {sewerage}")


        try:
            bathroom = driver.find_element(By.XPATH, "//div[@class='MuiTypography-root MuiTypography-body3 mui-style-xckitu' and contains(text(), 'Санузел раздельный')]").text
            bathroom = 1
        except:
            bathroom = 0
        bathrooms.append(bathroom)
        print(f"Bathroom: {bathroom}")

        try:
            video_monitor = driver.find_element(By.XPATH, "//div[@class='MuiTypography-root MuiTypography-body3 mui-style-xckitu' and contains(text(), 'Видеонаблюдение')]").text
            video_monitor = 1
        except:
            video_monitor = 0
        video_monitors.append(video_monitor)
        print(f"Video_monitor: {video_monitor}")

        try:
            parking_space = driver.find_element(By.XPATH, "//div[@class='MuiTypography-root MuiTypography-body3 mui-style-xckitu' and contains(text(), 'Парковочное место')]").text
            parking_space = 1
        except:
            parking_space = 0
        parking_spaces.append(parking_space)
        print(f"Parking_space: {parking_space}")


        try:
            air_condition = driver.find_element(By.XPATH, "//div[@class='MuiTypography-root MuiTypography-body3 mui-style-xckitu' and contains(text(), 'Кондиционер')]").text
            air_condition = 1
        except:
            air_condition = 0
        air_conditions.append(air_condition)
        print(f"Air condition: {air_condition}")

        try:
            furniture = driver.find_element(By.XPATH, "//div[@class='MuiTypography-root MuiTypography-body3 mui-style-xckitu' and contains(text(), 'Мебель')]").text
            furniture = 1
        except:
            furniture = 0
        furnitures.append(furniture)
        print(f"Furniture: {furniture}")
        counter += 1

        print(f"<{'-'*30}>\n")


df = pd.DataFrame(
    {
        'title': titles,
        'room': rooms,
        'area': areas,
        'floor': floors,
        'renovation': renovations,
        'material': materials,
        'price': prices,
        'address': addresses,
        'lift': lifts,
        'security': securities,
        'internet': internets,
        'playground': playgrounds,
        'sewerage': sewerages,
        'bathroom': bathrooms,
        'video_monitor': video_monitors,
        'parking_space': parking_spaces,
        'air_condition': air_conditions,
        'furniture': furnitures
    }
)
df.to_csv('uybor.csv')
