import requests
from bs4 import BeautifulSoup
import time

print("Put some skill that you are not familiar skill")
unfamiliar_skill = input('>')
print(f'filtering out..... {unfamiliar_skill}')

def find_jobs():
	response = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=').text
	soup = BeautifulSoup(response, 'lxml')
	jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
	for index, job in enumerate(jobs):
	    published_date = job.find('span', class_='sim-posted').span.text
	    if 'few' in published_date:

	        # Remove excessive spaces, while keeping valid spaces between words
	        company_name = job.find('h3', class_='joblist-comp-name').text.strip()
	        company_name = ' '.join(company_name.split())  # Clean extra spaces within the text
	        

	        skills = job.find('div', class_='srp-skills').text.strip()
	        skills = ' '.join(skills.split())  # Clean extra spaces within the text
	        more_info = job.header.h2.a['href']

	        if unfamiliar_skill not in skills:
	        	with open(f'post/{index}.txt', 'w') as f:
			        f.write(f"Company name: {company_name}\n")
			        f.write(f"Required Skills: {skills}\n")
			        f.write(f"More Info: {more_info}\n")
		        	f.write('-'*50)
		        	print(f'file saved: {index}')

if __name__ == '__main__':
	while True:
		find_jobs()
		time_wait = 10
		print(f'Waiting {time_wait} minutes.....')
		time.sleep(time_wait*60)
