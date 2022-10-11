#instance for both flask(app.py) and mysql(db)
#perform crud operations
import pymysql
from app import app
from tables import Results
from db_config import mysql
from flask import flash,render_template, request ,redirect
from werkzeug.security import generate_password_hash, check_password_hash
from queries import sql1, sql2, sql3, sql4,sql5

    


@app.route('/new_emp')
def add_emp_view():
    return render_template('add.html')

#adding emp
@app.route('/add', methods=['POST'])
def add_emp():
    conn = None
    cursor = None
    try: 
        _name = request.form['inputName']
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']
    # validate the received values
        if _name and _email and _password and request.method == 'POST':
            #do not save password as a plain text
            
            _hashed_password = generate_password_hash(_password)
            print(_hashed_password)
            # save edits
            data = (_name, _email, _hashed_password)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql1, data)
            conn.commit()
            flash('empolyee added successfully!')
            return redirect('/')
        else:
            return 'Error while adding user'
    #1
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()

@app.route('/')
def emps():
    conn = None
    cursor = None
    try:
        
        conn = mysql.connect()
        #1
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        #sql2
        cursor.execute(sql2)
        rows = cursor.fetchall()
        table = Results(rows)
        table.border = True
        return render_template('emps.html', table=table)
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()

#getting 
@app.route('/edit/<int:id>')
def edit_view(id):
    conn = None
    cursor = None
    try:
        # conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        #sql3
        cursor.execute(sql3, id)
        row = cursor.fetchone()
        if row:
            #row
            return render_template('edit.html', row=row)
        else:
            #id
            return 'Error loading #{id}'.format(id=id)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

#updating
@app.route('/update', methods=['POST'])
def update_emp():
    conn = None
    cursor = None
    try: 
        _name = request.form['inputName']
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']
        _id = request.form['id']
        # validate the received values
        if _name and _email and _password and _id and request.method == 'POST':
            #do not save password as a plain text
            _hashed_password = generate_password_hash(_password)
            print(_hashed_password)
            # save edits
            data = (_name, _email, _hashed_password, _id,)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql4, data)
            conn.commit()
            flash('Employee data updated successfully!')
            return redirect('/')
        else:
            return 'Error while updating empolyee details'
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()

#deleting
@app.route('/delete/<int:id>')
def delete_emp(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql5, (id,))
        conn.commit()
        flash('empolyee deleted successfully!')
        return redirect('/')
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()


if __name__ == "__main__":
    app.run()