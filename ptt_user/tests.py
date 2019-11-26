from django.test import TestCase

# Create your tests here.
from .mysql_select_from_ptt import count_keyword

class sqlTestCase(TestCase):
    def setUp(self):
        pass

    def test_sql_type(self):
        test = count_keyword("韓粉")
        self.assertEqual(type(test), type((1,2)))





