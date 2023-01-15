from bs4 import BeautifulSoup
import requests


def extract_remoteok_jobs(term):
  url = f"https://remoteok.com/remote-{term}-jobs"
  request = requests.get(url, headers={"User-Agent": "Kimchi"})
  results = []
  if request.status_code == 200:
    soup = BeautifulSoup(request.text, "html.parser")
    jobs = soup.find_all("tr", class_="job")
    for job in jobs:
      company = job.find("h3", itemprop="name")
      position = job.find("h2", itemprop="title")
      location = job.find("div", class_="location")
      anchor = job.find("a", itemprop="url")
      link = anchor['href']
      if company:  # company tag가 없으면 아래의 코드에서 error가 발생하므로 if 써주기!
        company = company.string.strip()
      if position:
        position = position.string.strip()
      if location:
        location = location.string.strip()
      if company and position and location:  # company, position, location 값이 모두 있는 구인 정보만 선택하기 위해 if 조건문을 적어줌.
        job = {
          'company': company,
          'position': position,
          'location': location,
          'link': f"https://remoteok.com{link}"
        }
        results.append(job)
  else:
    print("Can't get jobs.")
  return results
