# pylint: disable-all
from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve

from lists.views import home_page


class HomePageTest(TestCase):
    
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        doc_html = response.content.decode('utf8')

        self.assertTrue(doc_html.startswith('<!DOCTYPE html>'))
        self.assertIn('<title>To-Do lists</title>', doc_html)
        self.assertTrue(doc_html.endswith('</html>'))

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)


class SmokeTest(TestCase):

    def test_bad_maths(self):
        self.assertNotEqual(1 + 1, 3)
