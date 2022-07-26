from django.test import TestCase

# Create your tests here.
class TestDjango(TestCase):
    """
    Inherits the built-in test case class to contain all tests
    """
    
    def test_this_thing_works_pass(self):
        self.assertEqual(1, 1)
    
    # def test_this_thing_works2_fail(self):
    #     self.assertEqual(1, 3)
    # def test_this_thing_works3_syntax(self):
    #     self.assertEqual(1, )
    # def test_this_thing_works4_input(self):
    #     self.assertEqual(1, 'bob')
