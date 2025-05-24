# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support import expected_conditions
# import pandas as pd

# url = "https://uybor.uz/listings?category__eq=7&isNewBuilding__eq=false"
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


# titles = []
# rooms = []
# areas = []
# floors = []
# renovations = []
# materials = []
# prices = []
# adresses = []
# lifts = []
# securities = []
# internets = []
# playground = []
# sewerages = []
# bathrooms = []
# video_monitor = []
# parking_spaces = []
# air_condition = []
# furniture = []
# counter = 1

# driver.get(url)

# for i in range(1):
#     float_links = driver.find_elements(By.XPATH, "//a[@class='MuiBox-root mui-style-1vssrzj']")
#     flat_urls = []
#     for link in float_links:
#         flat_urls.append(link.get_attribute('href'))
#     print(flat_urls)
#     print(len(flat_urls))

#     for furl in flat_urls:
#         driver.get(furl)
#         try:
#             title = driver.find_element(By.XPATH, "//h1[@class='MuiTypography-root MuiTypography-h2 mui-style-1tyknu']").text
#         except:
#             title = "No title"

#         titles.append(title)
#         print(counter)
#         print(f"Title: {title}")
#         counter += 1

#         try:
#             room = driver.find_element(By.XPATH, "//div[@class='MuiTypography-root MuiTypography-overline mui-style-1xqesu'"
#                                                  "and contains(text(), 'Комнат')]"
#                                                  "/following-sibling::div").text
#         except:
#             room = "No room"

#         rooms.append(room)
#         print(f"Room: {room}")

#         try:
#             area = driver.find_element(By.XPATH, "//div[@class='MuiTypography-root MuiTypography-overline mui-style-1xqesu'"
#                                                  "and contains(text(), 'Площадь')]"
#                                                  "/following-sibling::div").text
#         except:
#             area = "No area"
#         areas.append(area)
#         print(f"Area: {area}")

#         try:
#             floor = driver.find_element(By.XPATH, "//div[@class='MuiTypography-root MuiTypography-overline mui-style-1xqesu'"
#                                                  "and contains(text(), 'Этаж')]"
#                                                  "/following-sibling::div").text
#         except:
#             floor = "No floor"
#         floors.append(floor)
#         print(f"Floor: {floor}")


#         try:
#             renovation = driver.find_element(By.XPATH, "//div[@class='MuiTypography-root MuiTypography-overline mui-style-1xqesu'"
#                                                  "and contains(text(), 'Ремонт')]"
#                                                  "/following-sibling::div").text
#         except:
#             renovation = "No renovation"
#         renovations.append(renovation)
#         print(f"renovation: {renovation}")

#         try:
#             material = driver.find_element(By.XPATH, "//div[@class='MuiTypography-root MuiTypography-overline mui-style-1xqesu'"
#                                                  "and contains(text(), 'Материал')]"
#                                                  "/following-sibling::div").text
#         except:
#             material = "No material"
#         materials.append(material)
#         print(f"material: {material}")

#         try:
#             price = driver.find_element(By.XPATH, "//div[@class='MuiTypography-root MuiTypography-h2 mui-style-86wpc3']").text
#         except:
#             price = "No price"
#         prices.append(price)
#         print(f"price: {price}")

#         try:
#             adresse = driver.find_element(By.XPATH, "//div[@class='MuiTypography-root MuiTypography-body2 mui-style-31fjox']").text
#         except:
#             adresse = "No adresse"
#         adresses.append(adresse)
#         print(f"adresse: {adresse}")

#         try:
#             lift = driver.find_element(By.XPATH, "//div[@class='MuiStack-root mui-style-ekcp1r'"
#                                                  "and contains(text(), 'Лифт')]"
#                                                  "/following-sibling::div").text
#         except:
#             lift = floor[-1].split('/') # "5/9" -> ["5","9"]
#             if int(lift[-1]) > 5:
#                 lift = "1"
#             else:
#                 lift = "0"
#         lifts.append(lift)
#         print(f"lift: {lift}")


#         try:
#             security = driver.find_element(By.XPATH, "//div[@class='MuiStack-root mui-style-ekcp1r' and contains(text(), 'Видеонаблюдение')]/following-sibling::div").text
#         except:
#             security = ""

#         securities.append(security)
#         print(f"security: {security}")


# # from selenium import webdriver
# # from selenium.webdriver.chrome.service import Service
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.support.wait import WebDriverWait
# # from webdriver_manager.chrome import ChromeDriverManager
# # from selenium.webdriver.support import expected_conditions
# # import pandas as pd
# #
# # url = "https://uybor.uz/listings?category__eq=7&isNewBuilding__eq=false"
# # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# #
# #
# # titles = []
# # rooms = []
# # areas = []
# # floors = []
# # renovations = []
# # materials = []
# # prices = []
# # adresses = []
# # lifts = []
# # securities = []
# # internets = []
# # playground = []
# # sewerages = []
# # bathrooms = []
# # video_monitor = []
# # parking_spaces = []
# # air_condition = []
# # furniture = []
# #
# #
# # counter = 1
# # max_count = 98
# # while counter <= max_count:
# #     laptop_links = []
# #     driver.get(url)
# #
# #     try:
# #         # Keyingi sahifaga o'tish tugmasini kutish
# #         next_page = WebDriverWait(driver, 10).until(
# #             expected_conditions.presence_of_element_located((By.XPATH,
# #                                             "//a[@class='MuiButtonBase-root MuiPaginationItem-root MuiPaginationItem-sizeLarge MuiPaginationItem-text MuiPaginationItem-rounded MuiPaginationItem-textPrimary MuiPaginationItem-previousNext mui-style-mj6azz']"))
# #         )
# #
# #         # To'liq URL olish (relative URL dan to'liq URL yaratish)
# #         next_page_url = next_page.get_attribute("href")
# #         next_page_full_url = url.join(url, next_page_url)  # Asosiy URL ni qo'shish
# #
# #         # Keyingi sahifaga o'tish
# #         url = next_page_full_url  # yangi URLga o'tish
# #         counter += 1
# #         print(f"Sahifa {counter}: {url}")
# #
# #     except Exception as e:
# #         print("End page yoki xatolik:", e)
# #         break
# #
# #
# # # driver.get(url)
# #     float_links = driver.find_elements(By.XPATH, "//a[@class='MuiBox-root mui-style-1vssrzj']")
# #     flat_urls = []
# #     for link in float_links:
# #         flat_urls.append(link.get_attribute('href'))
# #     print(flat_urls)
# #     print(len(flat_urls))
# #
# #     for furl in flat_urls:
# #         driver.get(furl)
# #         try:
# #             title = driver.find_element(By.XPATH, "//h1[@class='MuiTypography-root MuiTypography-h2 mui-style-1tyknu']").text
# #         except:
# #             title = "No title"
# #
# #         titles.append(title)
# #         print(counter)
# #         print(f"Title: {title}")
# #         counter += 1
# #
# #         try:
# #             room = driver.find_element(By.XPATH, "//div[@class='MuiTypography-root MuiTypography-overline mui-style-1xqesu'"
# #                                                  "and contains(text(), 'Комнат')]"
# #                                                  "/following-sibling::div").text
# #         except:
# #             room = "No room"
# #
# #         rooms.append(room)
# #         print(f"Room: {room}")
# #
# #         try:
# #             area = driver.find_element(By.XPATH, "//div[@class='MuiTypography-root MuiTypography-overline mui-style-1xqesu'"
# #                                                  "and contains(text(), 'Площадь')]"
# #                                                  "/following-sibling::div").text
# #         except:
# #             area = "No area"
# #         areas.append(area)
# #         print(f"Area: {area}")
# #
# #         try:
# #             floor = driver.find_element(By.XPATH, "//div[@class='MuiTypography-root MuiTypography-overline mui-style-1xqesu'"
# #                                                  "and contains(text(), 'Этаж')]"
# #                                                  "/following-sibling::div").text
# #         except:
# #             floor = "No floor"
# #         floors.append(floor)
# #         print(f"Floor: {floor}")
# #
# #
# #         try:
# #             renovation = driver.find_element(By.XPATH, "//div[@class='MuiTypography-root MuiTypography-overline mui-style-1xqesu'"
# #                                                  "and contains(text(), 'Ремонт')]"
# #                                                  "/following-sibling::div").text
# #         except:
# #             renovation = "No renovation"
# #         renovations.append(renovation)
# #         print(f"renovation: {renovation}")
# #
# #         try:
# #             material = driver.find_element(By.XPATH, "//div[@class='MuiTypography-root MuiTypography-overline mui-style-1xqesu'"
# #                                                  "and contains(text(), 'Материал')]"
# #                                                  "/following-sibling::div").text
# #         except:
# #             material = "No material"
# #         materials.append(material)
# #         print(f"material: {material}")
# #
# #         try:
# #             price = driver.find_element(By.XPATH, "//div[@class='MuiTypography-root MuiTypography-h2 mui-style-86wpc3']").text
# #         except:
# #             price = "No price"
# #         prices.append(price)
# #         print(f"price: {price}")
# #
# #         try:
# #             adresse = driver.find_element(By.XPATH, "//div[@class='MuiTypography-root MuiTypography-body2 mui-style-31fjox']").text
# #         except:
# #             adresse = "No adresse"
# #         adresses.append(adresse)
# #         print(f"adresse: {adresse}")
# #
# #
# #         try:
# #             elements = driver.find_elements(By.CSS_SELECTOR,".MuiGrid-root.MuiGrid-container.MuiGrid-spacing-xs-2.mui-style-isbt42")
# #             for element in elements:
# #                 text = element.text.strip()
# #                 if 'Лифт' in text:
# #                     lift = '1'
# #                 else:
# #                     liftlar = floor.split('/')
# #                     if int(liftlar[-1]) > 5:
# #                         lift = '1'
# #                     else:
# #                         lift = '0'
# #                 if 'Охрана' in text:
# #                     security = '1'
# #                 else:
# #                     security = '0'
# #                 if 'Интернет' in text:
# #                     internet = '1'
# #                 else:
# #                     internet = '0'
# #                 if 'Детская площадка' in text:
# #                     playgr = '1'
# #                 else:
# #                     playgr = '0'
# #                 if 'Канализация' in text:
# #                     swg = '1'
# #                 else:
# #                     swg = '0'
# #                 if 'Санузел' in text:
# #                     bath = '1'
# #                 else:
# #                     bath = '0'
# #                 if 'Видеонаблюдение' in text:
# #                     video = '1'
# #                 else:
# #                     video = '0'
# #                 if 'Парковочное место' in text:
# #                     parking = '1'
# #                 else:
# #                     parking = '0'
# #         except Exception as e:
# #             print(f"xato:{e}")
# #
# #         lifts.append(lift)
# #         print(f"lift: {lift}")
# #         securities.append(security)
# #         print(f"security: {security}")
# #         internets.append(internet)
# #         print(f"internet: {internet}")
# #         playground.append(playgr)
# #         print(f"playgr: {playgr}")
# #         sewerages.append(swg)
# #         print(f"swg: {swg}")
# #         bathrooms.append(bath)
# #         print(f"bath: {bath}")
# #         video_monitor.append(video)
# #         print(f"video: {video}")
# #         parking_spaces.append(parking)
# #         print(f"parking: {parking}")
# #
# #


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions
from urllib.parse import urljoin  # URL bog'lash uchun import
import pandas as pd

url = "https://uybor.uz/listings?category__eq=7&isNewBuilding__eq=false"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Ma'lumotlar saqlash uchun ro'yxatlar
titles = []
rooms = []
areas = []
floors = []
renovations = []
materials = []
prices = []
adresses = []
lifts = []
securities = []
internets = []
playground = []
sewerages = []
bathrooms = []
video_monitor = []
parking_spaces = []
air_condition = []
furniture = []

son = 0
counter = 1
max_count = 100
while counter <= max_count:
    laptop_links = []
    driver.get(url)

    try:
        # Keyingi sahifaga o'tish tugmasini kutish
        next_page = WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH,
                                            "//a[@class='MuiButtonBase-root MuiPaginationItem-root MuiPaginationItem-sizeLarge MuiPaginationItem-text MuiPaginationItem-rounded MuiPaginationItem-textPrimary MuiPaginationItem-previousNext mui-style-mj6azz']"))
        )

        # To'liq URL olish (relative URL dan to'liq URL yaratish)
        next_page_url = next_page.get_attribute("href")
        next_page_full_url = urljoin(url, next_page_url)  # Asosiy URL ni qo'shish

        # Keyingi sahifaga o'tish
        url = next_page_full_url  # yangi URLga o'tish
        print(f"Sahifa {counter}: {url}")

    except Exception as e:
        print("End page yoki xatolik:", e)
        break

    # Linklarni olish
    float_links = driver.find_elements(By.XPATH, "//a[@class='MuiBox-root mui-style-1vssrzj']")
    flat_urls = [link.get_attribute('href') for link in float_links]
    print(flat_urls)
    print(len(flat_urls))

    for furl in flat_urls:
        driver.get(furl)
        try:
            title = driver.find_element(By.XPATH, "//h1[@class='MuiTypography-root MuiTypography-h2 mui-style-1tyknu']").text
        except:
            title = "No title"
        titles.append(title)
        print(f"Title: {title}")

        try:
            room = driver.find_element(By.XPATH, "//div[@class='MuiTypography-root MuiTypography-overline mui-style-1xqesu' and contains(text(), 'Комнат')]/following-sibling::div").text
        except:
            room = "No room"
        rooms.append(room)
        print(f"Room: {room}")

        try:
            area = driver.find_element(By.XPATH, "//div[@class='MuiTypography-root MuiTypography-overline mui-style-1xqesu' and contains(text(), 'Площадь')]/following-sibling::div").text
        except:
            area = "No area"
        areas.append(area)
        print(f"Area: {area}")

        try:
            floor = driver.find_element(By.XPATH, "//div[@class='MuiTypography-root MuiTypography-overline mui-style-1xqesu' and contains(text(), 'Этаж')]/following-sibling::div").text
        except:
            floor = "No floor"
        floors.append(floor)
        print(f"Floor: {floor}")

        try:
            renovation = driver.find_element(By.XPATH, "//div[@class='MuiTypography-root MuiTypography-overline mui-style-1xqesu' and contains(text(), 'Ремонт')]/following-sibling::div").text
        except:
            renovation = "No renovation"
        renovations.append(renovation)
        print(f"Renovation: {renovation}")

        try:
            material = driver.find_element(By.XPATH, "//div[@class='MuiTypography-root MuiTypography-overline mui-style-1xqesu' and contains(text(), 'Материал')]/following-sibling::div").text
        except:
            material = "No material"
        materials.append(material)
        print(f"Material: {material}")

        try:
            price = driver.find_element(By.XPATH, "//div[@class='MuiTypography-root MuiTypography-h2 mui-style-86wpc3']").text
        except:
            price = "No price"
        prices.append(price)
        print(f"Price: {price}")

        try:
            adresse = driver.find_element(By.XPATH, "//div[@class='MuiTypography-root MuiTypography-body2 mui-style-31fjox']").text
        except:
            adresse = "No address"
        adresses.append(adresse)
        print(f"Address: {adresse}")

        # Qo'shimcha atributlar
        try:
            elements = driver.find_elements(By.CSS_SELECTOR, ".MuiGrid-root.MuiGrid-container.MuiGrid-spacing-xs-2.mui-style-isbt42")
            for element in elements:
                text = element.text.strip()
                lift = '1' if 'Лифт' in text else ('1' if int(floor.split('/')[1]) > 5 else '0')
                security = '1' if 'Охрана' in text else '0'
                internet = '1' if 'Интернет' in text else '0'
                playgr = '1' if 'Детская площадка' in text else '0'
                swg = '1' if 'Канализация' in text else '0'
                bath = '1' if 'Санузел' in text else '0'
                video = '1' if 'Видеонаблюдение' in text else '0'
                parking = '1' if 'Парковочное место' in text else '0'

        except Exception as e:
            print(f"Error: {e}")

        lifts.append(lift)
        print(f"Lift: {lift}")
        securities.append(security)
        print(f"Security: {security}")
        internets.append(internet)
        print(f"Internet: {internet}")
        playground.append(playgr)
        print(f"Playground: {playgr}")
        sewerages.append(swg)
        print(f"Sewerage: {swg}")
        bathrooms.append(bath)
        print(f"Bathroom: {bath}")
        video_monitor.append(video)
        print(f"Video: {video}")
        parking_spaces.append(parking)
        print(f"Parking: {parking}\n\n")

        son += 1
        print(son)

    counter += 1
    print(counter)


df = pd.DataFrame({
    'Title': titles, 'Room': rooms, 'Area': areas, 'Floor': floors, 'Renovation': renovations, 'Material': materials,
    'Price': prices, 'Address': adresses, 'Lift': lifts, 'Security': securities, 'Internet': internets,
    'Playground': playground, 'Sewerage': sewerages, 'Bathroom': bathrooms, 'Video': video_monitor,
    'Parking': parking_spaces
})


df.to_csv('uy_bor_data.csv', index=False)
print("Data saved to CSV.")



# from selenium import webdriver
# from selenium.common import TimeoutException
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support import expected_conditions
# import pandas as pd
#
# next_url = f"https://uybor.uz/listings?category__eq=7&isNewBuilding__eq=false&page=1"
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#
#
# titles = []
# rooms = []
# areas = []
# floors = []
# renovations = []
# materials = []
# prices = []
# addresses = []
# lifts = []
# securities = []
# internets = []
# playgrounds = []
# sewerages = []
# bathrooms = []
# video_monitors = []
# parking_spaces = []
# air_conditions = []
# furnitures = []
#
# counter = 1
#
#
# for i in range(2):
#     driver.get(next_url)
#     try:
#         next_url = f"https://uybor.uz/listings?category__eq=7&isNewBuilding__eq=false&page={i+1}"
#         print(next_url)
#     except:
#         print('No next page')
#         break
#
#     # float_links = WebDriverWait(driver, 10).until(
#     #     expected_conditions.presence_of_all_elements_located(
#     #         (By.XPATH, "//a[@class='MuiBox-root mui-style-1vssrzj']")))
#
#     flat_urls = []
#     for link in float_links:
#         flat_urls.append(link.get_attribute('href'))
#     print(flat_urls)
#     print(len(flat_urls))
#
#     for furl in flat_urls:
#         driver.get(furl)
#         try:
#             title = driver.find_element(By.XPATH, "//h1[@class='MuiTypography-root MuiTypography-h2 mui-style-1tyknu']").text
#         except:
#             title = "No title"
#
#         titles.append(title)
#         print(counter)
#         print(f"Title: {title}")
#
#         try:
#             room = driver.find_element(By.XPATH, "//div[@class='MuiTypography-root MuiTypography-overline mui-style-1xqesu'"
#                                                  "and contains(text(), 'Комнат')]"
#                                                  "/following-sibling::div").text
#         except:
#             room = 'room'
#         rooms.append(room)
#         print(f"Room: {room}")
#
#         try:
#             area = driver.find_element(By.XPATH, "//div[@class='MuiTypography-root MuiTypography-overline mui-style-1xqesu'"
#                                                  "and contains(text(), 'Площадь')]"
#                                                  "/following-sibling::div").text
#         except:
#             area = 0
#         areas.append(area)
#         print(f"Area: {area}")
#
#         try:
#             floor = driver.find_element(By.XPATH, "//div[@class='MuiTypography-root MuiTypography-overline mui-style-1xqesu'"
#                                                  "and contains(text(), 'Этаж')]"
#                                                  "/following-sibling::div").text
#         except:
#             floor = "floor"
#         floors.append(floor)
#         print(f"Floor: {floor}")
#
#         try:
#             renovation = driver.find_element(By.XPATH,
#                                              "//div[@class='MuiTypography-root MuiTypography-overline mui-style-1xqesu'"
#                                              "and contains(text(), 'Ремонт')]"
#                                              "/following-sibling::div").text
#         except:
#             renovation = "renovation"
#         renovations.append(renovation)
#         print(f"Renovation: {renovation}")
#
#         try:
#             material = driver.find_element(By.XPATH,
#                                            "//div[@class='MuiTypography-root MuiTypography-overline mui-style-1xqesu'"
#                                            "and contains(text(), 'Материал')]"
#                                            "/following-sibling::div").text
#         except:
#             material = 'material'
#         materials.append(material)
#         print(f"Material: {material}")
#
#         try:
#             price = driver.find_element(By.XPATH,
#                                         "//div[@class='MuiTypography-root MuiTypography-h2 mui-style-86wpc3']").text
#         except:
#             price = 'No price'
#         prices.append(price)
#         print(f"Price: {price}")
#
#         try:
#             address = driver.find_element(By.XPATH,
#                                           "//div[@class='MuiTypography-root MuiTypography-body2 mui-style-31fjox']").text
#         except:
#             address = 'No address'
#         addresses.append(address)
#         print(f"Address: {address}")
#
#         try:
#             lift = driver.find_element(By.XPATH,
#                                        "//div[@class='MuiTypography-root MuiTypography-body3 mui-style-xckitu' and contains(text(), 'Лифт')]").text
#         except:
#             print('except qismi!!!!!!!!!!!!!1')
#             try:
#                 if int(floor.split('/')[1]) > 5:
#                     lift = 1
#                 else:
#                     lift = "no lift"
#             except:
#                 lift = "no lift"
#         lifts.append(lift)
#         print(f"Lifts: {lift}")
#
#         try:
#             internet = driver.find_element(By.XPATH,
#                                            "//div[@class='MuiTypography-root MuiTypography-body3 mui-style-xckitu' and contains(text(), 'Интернет')]").text
#         except:
#             internet = "internet"
#         internets.append(internet)
#         print(f"Internet: {internet}")
#
#         try:
#             playground = driver.find_element(By.XPATH,
#                                              "//div[@class='MuiTypography-root MuiTypography-body3 mui-style-xckitu' and contains(text(), 'Детская площадка')]").text
#         except:
#             playground = 'playground'
#         playgrounds.append(playground)
#         print(f"Playground: {playground}")
#
#         try:
#             sewerage = driver.find_element(By.XPATH,
#                                            "//div[@class='MuiTypography-root MuiTypography-body3 mui-style-xckitu' and contains(text(), 'Канализация')]").text
#         except:
#             sewerage = 'sewerage'
#         sewerages.append(sewerage)
#         print(f"Sewerage: {sewerage}")
#
#         try:
#             bathroom = driver.find_element(By.XPATH,
#                                            "//div[@class='MuiTypography-root MuiTypography-body3 mui-style-xckitu' and contains(text(), 'Санузел раздельный')]").text
#         except:
#             bathroom = "bathroom"
#         bathrooms.append(bathroom)
#         print(f"Bathroom: {bathroom}")
#
#         try:
#             video_monitor = driver.find_element(By.XPATH,
#                                                 "//div[@class='MuiTypography-root MuiTypography-body3 mui-style-xckitu' and contains(text(), 'Видеонаблюдение')]").text
#         except:
#             video_monitor = "video_monitor"
#         video_monitors.append(video_monitor)
#         print(f"Video_monitor: {video_monitor}")
#
#         try:
#             parking_space = driver.find_element(By.XPATH,
#                                                 "//div[@class='MuiTypography-root MuiTypography-body3 mui-style-xckitu' and contains(text(), 'Парковочное место')]").text
#         except:
#             parking_space = 'parking_space'
#         parking_spaces.append(parking_space)
#         print(f"Parking_space: {parking_space}")
#
#         try:
#             air_condition = driver.find_element(By.XPATH,
#                                                 "//div[@class='MuiTypography-root MuiTypography-body3 mui-style-xckitu' and contains(text(), 'Кондиционер')]").text
#         except:
#             air_condition = "air_condition"
#         air_conditions.append(air_condition)
#         print(f"Air condition: {air_condition}")
#
#         try:
#             furniture = driver.find_element(By.XPATH,
#                                             "//div[@class='MuiTypography-root MuiTypography-body3 mui-style-xckitu' and contains(text(), 'Мебель')]").text
#         except:
#             furniture = "furniture"
#         furnitures.append(furniture)
#         print(f"Furniture: {furniture}")
#         counter += 1
#         print(f"<--------------------------->\n")
#
#
#
# df = pd.DataFrame({
#     "titles": titles,
#     "rooms": rooms,
#     "areas": areas,
#     "floors": floors,
#     "renovations": renovations,
#     "materials": materials,
#     "prices": prices,
#     "addresses": addresses,
#     "lifts": lifts,
#     "securities": securities,
#     "internets": internets,
#     "playgrounds": playgrounds,
#     "sewerages": sewerages,
#     "bathrooms": bathrooms,
#     "video_monitor": video_monitors,
#     "parking_spaces": parking_spaces,
#     "air_conditions": air_conditions,
#     "furnitures": furnitures,
# })
# df.to_csv("uy_bor_data.csv", index=False)
#
#
#


