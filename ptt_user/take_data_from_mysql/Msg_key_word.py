class Msg_key_word:
    def __init__(self):
        self.key_word = []
    
    def add_keyWord(self, msg:str):
         self.key_word.append(msg)
    
    def get_sql_str(self, table_col):
        output_str = ""

        is_first = True
        for i in range( len(self.key_word) ):
            if(is_first):
                is_first = False
                output_str = table_col + " LIKE " + "%s" 
            else:
                output_str = output_str + " AND " + table_col + " LIKE " + "%s" 
        
        return output_str

    def get_sql_args(self)->list:
        key_word_list = self.key_word.copy()
        for i in range(len(key_word_list)):
            key_word_list[i] = "%" + key_word_list[i] + "%"
            
        return key_word_list
