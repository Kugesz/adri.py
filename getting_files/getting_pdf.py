from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import requests

from datetime import datetime, timedelta

import config

webpage_url = config.vasvari_url

def downloading_pdf():
  driver = webdriver.Chrome()

  driver.get(webpage_url)

  next_day = datetime.now() + timedelta(days=1)
  formatted_date = next_day.strftime("%Y. %m. %d.")
  link_name = "ÓRACSERÉK: " + formatted_date
  print(link_name)
  # Getting the google drive link
  try:
    a_tag = driver.find_element(By.XPATH, f"//a[contains(text(), '{link_name}')]")
    href = a_tag.get_attribute("href")
    id = href.split("/")[-2]
    download_link = f"https://drive.google.com/u/3/uc?id={id}"

    return download_link
  except Exception as e:
    print("An error has accourd when getting the download link.")

  driver.quit()

  # Downloading pdf
  try:
    response = requests.get(download_link)
    open("../files/file.pdf", "wb").write(response.content)
  except Exception as e:
    print(e)
    print("An error has accourd when downloading and convertin the PDF file.")
