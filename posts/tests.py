from django.test import TestCase
from django.urls import reverse

from .models import Post


# Create your tests here.


class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(text="This is a test!")

    def test_model_content(self):
        self.assertEqual(self.post.text, "This is a test!")

    def test_url_exists(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_correct_name(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "posts/home.html")

    def test_template_content(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "This is a test")

    def test_homepage(self):  # correct way (Best Practice)
        response = self.client.get(reverse("home"))
        self.assertContains(response, "This is a test!")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "posts/home.html")
