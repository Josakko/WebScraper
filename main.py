import requests
from bs4 import BeautifulSoup
import csv


url = input("Enter a URL to scrape: ")

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

print("What data do you want to extract?")
print("1. Title")
print("2. Meta description")
print("3. Links")
print("4. Metadata")
print("5. Text data")
print("6. Social Media")

choices = input("Enter your choices (comma-separated, e.g. 1,3,5): ")

choices_list = choices.split(',')
data = {}
for choice in choices_list:
    if choice == '1':
        data['Title'] = soup.title.string
    elif choice == '2':
        data['Meta Description'] = soup.find('meta', attrs={'name': 'description'})['content']
    elif choice == '3':
        links = [link.get('href') for link in soup.find_all('a') if link.get('href')]
        data['Links'] = links
    elif choice == '4':
        metadata = {}
        for tag in soup.find_all('meta'):
            name = tag.get('name', '')
            if name:
                metadata[name] = tag.get('content', '')
        data.update(metadata)
    elif choice == '5':
        text_data = soup.get_text()
        data['Text Data'] = text_data
    elif choice == '6':
        social_media = {}
        social_tags = soup.find_all('a', href=True)
        for tag in social_tags:
            url = tag['href']
            if 'twitter.com' in url:
                social_media['Twitter'] = url
            elif 'facebook.com' in url:
                social_media['Facebook'] = url
            elif 'instagram.com' in url:
                social_media['Instagram'] = url
            elif 'linkedin.com' in url:
                social_media['LinkedIn'] = url
            elif 'youtube.com' in url:
                social_media['YouTube'] = url
            else:
                pass
        data.update(social_media)
    else:
        print(f"Invalid choice: {choice}")
        
if data:
    with open('data.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(data.keys())
        writer.writerow(data.values())
