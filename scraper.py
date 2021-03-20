from bs4 import BeautifulSoup

from request_manager import RequestManager

class Scraper:
    def __init__(self, url):
        # We will take in the url and then pass it to The RequestManager. We will 
        # save the result as `page`
        self.page = BeautifulSoup(
            RequestManager.get_page(url).content,
            'html.parser'
        )

    def print_raw_page(self):
        print(self.page)

    def print_pretty_page(self):
        print(self.page.prettify())

    def print_page_text(self):
        page_text = self.page.get_text()
        page_text_without_blank_lines = page_text.strip()
        print(page_text_without_blank_lines)

    def find_tags_by_name(self, tag_name):
        """
        Takes in an HTML tag name and will return a list of all the tags found on the page

        :param tag_name string: A string representing an HTML tag(e.g. h1)

        :return: A list of all the found tags on the page
        :rtype list[bs4.element.Tag]:
        """
        return self.page.find_all(tag_name)

    def get_all_attributes_for_tag(self, tag_name, attribute):
        """
        Given a HTML tag name and an attribute to find, return a map where the key is
        any tag where the attribute is found and the value is the value of the attribute
        
        :param tag_name string: Name of HTML tag
        :param attribute string: Name of HTML attribute

        :return: A dict of tags to found attributes
        :rtype: dict[bs4.element.Tag, string]
        """
        tag_to_attribute_map = {}

        tags = self.find_tags_by_name(tag_name)

        for tag in tags:
            if tag.has_attr(attribute):
                tag_to_attribute_map[tag] = tag[attribute]

        return tag_to_attribute_map


    
        