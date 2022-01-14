from configparser import ConfigParser
import main
config = ConfigParser()
print(config.sections())
config.read('url.ini')
print(config.sections())
url = [config['dailythanthi']['url']]

print(url)


urls = main.get_url(url)
extract_urls = main.multi_extract_url(urls)
merge_url = main.merge_url(extract_urls)



urls_again = main.get_url(merge_url)
extract_urls_again = main.multi_extract_url(urls_again)
merge_url_again = main.merge_url(extract_urls_again)

print(merge_url_again)
print(len(merge_url_again))


print(main.Tamilwebscraping(merge_url_again))
print(len(main.Tamilwebscraping(merge_url_again)))

