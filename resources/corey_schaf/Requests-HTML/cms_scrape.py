###Part 1
import csv
from requests_html import HTML, HTMLSession

# with open('simple.html') as html_file:
#     source = html_file.read()
#     html =  HTML(html = source)
# #without the tags use text with tags use html
# print(html.text)
# #dynanically generated data is a bit weird
#
# #first = true first element found within that search
# # #footer return id footer
# match = html.find('title', first = True)
# #html or text
# print(match.text)

### Part 2
# with open('simple.html') as html_file:
#     source = html_file.read()
#     html = HTML(html = source)
#
# articles = html.find('div.article')
# for article in articles:
#
#     headline = article.find('h2', first = True).text
#     summary = article.find('p', first = True).text
#
#     print(headline)
#     print(summary)
#     print()

###Part 3 Scraping from corey's website

# csv_file = open('cms_scrape.csv', 'w')
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(['headline', 'summary', 'video'])

# session = HTMLSession()
# r = session.get('https://coreyms.com/')
#
# #do not set first = True if you want all articles
# articles = r.html.find('article')
#
# for article in articles:
#
#     headline = article.find('.entry-title-link', first = True).text
#     #print(headline)
#
#     summary = article.find('.entry-content p', first = True).text
#     #print(summary)
#     try:
#
#         vid_src = article.find('iframe', first = True).attrs['src']
#         #attrs for attributes
#
#         vid_id = vid_src.split('/')[4]
#         vid_id = vid_id.split('?')[0]
#
#         yt_link = f'https://youtube.com/watch?v={vid_id}'
#     except Exception as e:
#         yt_link = None
#     print(yt_link)
#     print()
#
#     csv_writer.writerow([headline, summary, yt_link])
#
# csv_file.close()

###Part 3
#gives set of links in a website
#absolute links
# for link in r.html.links:
#     print(link)

###Part 4 Dynamic links

with open('simple.html') as html_file:
    source = html_file.read()
    html = HTML(html= source)
    html.render()

match = html.find('#footer', first = True)
#dynamic text not included in response here
print(match.html)
