class Sql_date_format:
    def __init__(self, start_date:str, end_date:str):
        self.start_date = start_date
        self.end_date = end_date
    
    def get_sql_str(self, table_col):
        output_str = " " + table_col + " >= %s" + " AND " + table_col + " <= %s" + " " 
        return output_str

    def get_sql_args(self)->list:
        key_word_list = [self.start_date, self.end_date]
        return key_word_list