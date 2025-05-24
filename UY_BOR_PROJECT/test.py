# from selenium import webdriver
# from selenium.common import TimeoutException
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions
# from webdriver_manager.chrome import ChromeDriverManager
# import pandas as pd
#
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#
# # Bo'sh ro'yxatlar
# titles, rooms, areas, floors, renovations, materials = [], [], [], [], [], []
# prices, addresses, lifts, securities, internets = [], [], [], [], []
# playgrounds, sewerages, bathrooms, video_monitors = [], [], [], []
# parking_spaces, air_conditions, furnitures = [], [], []
#
# counter = 1
#
# # Sahifalar bo'yicha yurish
# for i in range(99):
#     next_url = f"https://uybor.uz/listings?category__eq=7&isNewBuilding__eq=false&page={i+1}"
#     driver.get(next_url)
#     print(f"Page: {next_url}")
#
#     try:
#         flat_links = WebDriverWait(driver, 15).until(
#             expected_conditions.presence_of_all_elements_located(
#                 (By.XPATH, "//a[@class='MuiBox-root mui-style-1vssrzj']")
#             )
#         )
#     except TimeoutException:
#         print("❌ Uylarga havolalar topilmadi.")
#         continue
#
#     flat_urls = [link.get_attribute('href') for link in flat_links]
#     print(f"🏘 Uylar soni: {len(flat_urls)}")
#
#     for furl in flat_urls:
#         driver.get(furl)
#         print(f"\n{counter}. {furl}")
#
#         # Har bir elementni alohida tekshirib olish
#         def safe_find(xpath, default="N/A"):
#             try:
#                 return driver.find_element(By.XPATH, xpath).text
#             except:
#                 return default
#
#         titles.append(safe_find("//h1[@class='MuiTypography-root MuiTypography-h2 mui-style-1tyknu']", "No title"))
#         rooms.append(safe_find("//div[contains(text(), 'Комнат')]/following-sibling::div", "No room"))
#         areas.append(safe_find("//div[contains(text(), 'Площадь')]/following-sibling::div", "No area"))
#         floors.append(safe_find("//div[contains(text(), 'Этаж')]/following-sibling::div", "No floor"))
#         renovations.append(safe_find("//div[contains(text(), 'Ремонт')]/following-sibling::div", "No renovation"))
#         materials.append(safe_find("//div[contains(text(), 'Материал')]/following-sibling::div", "No material"))
#         prices.append(safe_find("//div[@class='MuiTypography-root MuiTypography-h2 mui-style-86wpc3']", "No price"))
#         addresses.append(safe_find("//div[@class='MuiTypography-root MuiTypography-body2 mui-style-31fjox']", "No address"))
#
#         # Lift
#         try:
#             lift = driver.find_element(By.XPATH, "//div[contains(text(), 'Лифт')]").text
#         except:
#             try:
#                 floor_info = floors[-1]
#                 lift = "1" if int(floor_info.split('/')[1]) > 5 else "no lift"
#             except:
#                 lift = "no lift"
#         lifts.append(lift)
#
#         # Security (Kiritildi)
#         securities.append(safe_find("//div[contains(text(), 'Охрана')]", "No security"))
#
#         internets.append(safe_find("//div[contains(text(), 'Интернет')]", "No internet"))
#         playgrounds.append(safe_find("//div[contains(text(), 'Детская площадка')]", "No playground"))
#         sewerages.append(safe_find("//div[contains(text(), 'Канализация')]", "No sewerage"))
#         bathrooms.append(safe_find("//div[contains(text(), 'Санузел раздельный')]", "No bathroom"))
#         video_monitors.append(safe_find("//div[contains(text(), 'Видеонаблюдение')]", "No video_monitor"))
#         parking_spaces.append(safe_find("//div[contains(text(), 'Парковочное место')]", "No parking_space"))
#         air_conditions.append(safe_find("//div[contains(text(), 'Кондиционер')]", "No air_condition"))
#         furnitures.append(safe_find("//div[contains(text(), 'Мебель')]", "No furniture"))
#
#         counter += 1
#
# # DataFrame yaratish
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
#     "furnitures": furnitures
# })
#
# # CSV faylga yozish
# df.to_csv("uy_bor_data.csv", index=False)
# print("\n✅ CSV fayl saqlandi: uy_bor_data.csv")
#
# # Brauzerni yopish
# driver.quit()



# ************* #
