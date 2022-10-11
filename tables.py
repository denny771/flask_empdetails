from flask_table import Table, Col, LinkCol

class Results(Table):
    emp_id = Col('Id', show=False)
    emp_name = Col('Name')
    emp_email = Col('Email')
    emp_password = Col('Password', show=False)
    edit = LinkCol('Edit', 'edit_view', url_kwargs=dict(id='emp_id'))
    delete = LinkCol('Delete', 'delete_emp', url_kwargs=dict(id='emp_id'))