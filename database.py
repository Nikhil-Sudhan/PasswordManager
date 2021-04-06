
import psycopg2

def store_password(password,user_email,username,url,app_name):
  
  connection = psycopg2.connect(dbname='postgres',user='postgres',password='3000')
  cursor=connection.cursor() 

  query="INSERT INTO database (password,user_email,username,url,app_name) VALUES (%s,%s,%s,%s,%s)"
  record=(password,user_email,username,url,app_name)

  cursor.execute(query,record)
    
  if cursor.rowcount > 0:
    print("Insertion Success!")
  connection.commit()
  connection.close() 
  cursor.close() 

def find_password(app_name):

  connection = psycopg2.connect(dbname='postgres',user='postgres',password='3000')
  cursor=connection.cursor()
  query="SELECT password FROM database WHERE app_name= '"+ app_name +"'"
  cursor.execute(query,app_name)
  result=cursor.fetchone()
  print('Passowrd is:' )
  print(result[0])
      
  connection.commit()
  connection.close() 
  cursor.close() 


 
def find_user(user_email):
  connection = psycopg2.connect(dbname='postgres',user='postgres',password='3000')
  cursor=connection.cursor()
  query="SELECT * FROM database WHERE user_email= '" +user_email+ "'"
  cursor.execute(query,user_email)
  result=cursor.fetchall()
  print('Account details:')
  print('Password\t user_email \t username \t url \t app_name')
  print(result)
  connection.commit()
  connection.close() 
  cursor.close() 

def delete(app_name):
  connection = psycopg2.connect(dbname='postgres',user='postgres',password='3000')
  cursor=connection.cursor()
  cursor.execute("DELETE FROM database WHERE app_name = %s",(app_name,))
  connection.commit()
  connection.close() 
  cursor.close()

