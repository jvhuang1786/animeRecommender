import re
import requests
import pandas as pd
from bs4 import BeautifulSoup

def get_dict_ratings_anime(anime, ratings, genres, anime_img, anime_link, episodes):

    df_ratings = pd.DataFrame(ratings)

    dict_ratings = {
        'anime' : anime,
        'anime_img' : anime_img,
        'anime_url' : anime_link,
        'episodes' : episodes,
        'votes' : df_ratings['rate_votes'].sum(),
        'weight' : df_ratings['rate_weight'].sum(),
        'rate' : round(df_ratings['rate_weight'].sum() / df_ratings['rate_votes'].sum(), 2),
    }

    # For each rating
    for i in range(1,6):
        dict_ratings[f'rate_{i}'] = df_ratings[df_ratings['rate_class'] == i]['rate_votes'].values[0]

    return {**genres, **dict_ratings}


url = 'https://www.crunchyroll.com/sitemap'
request = requests.get(url)
soup = BeautifulSoup(request.content)

sitemap = soup.findAll('loc')

languages_symbols = ['en-gb', 'es', 'es-es', 'pt-br', 'pt-pt', 'fr', 'de', 'ar', 'it', 'ru']
languages_symbols_url = [ f'https://www.crunchyroll.com/{i}' for i in languages_symbols]

anime_links = []
for url in sitemap:
    request = requests.get(url.text)
    soup = BeautifulSoup(request.content)

    for link in soup.findAll('loc'):
        link = link.text

        # Looks only urls with len greater than https://www.crunchyroll.com/
        if len(link) > 28:
            if link.startswith('https://www.crunchyroll.com/') and 'forumtopic' not in link:
                if not link in languages_symbols_url:
                    re_search_tabs = re.search(r'(https://www\.crunchyroll\.com/.*)/', link)
                    if not re_search_tabs:
                        anime_links.append(link)


anime_links = list(set(anime_links))


with open("animes_list_urls.txt","w+") as f:
    f.write('\n'.join(anime_links))


anime_ratings = []
for anime_link in anime_links:
    request = requests.get(anime_link)
    soup = BeautifulSoup(request.content)
    rating = soup.find('ul', {'class' : 'rating-histogram'})

    anime = soup.find('div', {'id' : 'showview-content-header'}).find('span').text
    anime_img = soup.find('img', {'class' : 'poster xsmall-margin-bottom'})['src']
    content_videos = soup.find('div', {'id' : 'showview_content_videos'})
    episodes = len(content_videos.findAll('a', {'class' : 'episode'}))

    ratings = []
    for rate in rating.findAll('li'):
        rate_class = rate.find('div', {'class' : 'left num strong'})
        rate_votes = rate.find(lambda tag: tag.name == 'div' and tag['class'] == ['left'])
        rate_votes = re.search(r'(\d+)', rate_votes.text)
        if rate_class:
            rate_class = int(rate_class.text)
            if rate_votes:
                rate_votes = int(rate_votes.group(1))
            else :
                rate_votes = 0

            ratings.append({'rate_class' : rate_class, 'rate_votes' : rate_votes,
                            'rate_weight' : rate_class * rate_votes})

    genres = {}
    for link in soup.findAll(lambda tag: tag.name == 'a' and tag.get('class') == ['text-link']):
        if 'genres' in link['href']:
            genres[f'genre_{link.text}'] = 1

    anime_ratings.append(get_dict_ratings_anime(anime, ratings, genres, anime_img, anime_link, episodes))


df_ratings = pd.DataFrame(anime_ratings).fillna(0)

# Sort columns
cols_genres = [col for col in df_ratings.columns if col.startswith('genre_')]
cols_genres.sort()

df_ratings = df_ratings[['anime', 'anime_url', 'anime_img', 'episodes', 'votes', 'weight', 'rate',
                         'rate_1', 'rate_2', 'rate_3', 'rate_4', 'rate_5'] + cols_genres]

df_ratings.sort_values(['votes', 'rate'], ascending=False).to_csv('../data/animes.csv', index=False)
