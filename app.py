

import dbcreds
import mariadb


conn = mariadb.connect(
    user=dbcreds.user, 
    password=dbcreds.password,
    host=dbcreds.host, 
    port=dbcreds.port, 
    database=dbcreds.database)

cursor = conn.cursor()
# called the username and password seperately
# cursor.execute('select username from client')
# username_list = cursor.fetchall()

# cursor.execute('select password from client')
# password_list = cursor.fetchall()

cursor.execute('call client_list')
result = cursor.fetchall()



# client_list_all_decoded = client_list_all_encoded.decode("UTF-8")
# print(client_list_all_decoded)






cursor.close()
conn.close()

# print([x[0] for x in username_list].index('Rick'))

# the_index = username_list.index('Rick')


user_info=[]

def request_user_input():
    while True:
        try:
            username_input = input('enter your username: (this can not be empty)')
            
            password_input = input('enter your password: ')
            # x[] is the index inside of tuple, so this is checking the data going 
            # through the array of tuple at a specific index of the tuple
            # needed to use decode on strings if i called the sql with stored procedure, but didnt when i just wrote
            # manual code in the cursor.execute
            index_by_username =[x[1].decode("UTF-8") for x in result].index(username_input)
            index_by_password =[x[2].decode("UTF-8") for x in result].index(password_input)

            id_by_username = result[index_by_username][0]
            id_by_password = result[index_by_password][0]
            
            if (id_by_username == id_by_password):
                print(id_by_username, 'checking if id is valid, and it is')
                return id_by_username
            else:
                print('this failed or invalid user or pw')
                return None

            # this is just old code for me to trace my thinking
            # for x in username_list:
            #     if (x[0] == username_input):
            #         print('this passed')
            #         print(x, 'this is in pass')
            #         for x in password_list:
            #             if(x[0] == password_input):
            #                the_index =[x[1] for x in client_list_all].index(username_input)
            #                print('this is the index: ', the_index)
            #                print(client_list_all[the_index], " retrieving this")
            #                print(client_list_all[the_index][0], " this should be the id")
            #                the_id =client_list_all[the_index][0]
            #                return the_id
            #             else:
            #                 return None
                            
            #             print(x, ' this is valid')



                        # else:
                        #     print('wrong pw')
                # else:
                #     print(username_input)
                #     print(x, ' inside else')
                #     print('this failed')
            # if (len(username_input) < 1):
            #     print('try again, now this time your real username')
            # elif (len(password_input) < 1):
            #     print('try again with the password')
            # else:
            #     username_list = [user[0] for user in result]
            #     if username_input in username_list:
            #         print('true')
            #     else:
            #         print('the else')
        except:
            print('you have landed on error')

def adding_post(client_id):
    
    if (client_id != None):
        temp_db_storage = []
        user_title = input('enter a title: ')
        user_content = input('type your story here: ')
        temp_db_storage.append(client_id)
        temp_db_storage.append(user_title.encode("UTF-8"))
        temp_db_storage.append(user_content.encode("UTF-8"))
        print(temp_db_storage)

        conn = mariadb.connect(
        user=dbcreds.user, 
        password=dbcreds.password,
        host=dbcreds.host, 
        port=dbcreds.port, 
        database=dbcreds.database)

        cursor = conn.cursor()
        cursor.execute('CALL add_post(?, ?, ?)', [temp_db_storage[0], temp_db_storage[1], temp_db_storage[2]])
        
        cursor.close()
        conn.close()


def retrieve_all_post():
        
        conn = mariadb.connect(
        user=dbcreds.user, 
        password=dbcreds.password,
        host=dbcreds.host, 
        port=dbcreds.port, 
        database=dbcreds.database)

        cursor = conn.cursor()
        cursor.execute('CALL get_all_post()')
        result = cursor.fetchall()
        
        cursor.close()
        conn.close()
        for x in result:
            print("title: ", x[0].decode("UTF-8")," content: ", x[1])

def keep_logged_in():
    try:
        the_tries = request_user_input()
        if(the_tries != None):
            while True:
                user_answer = input('do you want to insert a new post?: y or n ')
                if(user_answer == 'y'):
                    adding_post(the_tries)
                else:
                    user_answer_2 = input('do you want to read all post?: y or n ')
                    if (user_answer_2 == 'y'):
                        retrieve_all_post()
                    else:
                        user_answer_3 = input('do you want to quit?: y or n ')
                        if (user_answer_3 == y):
                            print('good bye')
                            return
                        else:
                            request_user_input()
    except:
        print('did not work')        
    
keep_logged_in()
   
      




