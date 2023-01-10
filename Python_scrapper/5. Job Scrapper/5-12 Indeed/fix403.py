from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from bs4 import BeautifulSoup
# from extractors.wwr import extract_wwr_jobs

# base_url = "https://kr.indeed.com/jobs?q="
# search_term = "python"

# response = get(f"{base_url}{search_term}")

# if response != 200:
#   print("Can't request page.")
# else:
#   print(response.text)

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

browser = webdriver.Chrome(options=options)

browser.get(
  "https://kr.indeed.com/jobs?q=python&l=&from=searchOnHP&vjk=1015284880e2ff62"
)

print(browser.page_source)
