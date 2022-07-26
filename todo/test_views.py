from django.test import TestCase
from .models import Item

# Create your tests here.
class TestViews(TestCase):
    """
    Inherits the built-in test case class to contain all tests
    """

    def test_get_todo_list(self):
        """
        Test READ an item
        To test the HTTP responses of the todo_list view.
        """
        response = self.client.get('/')  # to get the home page
        self.assertEqual(response.status_code, 200)  # check the status code is successful (200)
        self.assertTemplateUsed(response, 'todo/todo_list.html')  # to confirm the view uses the correct template
    
    
    def test_get_add_item_page(self):
        """
        Test READ an item
        To test the HTTP responses of the add_item view.
        """
        response = self.client.get('/add')  # to get the add_item page
        self.assertEqual(response.status_code, 200)  # check the status code is successful (200)
        self.assertTemplateUsed(response, 'todo/add_item.html')


    def test_get_edit_item_page(self):
        """
        Test READ an item
        To test the HTTP responses of the edit_item view.
        """
        item = Item.objects.create(name='Test Todo item')  # import the item model at the top of the page & create an item to use in this test
        response = self.client.get(f'/edit/{item.id}')  # to get the edit_item page using drill down within a template literals
        self.assertEqual(response.status_code, 200)  # check the status code is successful (200)
        self.assertTemplateUsed(response, 'todo/edit_item.html')


    def test_can_add_item(self):
        """
        Test CREATE an item
        Test response equal to self.client.post on the 'add' URL
        That it returns to the home page
        """
        response = self.client.post('/add', {'name': 'Test added item'})  # assigning a name to the item (like we just submitted the item form)
        self.assertRedirects(response, '/')  # To confirm that it redirects back to home page.
    
    def test_can_toggle_item(self):
        """
        Test UPDATE an item
        Set the input to test and its status is done
        Get it's id within the function
        Test that it returns to home after the function has run
        Retrieve the updated item id and Test that item is no longer there 
        by testing with assertFalse() Django funciton
        """
        item = Item.objects.create(name='Test todo item toggle', done=True)  # create the content that tests from the model at top of the page
        response = self.client.get(f'/toggle/{item.id}')  # to get the id using drill down within a template literals
        self.assertRedirects(response, '/')  # To confirm that it redirects back to home page.
        updated_item = Item.objects.get(id=item.id)  # try to get the toggle item from the db as a safety check
        self.assertFalse(updated_item.done)  # to check its done status
    
    def test_can_delete_item(self):
        """
        Test DELETE an item
        Set the input to test and it's id within the function 
        Test that it returns to home 
        Check that item is no longer there by retrieving and testing
        """
        item = Item.objects.create(name='Test todo item delete')  # create the content that tests from the model at top of the page
        response = self.client.get(f'/delete/{item.id}')  # to get the id using drill down within a template literals
        self.assertRedirects(response, '/')  # To confirm that it redirects back to home page. 
        existing_items = Item.objects.filter(id=item.id)  # try to get the deleted item from the db as a final check
        self.assertEqual(len(existing_items), 0)  # to check that the deleted item is no longer there
        
    
    def test_can_edit_item(self):
        """
        Request a response from the server using post and post an updated name
        Test that the response sends us back to home page
        """
        item = Item.objects.create(name='Test todo item edit')  # create the content that tests from the model at top of the page
        response = self.client.post(f'/edit/{item.id}', {'name': 'Updated Name'})  # request a response from the server using post and post an updated name
        self.assertRedirects(response, '/')
        updated_item = Item.objects.get(id=item.id)  # get the updated item from the db as a final check
        self.assertEqual(updated_item.name, 'Updated Name')  # test that the updated items equal name as updated name
        
    
    # def test_this_thing_works_pass(self):
    #     self.assertEqual(1, 1)
    # def test_this_thing_works2_fail(self):
    #     self.assertEqual(1, 3)
    # def test_this_thing_works3_syntax(self):
    #     self.assertEqual(1, )
    # def test_this_thing_works4_input(self):
    #     self.assertEqual(1, 'bob')
