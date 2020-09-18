from requests_html import HTML, HTMLSession

with open('simple.html') as html_file:
    source = html_file.read()
    html = HTML(html= source)
    html.render()

match = html.find('#footer', first = True)
#dynamic text not included in response here
print(match.html)
