from configparser import ConfigParser
import main
config = ConfigParser()
# read url
config.read('url.ini')
url = [config['dailythanthi']['url']]
# print url
print(url)

# step 1 extract url from dailythanthi.com
urls = main.get_url(url)
extract_urls = main.multi_extract_url(urls)
merge_url = main.merge_url(extract_urls)


# step 2 extract url from dailythanthi.com child urls
urls_again = main.get_url(merge_url)
extract_urls_again = main.multi_extract_url(urls_again)
merge_url_again = main.merge_url(extract_urls_again)

# print urls from dailythanthi.com child urls
print(merge_url_again)
print(len(merge_url_again))

# print words from from dailythanthi.com child urls
print(main.Tamilwebscraping(merge_url_again))
print(len(main.Tamilwebscraping(merge_url_again)))
