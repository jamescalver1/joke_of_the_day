import requests

from bs4 import BeautifulSoup

class joke_creator:

    def get_joke_tag(self, tag):

        return tag.name == "a" and tag.has_attr("class") and tag.has_attr("data-description")

    def create_joke(self):

        response = requests.get("https://www.ajokeaday.com/")
        soup = BeautifulSoup(response.content, 'html.parser')
        tag = soup.find_all(self.get_joke_tag)[0]
        return ''.join(tag.get("data-description").splitlines())

def get_joke_creator():
    return joke_creator()