import requests
from bs4 import BeautifulSoup

def extract_text_from_url(url):
    response=requests.get(url)
    soup= BeautifulSoup(response.text,'html.parser')

    for tag in soup(['script','style']):
        tag.decompose
    
    text=''.join(soup.stripped_strings)
    return text

def company_data(url):
    company_data_extracted=extract_text_from_url(url)
    return company_data_extracted

def job_description(url):
    job_description_extracted=extract_text_from_url(job_description(url))
    return job_description_extracted