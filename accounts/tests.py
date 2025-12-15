from django.test import TestCase

# Create your tests here.
class AccountsTests(TestCase):
    def test_register(self):
        self.client.post()