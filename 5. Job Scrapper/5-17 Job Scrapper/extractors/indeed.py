from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from extractors.wwr import extract_wwr_jobs


def get_page_count(keyword):
  options = Options()
  options.add_argument("--no-sandbox")
  options.add_argument("--disable-dev-shm-usage")

  browser = webdriver.Chrome(options=options)

  base_url = "https://kr.indeed.com/jobs?q="

  browser.get(f"{base_url}{keyword}")

  soup = BeautifulSoup(browser.page_source, "html.parser")
  pagination = soup.find("nav", class_="ecydgvn0")
  pages = pagination.find_all("div", recursive=False)
  count = len(pages)
  if count >= 6:
    return 5
  elif count == 0:
    return 1
  elif 2 <= count <= 5:
    return (count - 1)


def extract_indeed_jobs(keyword):
  pages = get_page_count(keyword)
  results = []

  for page in range(pages):
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    browser = webdriver.Chrome(options=options)

    base_url = "https://kr.indeed.com/jobs?q="
    final_url = f"{base_url}{keyword}&start={page*10}"
    print("Requesting", final_url)
    browser.get(final_url)

    soup = BeautifulSoup(browser.page_source, "html.parser")
    job_list = soup.find("ul", class_="jobsearch-ResultsList")
    jobs = job_list.find_all('div', recursive=False)

    for job in jobs:
      zone = job.find("div", class_="mosaic-zone")
      if zone == None:
        anchor = job.select_one("h2 a")
        title = anchor['aria-label']
        link = anchor['href']
        company = job.find("span", class_="companyName")
        location = job.find("div", class_="companyLocation")
        job_data = {
          'link': f"https://kr.indeed.com{link}",
          'company': company.string,
          'location': location.string,
          'position': title
        }
        results.append(job_data)
  return results