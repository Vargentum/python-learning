from django.core.urlresolvers import reverse
from django.test import TestCase


class TestPostsRead(TestCase):
    fixtures = ['initial_data.json']

    def test_viewable_blog_main_page(self):
        response = self.client.get(reverse('blog'))
        self.assertEqual(response.status_code, 200)

    def test_viewable_post_list_pages(self):
        page1 = self.client.get(reverse('post_list', kwargs={'page': 1}))
        self.assertEqual(page1.status_code, 200)

        page2 = self.client.get(reverse('post_list', kwargs={'page': 2}))
        self.assertEqual(page2.status_code, 200)

    def test_viewable_post_detail(self):
        first_post = self.client.get(reverse('post_detail', kwargs={'pk': 1}))
        self.assertContains(first_post, 'Kyocera', status_code=200)


class TestPostsModification(TestCase):
    fixtures = ['initial_data.json']

    def test_viewable_post_add_page(self):
        response = self.client.get(reverse('post_create'))
        self.assertEqual(response.status_code, 200)

    def test_viewable_post_update_page(self):
        response = self.client.get(reverse('post_update', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)

    def test_viewable_post_delete_page(self):
        response = self.client.get(reverse('post_delete', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)


class TestCategoriesRead(TestCase):
    fixtures = ['initial_data.json']

    def test_viewable_categories_list(self):
        response = self.client.get(reverse('category_list'))
        self.assertEqual(response.status_code, 200)

    def test_viewable_category_detail(self):
        response = self.client.get(reverse('category_detail', kwargs={'category': 1}))
        self.assertEqual(response.status_code, 200)
