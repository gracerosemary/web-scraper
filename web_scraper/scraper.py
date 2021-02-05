import requests
from bs4 import BeautifulSoup
import re

def get_citations_needed_count(url):
    """Count function gets the number of citations needed.

    Args:
        url (str): website link string

    Returns:
        int: int representing number of citations needed
    """
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    result = soup.find(id='bodyContent')
    count = len(result.find_all('a', title='Wikipedia:Citation needed'))
    return count 

def get_citations_needed_report(url):
    """String of sentence(s) that needs a citation.

    Args:
        url (str): website link string

    Returns:
        str: string formatted with each citation needed on own line, in the order found
    """
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    body_results = soup.find(id='bodyContent')
    citation_results = body_results.find_all('p')

    final_result = []
    for result in citation_results:
        section = result.find(title='Wikipedia:Citation needed')
        if section:
            x = re.sub("\[?[0-9]?[0-9]?\]?(.*?)\[[0-9][0-9][0-9]?\]","",result.text)
            x = x.strip('\n')
            final_result.append(x)
    return '\n'.join(final_result)

def get_citations_needed_section(url):
    """String of passage that contains the missing citation. 

    Args:
        url (str): website link string

    Returns:
        str: string formatted with the passage, in the order found
    """
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    body_results = soup.find(id='bodyContent')
    citation_results = body_results.find_all('p')
    
    for result in citation_results:
        section = result.find(title='Wikipedia:Citation needed')
        if section:
            x = re.sub("\[?[0-9]?[0-9]?\]?(.*?)\[[0-9][0-9][0-9]?\]", "", result.text)
            print(f"Relevant passage:\n{result.text}")
            # return f"Relevant passage:\n{result.text}"

if __name__ == '__main__':
    url = 'https://en.wikipedia.org/wiki/GameStop'
    # print(get_citations_needed_count(url))
    print(get_citations_needed_report(url))
