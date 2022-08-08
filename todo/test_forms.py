from django.test import TestCase
from .forms import ItemForm


class TestForms(TestCase):

    def test_item_name_is_required(self):
        """
        Testing that the form is not valid.
        The error occurred on the name field.
        The specific error message is what we expect.
        """
        form = ItemForm({'name': ''})  # simulate a user not filling in name
        self.assertFalse(form.is_valid())  # asserting that the form is not valid
        self.assertIn('name', form.errors.keys())  # assert if there is a name key in the dictionary of form.errors
        self.assertEqual(form.errors['name'][0], 'This field is required.')  # checks that the name field is first on the errors list[0] and indicates that "This filed is required"


    def test_done_field_is_not_required(self):
        """
        Test that the form is valid as it should be even without selecting a done status.
        """
        form = ItemForm({'name': 'Test ToDo Item'})
        self.assertTrue(form.is_valid())


    def test_fields_are_explicit_in_form_metaclass(self):
        """
        Test that the only fields that are displayed in the form are the name and done fields.
        """
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])
