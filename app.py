
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
cursor.execute('select username from client')
username_list = cursor.fetchall()

cursor.execute('select password from client')
password_list = cursor.fetchall()

cursor.execute('select id, username, password from client')
client_list_all = cursor.fetchall()






cursor.close()
conn.close()

print([x[0] for x in username_list].index('Rick'))

# the_index = username_list.index('Rick')


user_info=[]

def request_user_input():
    while True:
        try:
            username_input = input('enter your username: (this can not be empty)')
            
            password_input = input('enter your password: ')
        
            for x in username_list:
                if (x[0] == username_input):
                    print('this passed')
                    print(x, 'this is in pass')
                    for x in password_list:
                        if(x[0] == password_input):
                           the_index =[x[1] for x in client_list_all].index(username_input)
                           print('this is the index: ', the_index)
                           print(client_list_all[the_index], " retrieving this")
                           print(client_list_all[the_index][0], " this should be the id")
                            
                        print(x, ' this is valid')



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
    
   
for x in client_list_all:
    print(x)       
      

request_user_input()