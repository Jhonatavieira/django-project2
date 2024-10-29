from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views


class RecipViewsTest(TestCase):

    def test_recipe_home_view_function_is_correct(self):
        vws = resolve(reverse('recipes:home'))
        self.assertIs(vws.func, views.home)

    def test_recipe_category_view_function_is_correct(self):
        vws = resolve(reverse('recipes:category'))
        self.assertIs(vws.func, views.category)

    def test_recipe_recipe_view_function_is_correct(self):
        vws = resolve(reverse('recipes:recipe'))
        self.assertIs(vws.func, views.recipe)

    def test_recipe_home_view_return_status_code_200_OK(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')
