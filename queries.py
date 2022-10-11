#add
sql1 = "INSERT INTO tbl_emp(emp_name, emp_email, emp_password) VALUES(%s, %s, %s)"

#/
sql2 = "SELECT * FROM tbl_emp"

#edit
sql3 = "SELECT * FROM tbl_emp WHERE emp_id=%s"

#update
sql4 = "UPDATE tbl_emp SET emp_name=%s, emp_email=%s, emp_password=%s WHERE emp_id=%s"

#delete
sql5 = "DELETE FROM tbl_emp WHERE emp_id=%s"
