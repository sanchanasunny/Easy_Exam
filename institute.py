from flask import *
from database import *

import smtplib
from email.mime.text import MIMEText
from flask_mail import Mail
institute=Blueprint('institute',__name__)

@institute.route('/institute_home')

def institute_home():
	return render_template('institute_home.html')


@institute.route('/institute_add_staff',methods=['get','post'])
def institute_add_staff():
	institute_id=session['institute_id']
	if 'submit' in request.form:
		firstname=request.form['stafffirstname']
		lastname=request.form['stafflastname']
		phone=request.form['phone']
		email=request.form['email']
		staffusername=request.form['username']
		staffpassword=request.form['password']

		p="insert into login values(null,'%s','%s','staff')"%(staffusername,staffpassword)
		id=insert(p)

		q="insert into staff values(null,'%s','%s','%s','%s','%s','%s')"%(institute_id,id,firstname,lastname,phone,email)
		insert(q)
		try:
			gmail = smtplib.SMTP('smtp.gmail.com', 587)
			gmail.ehlo()
			gmail.starttls()
			gmail.login('projectsriss2020@gmail.com','messageforall')
		except Exception as e:
			print("Couldn't setup email!!"+str(e))
		msg = MIMEText("Your Username and Password is " +staffusername + " and " +staffpassword +" respectively")
		msg['Subject'] = 'Send Staff Cerdinalities'
		msg['To'] = email
		msg['From'] = 'projectsriss2020@gmail.com'
		try:
			gmail.send_message(msg)
			print(msg)
			print(email)
			flash('ASSIGNED SUCCESS..')
		except Exception as e:
			print("COULDN'T SEND EMAIL", str(e))
			flash("Something Went Wrong...")
		return redirect(url_for('institute.institute_add_staff'))

	return render_template('institute_add_staff.html')


@institute.route('/institute_view_staff',methods=['get','post'])
def institute_view_staff():

	data={}
	institute_id=session['institute_id']
	q="select * from staff where institute_id='%s'"%(institute_id)
	res=select(q)
	data['staff']=res

	if 'action' in request.args:
		action=request.args['action']
		staffid=request.args['staffid']
	else:
		action=	None

	if action=="delete":
		q="delete from staff where staff_id='%s'"%(staffid)
		delete(q)
		return redirect(url_for('institute.institute_view_staff'))

	if action=="update":
		q="select * from staff where staff_id='%s' "%(staffid)
		res=select(q)
		data['upstaff']=res

		if 'submit' in request.form:
			phone=request.form['phone']
			email=request.form['email']
		
			q="update staff set phone='%s',email='%s' where staff_id='%s'"%(phone,email,staffid)
			update(q)
			return redirect(url_for('institute.institute_view_staff'))
	
	return render_template('institute_view_staff.html',data=data)



@institute.route('/institute_view_examschedule',methods=['get','post'])
def institute_view_examschedule():
	data={}
	ins_id=session['institute_id']
	q="SELECT * FROM candidates INNER JOIN applications USING (candidate_id) INNER JOIN exam_master USING (exam_id) INNER JOIN assign USING(application_id) where institute_id='%s' "%(ins_id)
	print(q)
	res=select(q)
	data['ische']=res
	return render_template('institute_view_examschedule.html',data=data)


@institute.route('/institute_add_block',methods=['get','post'])
def institute_add_block():
	institute_id=session['institute_id']
	if 'submit' in request.form:
		blockname=request.form['blockname']

		q="insert into block values(null,'%s','%s')"%(institute_id,blockname)
		insert(q)
		return redirect(url_for('institute.institute_add_block'))

	return render_template('institute_add_block.html')


@institute.route('/institute_view_block',methods=['get','post'])
def institute_view_block():

	data={}
	ins_id=session['institute_id']
	q="SELECT * FROM block INNER JOIN institutes USING(institute_id)  where institute_id='%s'" %(ins_id)
	
	res=select(q)
	data['block']=res

	if 'action' in request.args:
		action=request.args['action']
		blockid=request.args['blockid']
	else:
		action=	None

	if action=="delete":
		q="delete from block where block_id='%s'"%(blockid)
		delete(q)
		return redirect(url_for('institute.institute_view_block'))

	if action=="update":
		q="select * from block where block_id='%s' "%(blockid)
		
		res=select(q)
		data['upblock']=res

		if 'submit' in request.form:
			blockname=request.form['blockname']
			
		
			q="update block set block_name='%s' where block_id='%s'"%(blockname,blockid)
			update(q)
			return redirect(url_for('institute.institute_view_block'))
	
	return render_template('institute_view_block.html',data=data)


@institute.route('/institute_add_classroom',methods=['get','post'])
def institute_add_classroom():
	data={}
	institute_id=session['institute_id']
	if 'submit' in request.form:
		blockename=request.form['blockename']
		classname=request.form['classname']
		strength=request.form['strength']

		q="insert into classroom values(null,'%s','%s','%s')"%(blockename,classname,strength)
		insert(q)
		return redirect(url_for('institute.institute_add_classroom'))
	q="select * from block where institute_id='%s'" %(institute_id)
	res=select(q)
	data['block']=res

	return render_template('institute_add_classroom.html',data=data)



@institute.route('/institute_view_classroom',methods=['get','post'])
def institute_view_classroom():

	data={}
	ins_id=session['institute_id']
	q="SELECT * FROM classroom	INNER JOIN block USING(block_id) INNER JOIN institutes USING(institute_id) where institute_id='%s'" %(ins_id)
	res=select(q)
	data['class']=res

	if 'action' in request.args:
		action=request.args['action']
		classroomid=request.args['classroomid']
	else:
		action=	None

	if action=="delete":
		q="delete from classroom where classroom_id='%s'"%(classroomid)
		delete(q)
		return redirect(url_for('institute.institute_view_classroom'))

	if action=="update":
		q="select * from classroom where classroom_id='%s' "%(classroomid)
		res=select(q)
		data['upclass']=res

		if 'submit' in request.form:
			classroomname=request.form['classroomname']
			strength=request.form['strength']
			
		
			q="update classroom set class_name='%s',strength='%s' where classroom_id='%s'"%(classroomname,strength,classroomid)
			update(q)
			return redirect(url_for('institute.institute_view_classroom'))
	
	return render_template('institute_view_classroom.html',data=data)

@institute.route('/institute_set_seat',methods=['get','post'])
def institute_set_seat():

	data={}
	institute_id=session['institute_id']
	id=request.args['id']
	hid=request.args['hid']

	qq="select * from seats where application_id='%s'" %(hid)
	resqq=select(qq)
	if resqq:
		data['valsss']=resqq

	qr="select *  from classroom inner join block using(block_id)  where institute_id='%s' " %(institute_id)
	res=select(qr)
	data['class']=res

	if 'submit' in request.form:
	
		hid=request.args['hid']
		classroom=request.form['classroom']

		q="select * from applications where application_id='%s'" %(hid)
		print(q)
		res1=select(q)
		print(res1)
		if res1:
			eid=res1[0]['exam_id']
			q="SELECT *  FROM seats  where classroom_id='%s' order by seat_no desc" %(classroom)
			print(q)
			res2=select(q)
			print(res2)
			if res2:
				if res2[0]['seat_no']!=None:
					sn=res2[0]['seat_no']
					snn=sn+1
					if int(snn)>int(res[0]['strength']):
						return redirect(url_for('institute.institute_view_examschedule'))
				else:
					snn=1
			else:
				snn=1
			p="insert into seats values(null,'%s','%s','%s')" %(hid,classroom,snn)
			print(p)
			insert(p)
			return redirect(url_for('institute.institute_view_examschedule'))


		

	
	q="SELECT * FROM candidates INNER JOIN applications USING (candidate_id) INNER JOIN exam_master USING (exam_id) where application_id='%s'" %(hid)
	res=select(q)
	data['seat']=res

	qs="select * from block where institute_id='%s' " %(institute_id)
	res=select(qs)
	data['block']=res	

	

	return render_template('institute_set_seat.html',data=data)
