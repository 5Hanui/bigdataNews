import pymysql as sql


def selectLogin(email, pw):
    db_session = None
    row = None
    try:
        db_session = sql.connect(host='localhost',
                                 user='root',
                                 password='root',
                                 db='newsdb',
                                 charset='utf8',
                                 cursorclass=sql.cursors.DictCursor)
        print("디비접속성공")
        with db_session.cursor() as cursor:
            sql_str = "SELECT * FROM users WHERE email=%s AND pw=%s;"
            cursor.execute(sql_str, (email, pw))  # 튜플이 1개일 경우 ('m',
            row = cursor.fetchone()  # row는 회원정보
            
    except Exception as e:
        print(e)
    finally:
        if db_session:  # 비번틀렸을 때 db_session은 None이 되므로 확인하기
            db_session.close()
            print("디비접속해제성공")
    #쿼리결과인 회원정보리턴
    return row

#singup
def insertUser(username, email, pw):
    db_session = None
    rows = None
    try:
        db_session = sql.connect(host='localhost',
                                 user='root',
                                 password='root',
                                 db='newsdb',
                                 charset='utf8',
                                 cursorclass=sql.cursors.DictCursor)

        with db_session.cursor() as cursor:
            sql_str = '''
                INSERT INTO users
                (username, email, pw) 
                VALUES
                (%s, %s, %s);
                '''
            cursor.execute(sql_str, (
                username,
                email,
                pw
            ))
            db_session.commit()
    finally:
        if db_session:  # 비번틀렸을 때 db_session은 None이 되므로 확인하기
            db_session.close()
    return rows


# if __name__ == '__main__':
#     print(selectLogin('ww','12'))
