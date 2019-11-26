from django.test import TestCase

# Create your tests here.
from .mysql_select_from_ptt import count_keyword
from .take_data_from_mysql.Msg_key_word import Msg_key_word
class sqlTestCase(TestCase):
    def setUp(self):
        pass

    # def test_sql_type(self):
    #     test = count_keyword("韓粉")
    #     self.assertEqual( type(test), int )
                       
    def test_keyWord_add_one(self):
        m_s = Msg_key_word()
        m_s.add_keyWord("YAYA")
     
        self.assertEqual("test_col LIKE " + "%s" , m_s.get_sql_str("test_col"))
        self.assertEqual( ("%YAYA%",) , m_s.get_sql_args())
        
        
        





