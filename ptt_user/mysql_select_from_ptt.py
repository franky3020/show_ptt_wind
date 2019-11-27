from .db_operation import db_operation

def ptt_user_name(user_name:str) -> str :
    db = db_operation()
    
    search_user_msg_sql=" \
    SELECT msg_2.msg, article.article_title, article.article_url,msg_2.msg_time,article.nrec \
    FROM test_user, msg_2, article \
    WHERE test_user.user_name = %s \
    AND msg_2.user_id_fk = test_user.id \
    AND article.id = msg_2.article_id_fk \
    ORDER BY msg_2.msg_time DESC \
    LIMIT 100 \
    "
    args = (user_name)
    
    db.execute(search_user_msg_sql, args)
    result = db.fetchall()
    
    db.colse()
    return result
    
def ptt_user_name_and_msg(user_name:str, msg_like:str) -> str :
    msg_list = msg_like.split()
    if len(msg_list) == 0:# 檢查是否為空
        return  ptt_user_name(user_name)
    
    msg_key_word=Msg_key_word()
    for msg in msg_list:
        msg_key_word.add_keyWord(msg)
        
    search_user_msg_sql=" \
    SELECT msg_2.msg, article.article_title, article.article_url,msg_2.msg_time,article.nrec \
    FROM test_user, msg_2, article \
    WHERE test_user.user_name = %s \
    AND " + msg_key_word.get_sql_str("msg_2.msg") + " \
    AND msg_2.user_id_fk = test_user.id \
    AND article.id = msg_2.article_id_fk \
    ORDER BY msg_2.msg_time DESC \
    LIMIT 100 \
    "
    args = []
    args.append(user_name)
    args.extend( msg_key_word.get_sql_args() )
    
    db = db_operation()
    db.execute(search_user_msg_sql,tuple( args ) )
    result = db.fetchall()
    
    db.colse()
    return result
    
from .take_data_from_mysql.Msg_key_word import Msg_key_word
def ptt_msg_search(msg_like:str) -> str :
    msg_list = msg_like.split()
    if len(msg_list) == 0:# 檢查是否為空
        return  list([])
    
    msg_key_word=Msg_key_word()
    for msg in msg_list:
        msg_key_word.add_keyWord(msg)
    
    print(msg_key_word.get_sql_str("msg_2.msg"))
    search_user_msg_sql=" \
    SELECT test_user.user_name, msg_2.msg, article.nrec, article.article_title, article.article_url,msg_2.msg_time \
    FROM test_user, msg_2, article \
    WHERE " + msg_key_word.get_sql_str("msg_2.msg") + " \
    AND msg_2.user_id_fk = test_user.id \
    AND article.id = msg_2.article_id_fk \
    ORDER BY msg_2.msg_time DESC \
    LIMIT 100" \
    
    args = msg_key_word.get_sql_args()
    
    db = db_operation()
    db.execute(search_user_msg_sql, tuple(args) )
    result = db.fetchall()
    
    db.colse()
    return result

# msg_over_count 講 超過幾次
from .take_data_from_mysql.Sql_date_format import Sql_date_format
def count_keyword(msg_like:str, start_date:str, end_date:str, msg_over_count:str) -> int :
    msg_list = msg_like.split()
    if len(msg_list) == 0:# 檢查是否為空
        return 0
    
    msg_key_word=Msg_key_word()
    for msg in msg_list:
        msg_key_word.add_keyWord(msg)
    
    sql_date_format = Sql_date_format(start_date, end_date)

    count_keyword_sql = " \
        SELECT COUNT(*) FROM( \
        SELECT COUNT(test_user.user_name) FROM msg_2,test_user \
        WHERE " + msg_key_word.get_sql_str("msg_2.msg") + " \
        AND msg_2.user_id_fk = test_user.id \
        AND " + sql_date_format.get_sql_str("msg_2.msg_time") + " \
        GROUP BY test_user.user_name \
        HAVING COUNT(test_user.user_name) >= %s \
        )d1 \
        "
        
    args = []
    args.extend( msg_key_word.get_sql_args() )
    args.extend( sql_date_format.get_sql_args() )
    args.extend( [msg_over_count] )
 
    db = db_operation()
    db.execute(count_keyword_sql, tuple(args) )
    result = db.fetchall()
    
    db.colse()
    return result[0][0]

def count_eachUser_keyword(msg_like:str, start_date:str, end_date:str, msg_over_count:str) -> list :
    msg_list = msg_like.split()
    if len(msg_list) == 0:# 檢查是否為空
        return 0
    
    msg_key_word=Msg_key_word()
    for msg in msg_list:
        msg_key_word.add_keyWord(msg)
    
    sql_date_format = Sql_date_format(start_date, end_date)

    count_keyword_sql = " \
        SELECT test_user.user_name,COUNT(*) FROM msg_2,test_user \
        WHERE " + msg_key_word.get_sql_str("msg_2.msg") + " \
        AND msg_2.user_id_fk = test_user.id \
        AND " + sql_date_format.get_sql_str("msg_2.msg_time") + " \
        GROUP BY test_user.user_name \
        HAVING COUNT(test_user.user_name) >= %s "
        
        
    args = []
    args.extend( msg_key_word.get_sql_args() )
    args.extend( sql_date_format.get_sql_args() )
    args.extend( [msg_over_count] )
 
    db = db_operation()
    db.execute(count_keyword_sql, tuple(args) )
    result = db.fetchall()
    
    db.colse()
    return result





    
    
    
    
    












