from django.test import TestCase

# Create your tests here.
from .mysql_select_from_ptt import count_keyword
from .take_data_from_mysql.Msg_key_word import Msg_key_word
from .take_data_from_mysql.Sql_date_format import Sql_date_format
import os 
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
        self.assertEqual( ["%YAYA%"] , m_s.get_sql_args())
    
    def test_date(self):
        date = Sql_date_format("2019/10/1 00:00:00", "2019/11/1 00:00:00")
        self.assertEqual(" " + "test_col" + " >= %s" + " AND " + "test_col" + " <= %s" + " " , date.get_sql_str("test_col"))
        self.assertEqual( ["2019/10/1 00:00:00", "2019/11/1 00:00:00"] , date.get_sql_args())
       
       





