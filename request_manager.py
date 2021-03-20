import requests
from requests.exceptions import ConnectionError, MissingSchema

class RequestManager:
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
    }

    @classmethod
    def get_page(cls, url):
        """
        Takes in a string url and returns HTTP Response

        :param url string: String representing a URL

        :return: An Http Response containing the HTML for the page
        :rtype: HttpResponse
        """
        try:
            return requests.get(url, headers=cls.HEADERS)
        except MissingSchema:
            print('Invalid schema entered. Please ensure your url uses either HTTP or HTTPS.')
        except ConnectionError:
            print('Failed to connect. Please check that the provided url is correct.')
