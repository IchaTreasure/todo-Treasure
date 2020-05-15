from django.test import TestCase
from .forms import Item

# Create your tests here.
class TestItemModel(TestCase):
    
    def test_done_defaults_to_false(self):
        item = Item(name = 'create a test')
        item.save()
        self.assertEqual(item.name, 'create a test')
        self.assertFalse(item.done)
        
    def test_can_create_an_item_with_a_name_and_status(self):
        item = Item(name = 'create a test', done=True)
        item.save()
        self.assertEqual(item.name, 'create a test')
        self.assertTrue(item.done)
        
    def test_item_as_a_string(self):
        item = Item(name = 'create a test')
        self.assertEqual('create a test', str(item))
    
