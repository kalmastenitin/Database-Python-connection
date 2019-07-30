import psycopg2
import sys

def connect():
    '''creating connection to the databse'''
    conn=None
    try:
        conn = psycopg2.connect(host='localhost',user='postgres',
                                password='admin', database='employee_db')
        print('Connected to employee_db successfully!\n')
    except Exception as e:
        print(str(e))
    return conn

def create_table():
    conn = connect()
    cur = conn.cursor()
    cur.execute('''CREATE TABLE employee_data
                    (pk serial PRIMARY KEY,
                    emp_name TEXT NOT NULL,
                    emp_email VARCHAR(320),
                    emp_age INT NOT NULL,
                    emp_salary INT NOT NULL);''')
    conn.commit()
    print('Table employee_data created successfully!')
    conn.close()

def insert_data():
    conn = connect()
    cur = conn.cursor()
    last_insert_id = None
    ''' Inserting data into employee_data table'''
    sql_query = "insert into employee_data (emp_name, emp_email, emp_age, emp_salary) values (%s, %s, %s, %s) returning pk;"

    print('Enter data to be inserted!\n')
    e_name = str(input('Employee Name: ')),
    e_email = str(input('Employee Email id: ')),
    e_age = int(input('Employee Age: ')),
    e_salary = int(input('Employee Salary: '))

    sql_data = (
        e_name,
        e_email,
        e_age,
        e_salary
        )

    cur.execute(sql_query, sql_data)
    last_insert_id = cur.fetchone()[0]
    print("Last Insert ID " + str(last_insert_id))
    conn.commit()
    cur.close()
    conn.close()
    return last_insert_id

def fetch_all_data():
    conn = connect()
    cur = conn.cursor()
    sql_query = "select * from employee_data"
    cur.execute(sql_query)
    results = cur.fetchall()
    print('Employee Data')
    return (results)

def fetch_data():
    conn = connect()
    cur = conn.cursor()
    selection = int(input('Search by\n 1 - name \n 2 - email \n 3 - age \n 4 - salary \n >'))
    if selection==1:
        sql_query = "SELECT emp_email, emp_age, emp_salary from employee_data where emp_name = %s;"
        search_term = input('Search by Employee Name: ')
        sql_data = (search_term,) #tuple is compulsory
        cur.execute(sql_query, sql_data)
        result = cur.fetchall()
        return result
    elif selection==2:
        sql_query = "SELECT emp_name, emp_age, emp_salary from employee_data where emp_email = %s;"
        search_term = str(input('Search by Employee Email: '))
        sql_data = (search_term,) #tuple is compulsory
        cur.execute(sql_query, sql_data)
        result = cur.fetchall()
        print(result)
        return result
    elif selection==3:
        sql_query = "SELECT emp_name, emp_email, emp_salary from employee_data where emp_age = %s;"
        search_term = input('Search by Employee age: ')
        sql_data = (search_term,) #tuple is compulsory
        cur.execute(sql_query, sql_data)
        result = cur.fetchall()
        return result
    elif selection==4:
        sql_query = "SELECT emp_name, emp_email, emp_age from employee_data where emp_salary = %s;"
        search_term = input('Search by Employee Salary: ')
        sql_data = (search_term,) #tuple is compulsory
        cur.execute(sql_query, sql_data)
        result = cur.fetchall()
        return result
    else:
        print('Enter correct choice!')

def update():
    conn = connect()
    cursor = conn.cursor()

    selection = int(input('Update\n 1 - name \n 2 - email \n 3 - age \n 4 - salary \n >'))
    if selection==1:
        sql_query = "update employee_data set emp_name = %s where emp_email=%s;"
        update_term = input('Enter New Name: ')
        search_term = input('Employee Email: ')
        sql_data = (update_term,search_term)
        cursor.execute(sql_query, sql_data)
    elif selection==2:
        sql_query = "update employee_data set emp_email = %s where emp_name=%s;"
        update_term = input('Enter New Email: ')
        search_term = input('Employee Name: ')
        sql_data = (update_term,search_term)
        cursor.execute(sql_query, sql_data)
    elif selection==3:
        sql_query = "update employee_data set emp_age = %s where emp_email=%s;"
        update_term = input('Enter New age: ')
        search_term = input('Employee Email: ')
        sql_data = (update_term,search_term)
        cursor.execute(sql_query, sql_data)
    elif selection==4:
        sql_query = "update employee_data set emp_salary = %s where emp_email=%s;"
        update_term = input('Enter New Salary: ')
        search_term = input('Employee Email: ')
        sql_data = (update_term,search_term)
        cursor.execute(sql_query, sql_data)
    else:
        print('Enter correct choice!')
    conn.commit()
    cursor.close()
    conn.close()
    return True

if __name__=='__main__':
    exit = 0
    while exit!=1:
        print('Please select your choice: \n')
        print(''' 1. Insert new data\n 2. Fetch data\n 3. Sort and fetch\n 4. Update data\n 5. Exit ''')
        try:
            choice = int(input())
            if choice==1:
                insert_data()
            elif choice==2:
                all_data = fetch_all_data()
                for data in all_data:
                    print(data)
            elif choice==3:
                all_data = fetch_data()
                for data in all_data:
                    print(data)
            elif choice==4:
                update()
                print('Data Updated!')
            else:
                exit = 1
        except:
            print('Please Enter Correct Choice!')
