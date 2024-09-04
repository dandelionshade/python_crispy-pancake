import requests
from bs4 import BeautifulSoup
import json

def fetch_movie_data(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    movies = []
    for item in soup.select('.item'):
        title = item.find('a').find('img')['alt']
        rating = item.find('span', {'class': 'rating_num'}).text
        movies.append({'title': title, 'rating': float(rating)})
    return movies

def fetch_multiple_pages(base_url, num_pages=10):
    all_movies = []
    for page in range(num_pages):
        url = f"{base_url}?start={page * 25}&filter="
        movies = fetch_movie_data(url)
        all_movies.extend(movies)
    return all_movies

def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    base_url = 'https://movie.douban.com/top250 '
    all_movies = fetch_multiple_pages(base_url)
    save_to_json(all_movies, '../douban_crawler/data/douban_movies.json')