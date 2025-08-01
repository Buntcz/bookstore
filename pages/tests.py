from django.test import TestCase
from django.urls import reverse,resolve

from .views import HomePageView,AboutPageView

# Create your tests here.

class HomePageTests(TestCase):
    def setUp(self):
        url = reverse("home")
        self.response = self.client.get(url)

    def test_url_exists_at_correct_location(self):
        self.assertEqual(self.response.status_code,200)

    def test_correct_template_used(self):
        self.assertTemplateUsed(self.response, "home.html")

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, "homepage")
    
    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "I am not on the web page")

    def test_homepage_resolves_homepageview(self):
        view = resolve("/")
        self.assertEqual(view.func.__name__,HomePageView.as_view().__name__)

class AboutPageTests(TestCase):
    def setUp(self):
        url = reverse("about")
        self.response = self.client.get(url)
    
    def test_url_exists_at_correct_location(self):
        self.assertEqual(self.response.status_code,200)
    
    def test_correct_template_used(self):
        self.assertTemplateUsed(self.response,"about.html")
    
    def test_aboutpage_contains_correct_html(self):
        self.assertContains(self.response,"About Page")
    
    def test_aboutpage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response,"I am not on the page")
    
    def test_aboutpages_resolves_aboutpageview(self):
        view = resolve("/about/")
        self.assertEqual(view.func.__name__,AboutPageView.as_view().__name__)