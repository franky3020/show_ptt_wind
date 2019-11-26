class Msg_key_word:
    def __init__(self):
        self.key_word = []
    
    def add_keyWord(self, msg:str):
         self.key_word.append(msg)
    
    def get_sql_str(self):
        output_str = ""

        is_first = True
        for i in range( len(self.key_word) ):
            if(is_first):
                output_str = "LIKE " + "%" + "%s" + "%"
            else:
                output_str = output_str + "AND LIKE " + "%" + "%s" + "%"
        
        return output_str

    def get_sel_args(self):
        return self.key_word
