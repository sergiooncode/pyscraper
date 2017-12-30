from scraper.models import Book
from scraper.webdriver import MyWebdriver
from scraper import db

BASE_URL = 'http://books.toscrape.com/'


def go_scrape():
    books = {}
    with MyWebdriver() as br:
        br.browser.set_window_size(1024, 768)
        br.browser.get(BASE_URL)
        books_with_no_serial_number = []
        for book_element in get_all_books(br):
            import bpdb;bpdb.set_trace()
            book_link_element = get_link_element(book_element)
            books_with_no_serial_number.append(
                {
                    'title': get_book_title(),
                    'link': get_book_url(book_link_element),
                    'price': get_book_price(book_element)
                }
            )

        for book_properties in books_with_no_serial_number:
            br.browser.get(book_properties['link'])
            serial_number_row = br.browser.find_elements_by_xpath("//table[@class='table table-striped']/tbody/tr")[0]
            books[serial_number_row.text.split(' ')[1]] = book_properties
    return books


def store(books):
    book_objects = []
    for book in books.items():
        book_objects.append(
            Book(
                title=book[1]['title'],
                serial_number=book[0],
                price=book[1]['price'],
                link=book[1]['link']
            )
        )
    db.bulk_save_objects(book_objects)
    db.commit()


def get_all_books(br):
    return br.browser.find_elements_by_xpath("//article[@class='product_pod']")


def get_book_price(element):
    return element.find_element_by_xpath(".//div[@class='product_price']/p["
                                         "@class='price_color']").text


def get_book_url(link_element):
    return link_element.get_attribute('href')


def get_book_title(link_element):
    return link_element.get_attribute('title')


def get_link_element(element):
    return element.find_element_by_xpath(".//h3/a")
