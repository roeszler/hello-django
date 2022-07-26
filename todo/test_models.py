from django.test import TestCase
from .models import Item

# Create your tests here.
class TestModels(TestCase):
    """
    To test that our todo items will be created by default with the done status of false
    """
    def test_done_defaults_to_false(self):
        item = Item.objects.create(name='Test todo item creates with done=false')  # the variable that tests
        self.assertFalse(item.done)  # tests that the above variable is created with done=false by default

    
    def test_item_string_method_returns_name(self):
        """
        To test the string method of our item model
        """
        item = Item.objects.create(name='Test todo item string')
        self.assertEqual(str(item), 'Test todo item string')
