from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views

# Create your tests here.


class RecipeURLsTest(TestCase):
    def test_recipe_home_url_is_correct(self):
        url = reverse('recipes:home')
        self.assertEqual(url, '/')

    def test_recipe_category_home_url_is_correct(self):
        url = reverse('recipes:category', kwargs={'category_id': 1})
        self.assertEqual(url, '/recipes/category/1/')

    def test_recipe_url_is_corret(self):
        url = reverse('recipes:recipe', kwargs={'id': 12})
        self.assertEqual(url, '/recipes/12/')


class RecipViewsTest(TestCase):

    def test_recipe_home_view_function_is_correct(self):
        vws = resolve(reverse('recipes:home'))
        self.assertIs(vws.func, views.home)

    def test_recipe_categoy_view_function_is_correct(self):
        vws = resolve(reverse('recipes:category'))
        self.assertIs(vws.func, views.category)

    def test_recipe_recipe_view_function_is_correct(self):
        vws = resolve(reverse('recipes:recipe'))
        self.assertIs(vws.func, views.recipe)
