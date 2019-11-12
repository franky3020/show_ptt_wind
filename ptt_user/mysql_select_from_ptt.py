from .db_operation import db_operation

def ptt_user_name(user_name:str, msg_like:str=None) -> str :
    db = db_operation()
    
    search_user_msg_sql=" \
    SELECT msg_2.msg, article.article_title, article.article_url,msg_2.msg_time,article.nrec \
    FROM test_user, msg_2, article \
    WHERE test_user.user_name = %s \
    AND msg_2.msg LIKE %s \
    AND msg_2.user_id_fk = test_user.id \
    AND article.id = msg_2.article_id_fk \
    ORDER BY msg_2.msg_time DESC \
    "
    
    if(msg_like != None):
        args = (user_name,"%"+msg_like+"%")
    else:
        args = (user_name,"%")
    
    db.execute(search_user_msg_sql, args)
    result = db.fetchall()
    
    db.colse()
    return result
    
def key_word_group_by_user():
    pass
    
    
    
    
    












