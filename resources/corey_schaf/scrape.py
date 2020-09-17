from bs4 import BeautifulSoup
import requests
import csv

###Step 1

# #can pass as string or html as file
# with open('simple.html') as html_file:
#         soup = BeautifulSoup(html_file, 'lxml')
# #find_all return list that match this arguement, vs just one with find
# for article in soup.find_all('div', class_= 'article'):
#     #headline
#     headline = article.h2.a.text
#     print(headline)
#
#     #summary
#     summary = article.p.text
#     print(summary)
#
#     print()

### Step 2

source = requests.get('https://coreyms.com').text

soup = BeautifulSoup(source, 'lxml')

article = soup.find('article')

# #print(article.prettify())
#
# #h2 . anchor. text
# headline = article.h2.a.text
# print(headline)
#
# summary = article.find('div', class_= 'entry-content').p.text
# print(summary)
#
# vid_src = article.find('iframe', class_ = 'youtube-player')['src']
# # print(vid_src)
#
# #question mark specify where url begins
# vid_id = vid_src.split('/')[4]
# vid_id = vid_id.split('?')[0]
# #print(vid_id)
#
# yt_link = f'https://youtube.com/watch?v={vid_id}'
# print(yt_link)

###Step 3

csv_file = open('cms_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])

for article in soup.find_all('article'):

    headline = article.h2.a.text
    print(headline)

    summary = article.find('div', class_ = 'entry-content').p.text
    print(summary)

    try:
        vid_src = article.find('iframe', class_ = 'youtube-player')['src']

        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]

        yt_link = f'https://youtube.com/watch?v={vid_id}'

    except Exception as e:
        yt_link = None

    print(yt_link)

    print()

    csv_writer.writerow([headline, summary, yt_link])

csv_file.close()
