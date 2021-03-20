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

    def get_tags_by_name(self, tag_name):
        """
        Takes in an HTML tag name and will return a list of all the tags found on the page

        :param tag_name string: A string representing an HTML tag(e.g. h1)

        :return: A list of all the found tags on the page
        :rtype: list[bs4.element.Tag]
        """
        return self.page.find_all(tag_name)

    def get_text_content_by_name(self, tag_name):
        """
        Takes in an HTML tag name and will return any text inside the returned tags
        
        :param tag_name string: A string representing an HTML tag

        :return: A list of all the text inside the found tags
        :rtype: list[string]
        """
        results = self.find_tags_by_name(tag_name)
        return [result.text.strip() for result in results]

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

        tags = self.get_tags_by_name(tag_name)

        for tag in tags:
            tag_to_attribute_map[tag] = tag.get(attribute)

        return tag_to_attribute_map

    def get_table_contents(self):
        """
        Finds a table on a webpage and parses it. The return value will be
        an array where is element is dict representing a row.

        :return: A list of dicts representing each row of data. Each dict will have column
            header as keys and the cell value as value
        :rtype: list[dict[str, str]]
        """
        data = []
        tables = self.get_tags_by_name('table')

        for table in tables:
            table_header = table.find_all('th')

            # The order of columns does matter here. We will map the actual rows in the same order
            # and assume that the data will end up in the correct spot
            columns = [column.text.strip() for column in table_header]

            rows = table.find_all('tr')

            for row in rows:
                row_data = {}
                cells = row.find_all('td')

                for index, cell in enumerate(cells):
                    row_data[columns[index]] = cell.text.strip()

                # No purpose in adding empty rows
                if len(row_data.keys()) > 0:
                    data.append(row_data)
        
        return data


    
        