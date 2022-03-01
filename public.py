from flask import *
from database import *

public=Blueprint('public',__name__)

@public.route('/')
def home():
	return render_template('home.html')

@public.route('/login',methods=['get','post'])

def login():
	if 'submit' in request.form:
		username=request.form['username']
		password=request.form['password']
		print(username,password)

		q="select * from login where username='%s' and password='%s'"%(username,password)
		res=select(q)


		if res:
			session['lid']=res[0]['login_id']
			if res[0]['usertype']=='admin':
				flash("login successfully")
				return redirect(url_for('admin.admin_home'))

			if res[0]['usertype']=='institute':
				q="select * from institutes where login_id='%s'"%(session['lid'])
				a=select(q)
				if a:
					session['institute_id']=a[0]['institute_id']
					ins_id=session['institute_id']
					return redirect(url_for('institute.institute_home'))



	return render_template('login.html')

@public.route('/registration',methods=['get','post'])

def registration():
	if 'submit' in request.form:
		instname=request.form['institutename']
		instplace=request.form['place']
		instlandmark=request.form['landmark']
		instphone=request.form['phone']
		instemail=request.form['email']
		instlatitute=request.form['lati']
		instlongitute=request.form['long']
		instint=request.form['inter']
		instclass=request.form['class']
		instusername=request.form['username']
		instpassword=request.form['password']
		q="select * from login where username='%s' and password='%s'"%(instusername,instpassword)
		res=select(q)
		if res:
			flash("username and password already exists")
		else:
			p="insert into login values(null,'%s','%s','pending')"%(instusername,instpassword)
			id=insert(p)
			q="insert into institutes values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(id,instname,instplace,instlandmark,instphone,instemail,instlatitute,instlongitute,instint,instclass)
			insert(q)
			flash("registered successfully")
	
	return render_template('institute_registration.html')