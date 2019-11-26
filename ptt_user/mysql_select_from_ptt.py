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
    db = db_operation()
    
    search_user_msg_sql=" \
    SELECT msg_2.msg, article.article_title, article.article_url,msg_2.msg_time,article.nrec \
    FROM test_user, msg_2, article \
    WHERE test_user.user_name = %s \
    AND msg_2.msg LIKE %s \
    AND msg_2.user_id_fk = test_user.id \
    AND article.id = msg_2.article_id_fk \
    ORDER BY msg_2.msg_time DESC \
    LIMIT 100 \
    "
    
    args = (user_name, "%"+msg_like+"%")
 
    db.execute(search_user_msg_sql, args)
    result = db.fetchall()
    
    db.colse()
    return result
    
from .take_data_from_mysql.Msg_key_word import Msg_key_word
def ptt_msg_search(msg_like:str) -> str :
    msg_list = msg_like.split()
    msg_key_word=Msg_key_word()
    for msg in msg_list:
        msg_key_word.add_keyWord(msg)
    
    print(msg_key_word.get_sql_str("msg_2.msg"))
    search_user_msg_sql=" \
    SELECT test_user.user_name, msg_2.msg, article.nrec, article.article_title, article.article_url,msg_2.msg_time \
    FROM test_user, msg_2, article \
    WHERE " + msg_key_word.get_sql_str("msg_2.msg") + "\
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

def count_keyword(msg_like:str) -> int :

    db = db_operation()

    count_keyword_sql = " \
        SELECT COUNT(*) FROM( \
        SELECT COUNT(test_user.user_name) FROM msg_2,test_user \
        WHERE msg_2.msg LIKE %s \
        AND msg_2.user_id_fk = test_user.id \
        AND msg_2.msg_time > %s \
        AND msg_2.msg_time < %s \
        GROUP BY test_user.user_name \
        HAVING COUNT(test_user.user_name) >= %s \
        )d1 \
        "
        
    args = ("%"+msg_like+"%", "2019/10/1 00:00:00", "2019/11/1 00:00:00","1")
 
    db.execute(count_keyword_sql, args)
    result = db.fetchall()
    
    db.colse()
    return result[0][0]





    
    
    
    
    












