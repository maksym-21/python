# Author -> Maksym Buniak

from prettytable import PrettyTable

import os
import datetime as dt
from sqlalchemy.engine import create_engine
from sqlalchemy.sql.expression import select
from sqlalchemy.sql.schema import Column, ForeignKey, MetaData, Table

from sqlalchemy.sql.sqltypes import DateTime, Integer, String

dict = {
        "students_in_class" : ['id','class_id','student_id'],
        "classes" : ['id','discipline','name','teacher_id'],
        "teachers" : ['id_teacher','id_person','name','last name','email','birth'],
        "students" : ['student_id','id_person','name','last name','email','birth'],
        "persons" : ['id','name','last name','email','birth']
    }

def show_main_menu() :
    print("\nPlease select a number from list of options :\n")
    print("1 - show my tables")
    print("2 - insert to table")
    print("3 - delete from table")
    print("4 - retrieve from table")
    print("5 - export table to file")
    print("6 - show main menu")
    print("7 - exit\n")

def ret_pretty_table(field_names, rows) :
    # init of pretty table
    t = PrettyTable()
    # setting an array of column names
    t.field_names = field_names
    # adding data(rows) to table
    t.add_rows(rows)
    return t

def show_tables() :
    p = select([persons])
    st = select([students.c.student_id,persons]).where(students.c.id == persons.c.id)
    t = select([teachers.c.teacher_id,persons]).where(persons.c.id == teachers.c.person_id)
    cl = select([classes])
    s_in_cl = select([students_in_class])

    p1 = conn.execute(p)
    st1 = conn.execute(st)
    t1 = conn.execute(t)
    cl1 = conn.execute(cl)
    ss1 = conn.execute(s_in_cl)

    print('\nTable "persons" : \n')
    print(ret_pretty_table(dict['persons'], p1.fetchall()))
    
    print('\nTable "students" : \n')
    print(ret_pretty_table(dict['students'], st1.fetchall()))

    print('\nTable "teachers" : \n')
    print(ret_pretty_table(dict['teachers'], t1.fetchall()))

    print('\nTable "classes" : \n')
    print(ret_pretty_table(dict['classes'], cl1.fetchall()))

    print('\nTable "students_in_class" : \n')
    print(ret_pretty_table(dict['students_in_class'], ss1.fetchall()))

    print()
    show_main_menu()

def insert_to_table() :
    print('\nTo which table you want insert a row(persons, students, teachers, classes, students_in_class)?\n')

    desired_table_name = input().lower().strip()

    if desired_table_name.lower().strip() == 'persons' :
        name = input('\nenter name: ')
        lastName = input('enter last name: ')
        email = input('enter email: ')
        date = input('enter birthdate(ex. 1.11.1999):\n')

        d = date.strip().split('.')

        for i in range(len(d)) : 
            if '0' in d[i] : d[i] = d[i][1]
        try :
            conn.execute(persons.insert(), {
                'name':name,
                'lastName':lastName,
                'email':email,
                'birth':dt.datetime(int(d[2]),int(d[1]),int(d[0])).date()
                }
            ) 
            print(f'\nSuccessful inserting to "persons" {{name:{name}, last_name:{lastName}, email:{email}, birth_date:{date}}}\n')
        except Exception as e : 
            print('\nSomething went wrong!\n')
            
            print(e)

            show_main_menu()
    elif desired_table_name.lower().strip() == 'students' :
        id = input('\nPlease give an ID of person : ')
        
        try :
            conn.execute(students.insert(), {
                'id':id
                }
            )
            print(f'\nSuccessful inserting to "students" {{person_id:{id}}}\n')
        except Exception as e : 
            print('\nSomething went wrong!\n')

            print(e)

            show_main_menu()
    elif desired_table_name.lower().strip() == 'teachers' :
        id = input('\nPlease give an ID of person : ')
        
        try :
            conn.execute(teachers.insert(), {
                'person_id':id
                }
            )
            print(f'\nSuccessful inserting to "teachers" {{person_id:{id} }}\n')
        except Exception as e : 
            print('\nSomething went wrong!\n')

            print(e)

            show_main_menu()
    elif desired_table_name.lower().strip() == 'classes' :
        discipline = input('\nenter a name of discipline : ')
        name = input('enter a name of class : ')
        id = input('enter a teacher_id : ')

        try :
            conn.execute(classes.insert(), {
                'discipline':discipline,
                'name':name,
                'teacher_id':id
                }
            )
            print(f'\nSuccessful inserting to "classes" {{discipline:{discipline}, name:{name} , teacher:{id}}}\n')
        except Exception as e : 
            print('\nSomething went wrong!\n')

            print(e)

            show_main_menu()
    elif desired_table_name.lower().strip() == 'students_in_class' :
        c_id = input('enter a class_id : ')
        s_id = input('enter a student_id : ')
        
        try :
            conn.execute(students_in_class.insert(),{
                'class_id':c_id,
                'student_id':s_id
                }
            )
        except Exception as e : 
            print('\nSomething went wrong!\n')
            
            print(e)

            show_main_menu()
    else :
        print('Bad input prompt!Try again\n')
    
    show_main_menu()

def delete_from_table() :
    name = input('In which table you want to delete a row(students,persons,teachers,classes,students_in_class) : ')

    id = input('\nPlease give me id :')
    if name.lower().strip() == 'persons' :
        try :
            d = persons.delete().where(persons.c.id == id)

            conn.execute(d)
        except Exception as e : print(e)
    elif name.lower().strip() == 'students' :
        try :
            d = students.delete().where(students.c.student_id == id)

            conn.execute(d)
        except Exception as e : print(e)    
    elif name.lower().strip() == 'teachers' : 
        try :
            d = teachers.delete().where(teachers.c.teacher_id == id)

            conn.execute(d)
        except Exception as e : print(e)   
    elif name.lower().strip() == 'classes' :
        try :
            d = classes.delete().where(classes.c.id == id)

            conn.execute(d)
        except Exception as e : print(e) 
    elif name.lower().strip() == 'students_in_class' : 
        try :
            d = students_in_class.delete().where(students_in_class.c.id == id)

            conn.execute(d)
        except Exception as e : print(e)
    else : 
        print('Bad input prompt!Try again\n')
    
    show_main_menu()

def retrieve_from_table() :
    name = input('From which table you want to retrieve information(students,persons,teachers,classes,students_in_class) : ')
    
    if name.lower().strip() == 'persons' :
        try :
            id = input('Give an id of person : ')

            s = persons.select().where(persons.c.id == id)

            print()
            ss = conn.execute(s)

            print(ret_pretty_table(dict['persons'], ss.fetchall()))
        except Exception as e : 
            print(e)
    elif name.lower().strip() == 'students' :
        try:
            id = input('Give an id of student : ')

            q = select([students.c.student_id,persons]).where(students.c.id == persons.c.id == id)

            print()
            qq = conn.execute(q)
            
            print(ret_pretty_table(['student_id','person_id','name','last_name','email','birth'], qq.fetchall()))
        except Exception as e : print(e)
    elif name.lower().strip() == 'teachers' :
        try:
            id = input('Give an id of teacher : ')

            q = select([teachers.c.teacher_id, persons]).where(persons.c.id == teachers.c.person_id == id)
            
            print()
            qq = conn.execute(q)
            
            print(ret_pretty_table(['teacher_id','id_person','name','last_name','email','birth'], qq.fetchall()))
        except Exception as e : print(e)
    elif name.lower().strip() == 'classes' :
        try :
            id = input('Give an id of class : ')

            w = select([classes]).where(classes.c.id == id)
            
            print()
            ww = conn.execute(w)

            print(ret_pretty_table(dict['classes'], ww.fetchall()))
        except Exception as e :
            print(e)
    elif name.lower().strip() == 'students_in_class' :
        try :
            id = input('Give an id of class : ')

            w = select([students_in_class]).where(students_in_class.c.class_id == id)
            
            print()
            ww = conn.execute(w)

            print(ret_pretty_table(['id','class_id','student_id'], ww.fetchall()))
        except Exception as e :
            print(e)
    else : 
        print('Bad input prompt!Try again\n')
    
    show_main_menu()

def export_table_to_file() :
    print('\nPlease choose a format of file : \n')
    print('1 - > .csv file')
    print('2 -> .txt file')
    print('3 -> .json file\n')

    prompt = int(input())

    print('\nPlease give a name of table which you want to export : \n')
    name = input()

    table = None
    if name == 'classes' : 
        table = classes
    elif name == 'students' :
        table = students 
    elif name == 'teachers' :
        table = teachers
    elif name == 'persons' :
        table = persons
    elif name == 'students_in_class' :
        table = students_in_class

    try : 
        queue = conn.execute(select([table]))

        # fetches all the rows of a query result
        fetched = queue.fetchall()
        if prompt == 1 : 
            import csv

            with open(f'table_{name}.csv','w',newline='') as file :
                writer = csv.writer(file)

                # firstly write column names
                writer.writerow(dict[name])
                
                # then writing rows
                writer.writerows(fetched)
            if os.path.exists(f'table_{name}.csv') :
                print("\nYour file is saved at : ", os.path.abspath(f'table_{name}.csv'))
        elif prompt == 2 : 
            with open(f'table_{name}.txt','w') as file :
                tb = PrettyTable()
                tb.field_names = dict[name]
                tb.add_rows(fetched)
                
                file.write(tb.get_string())
            if os.path.exists(f'table_{name}.txt') :
                print("\nYour file is saved at : ", os.path.abspath(f'table_{name}.txt'))
        elif prompt == 3 : 
            with open(f'table_{name}.json','w') as file :
                tb = PrettyTable()
                tb.field_names = dict[name]
                tb.add_rows(fetched)
                
                file.write(tb.get_json_string())
            if os.path.exists(f'table_{name}.txt') :
                print("\nYour file is saved at : ", os.path.abspath(f'table_{name}.json'))
        else : 
            print('\nBad input-intend, please try again\n')
        
        show_main_menu()
    except Exception as e :
        print('\nSomething went wrong (possible bad prompt-input), please try again')
        
        print(f'\n{e.__str__()}\n')
        show_main_menu()


if __name__ == '__main__' :
    # setting a path,connection path and name for our database
    BASE_DIRECTION = os.path.dirname(os.path.realpath(__file__))
    connection_string = 'sqlite:///' + os.path.join(BASE_DIRECTION, 'app.db')

    # new engine instance (
    # 1 param -> URL as the first positional argument, 
    #   usually a string that indicates database dialect
    # 2 param -> if True, the Engine will log all statements as well as a repr() 
    #   of their parameter lists to the engines logger, which defaults to sys.stdout
    # )
    engine = create_engine(connection_string, echo=True)    
    
    # MetaData is a container object that keeps together many 
    # different features of a database (or multiple databases) being described.
    meta = MetaData()

    # providing access to a Connection, which can then invoke SQL statements
    conn = engine.connect()

    persons = Table('persons', meta,
        Column('id', Integer(), primary_key=True),
        Column('name', String(25), nullable=False),
        Column('lastName', String(25), nullable=False),
        Column('email', String(40)),
        Column('birth', DateTime())
    )

    students = Table('students', meta,
        Column('student_id', Integer(), primary_key=True),
        Column('id', Integer(), ForeignKey('persons.id'))
    )

    teachers = Table('teachers', meta,
        Column('teacher_id', Integer(), primary_key=True),
        Column('person_id', Integer(), ForeignKey('persons.id'))
    )

    classes = Table('classes', meta,
        Column('id', Integer(), primary_key=True),
        Column('discipline', String(30), nullable=False),
        Column('name', String(25), nullable=False),
        Column('teacher_id', Integer(), ForeignKey('teachers.teacher_id'))
        # 1 class <=> 1 teacher
    )

    students_in_class = Table('students_in_class', meta,
        Column('id', Integer(), primary_key=True),
        Column('class_id', Integer(), ForeignKey('classes.id')),
        Column('student_id', Integer(), ForeignKey('students.student_id'))
        # 1 class <=> 0, 1 or many students
    )

    # creating all tables with it metadata (if they already exists then OK)
    meta.create_all(engine,checkfirst = True)

    print("\nWelcome to my database:)")
    show_main_menu()

    while True :        
        try :
            prompt = int(input())
        except :
            print('\nError! Bad input-intend, please try again')
        
        if prompt > 0 and prompt < 8 :
            if prompt == 1 :
                show_tables()
            elif prompt == 2 : 
                insert_to_table()
            elif prompt == 3 :
                delete_from_table() 
            elif prompt == 4 :
                retrieve_from_table()
            elif prompt == 5 :
                export_table_to_file()    
            elif prompt == 6 :
                show_main_menu()
            elif prompt == 7 : 
                conn.close()
                break
        else : print('\nBad input-intend, please try again\n')