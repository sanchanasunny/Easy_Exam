from flask import *
from database import *
import os
import cv2
import uuid
import qrcode
from core import *

import smtplib
from email.mime.text import MIMEText
from flask_mail import Mail

admin=Blueprint('admin',__name__)

@admin.route('/admin_home')
def admin_home():
	return render_template('admin_home.html')

@admin.route('/admin_manage_exam',methods=['get','post'])
def admin_manage_exam():
	
	if 'submit' in request.form:
		title=request.form['title']
		examdate=request.form['examdate']
		examtime=request.form['examtime']
		examduration=request.form['examduration']
		examdescription=request.form['examdescription']
		exammode=request.form['exammode']
		noofpost=request.form['noofpost']

		q="insert into exam_master values(null,'%s','%s','%s','%s','%s','%s','%s','Opened')"%(title,examdate,examtime,examduration,examdescription,noofpost,exammode)
		insert(q)
		return redirect(url_for('admin.admin_manage_exam'))

	return render_template('admin_manage_exam.html')

@admin.route('/admin_view_exam',methods=['get','post'])
def admin_view_exam():

	data={}
	q="select * from exam_master"
	res=select(q)
	data['exam']=res

	if 'action' in request.args:
		action=request.args['action']
		examid=request.args['examid']
	else:
		action=	None

	if action=="delete":
		q="delete from exam_master where exam_id='%s'"%(examid)
		delete(q)
		flash("deleted successfully")
		return redirect(url_for('admin.admin_view_exam'))
	if action=="closing":
		q="update exam_master set exam_status='Closed' where exam_id='%s'"%(examid)
		update(q)
		return redirect(url_for('admin.admin_view_exam'))

	if action=="update":
		q="select * from exam_master where exam_id='%s' "%(examid)
		res=select(q)
		data['upexam']=res

		# ///////////////////////////////// trainnn     //////////////////////////
	if action=="generateqr":
		# q="update exam_master set exam_status='application closed' WHERE `exam_id`='%s'"%(eid)
		# delete(q)
		# return redirect(url_for("pscadmin.pscadmin_manage_exam_noti"))
		q="select * from candidates where candidate_id in(select candidate_id from applications where exam_id='%s')" %(examid)
		res1=select(q)
		print(res1)
		pid=str(examid)
		isFile = os.path.isdir("static/trainimages/"+pid)  
		print(isFile)
		if(isFile==False):
			os.mkdir('static\\trainimages\\'+str(pid))
		for row in res1:
			print("haii")
			isFile = os.path.isdir("static/trainimages/"+str(pid)+"/"+str(row['candidate_id']))  
			print(isFile)
			if(isFile==False):
				os.mkdir('static\\trainimages\\'+str(pid)+'\\'+str(row['candidate_id']))
			imag = cv2.imread(row['photo'])
			FileName = "static/trainimages/"+str(pid)+"/"+str(row['candidate_id'])+"/"+str(uuid.uuid4())+".jpg" #Saving the current image from the webcam for testing.
			cv2.imwrite(FileName, imag)
			FileName = "static/trainimages/"+str(pid)+"/"+str(row['candidate_id'])+"/"+str(uuid.uuid4())+".jpg" #Saving the current image from the webcam for testing.
			cv2.imwrite(FileName, imag)
			FileName = "static/trainimages/"+str(pid)+"/"+str(row['candidate_id'])+"/"+str(uuid.uuid4())+".jpg" #Saving the current image from the webcam for testing.
			cv2.imwrite(FileName, imag)
			# qqq="select * from applications where candidate_id='%s' and exam_id='%s'" %(row['candidate_id'],pid)
			# resss=select(qqq)
			# print()
			# if resss:
			# 	path = "static/qrcode/" + str(uuid.uuid4()) + ".png"
				
			# 	img = qrcode.make(str(resss[0]['application_id']))
			# 	img.save(path)
			# 	qw="update applications set qrimage='%s' where application_id='%s'" %(path,resss[0]['application_id'])
			# 	update(qw)



		q="update exam_master set exam_status='Hall Tickets Generated' where exam_id='%s' " %(pid)
		update(q)
		s=enf("static/trainimages/"+str(pid)+"/",pid)
		# ///////////////////////////////////
		return redirect(url_for('admin.admin_view_exam'))



	if 'submit' in request.form:
		examdate=request.form['examdate']
		examtime=request.form['examtime']
		
		q="update exam_master set exam_date='%s',exam_time='%s' where exam_id='%s'"%(examdate,examtime,examid)
		update(q)
		flash("updated successfully")
		return redirect(url_for('admin.admin_view_exam'))


	return render_template('admin_view_exam.html',data=data)



@admin.route('/admin_view_institute',methods=['get','post'])
def admin_view_institute():

	data={}
	q="select * from institutes"
	res=select(q)
	data['inst']=res

	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=	None
	if action=="accept":
		q="update login set usertype='institute' where login_id='%s'"%(id) 
		update(q)
		q="select * from institutes where login_id='%s'"%(id)
		res=select(q)
		email=res[0]['email']

		try:
			gmail = smtplib.SMTP('smtp.gmail.com', 587)
			gmail.ehlo()
			gmail.starttls()
			gmail.login('projectsriss2020@gmail.com','messageforall')
		except Exception as e:
			print("Couldn't setup email!!"+str(e))
		msg = MIMEText("Your Request is Accepted")
		msg['Subject'] = 'Registration Request'
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


	if action=="reject":
		z="update login set usertype='rejected' where login_id='%s'"%(id)
		update(z)
		q="select * from institutes where login_id='%s'"%(id)
		res=select(q)
		email=res[0]['email']

		try:
			gmail = smtplib.SMTP('smtp.gmail.com', 587)
			gmail.ehlo()
			gmail.starttls()
			gmail.login('projectsriss2020@gmail.com','messageforall')
		except Exception as e:
			print("Couldn't setup email!!"+str(e))
		msg = MIMEText("Your Request is rejected")
		msg['Subject'] = 'Registration Request'
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

	return render_template('admin_view_institute.html',data=data)


@admin.route('/admin_view_staff',methods=['get','post'])
def admin_view_staff():

	data={}
	q="select * from staff"
	res=select(q)
	data['staff']=res
	return render_template('admin_view_staff.html',data=data)


@admin.route('/admin_view_candidate',methods=['get','post'])
def admin_view_candidate():
	data={}
	q="select * from candidates"
	res=select(q)
	data['cand']=res
	z="select * from institutes"
	res1=select(z)
	data['inst']=res1
	return render_template('admin_view_candidate.html',data=data)


@admin.route('/admin_view_examschedule',methods=['get','post'])
def admin_view_examschedule():
	data={}
	if "submits" in request.form:
		coll=request.form['college']
		att=request.form['att']
		q="select * from "
	q="select * from institutes"
	res1=select(q)
	data['insti']=res1
	q="SELECT * FROM candidates INNER JOIN applications USING (candidate_id) INNER JOIN exam_master USING (exam_id) INNER JOIN assign USING(application_id) INNER JOIN institutes USING(institute_id) "
	res=select(q)
	data['sche']=res
	return render_template('admin_view_examschedule.html',data=data)


@admin.route('/admin_view_applications',methods=['get','post'])
def admin_view_applications():
	data={}
	exam_id=request.args['examid']
	data['eid']=exam_id
	q="select * from applications inner join candidates using (candidate_id) where exam_id='%s'" %(exam_id)
	res=select(q)
	data['app']=res
	return render_template('admin_view_applications.html',data=data)


@admin.route('/admin_view_hallticket',methods=['get','post'])
def admin_view_hallticket():
	data={}
	q="select * from hall_ticket inner join institutes using(institute_id) inner join applications using(application_id) inner join candidates using(candidate_id)"
	res=select(q)
	data['hall']=res
	return render_template('admin_view_hallticket.html',data=data)

@admin.route('/admin_assign_institute',methods=['get','post'])
def admin_assign_institute():
	data={}

	if "iid" in request.args:
		iid=request.args['iid']
		eid=request.args['examid']
		q="insert into exam_institutes values(null,'%s','%s')" %(eid,iid)
		insert(q)
		return redirect(url_for('admin.admin_assign_institute',examid=eid))


	data['eid']=request.args['examid']

	q="select * from institutes where institute_id Not in(select institute_id from exam_institutes where exam_id='%s')" %(request.args['examid'])
	res=select(q)
	data['assign']=res
	return render_template('admin_assign_institute.html',data=data)

@admin.route('/admin_assigned_institute',methods=['get','post'])
def admin_assigned_institute():
	data={}

	data['eid']=request.args['examid']

	q="select * from institutes where institute_id in(select institute_id from exam_institutes where exam_id='%s')" %(request.args['examid'])
	res=select(q)
	data['assign']=res
	return render_template('admin_assigned_institute.html',data=data)


@admin.route('/adminviewcandidatesassigned',methods=['get','post'])
def adminviewcandidatesassigned():
	data={}
	data['eid']=request.args['examid']
	data['iid']=request.args['iid']
	if "submits" in request.form:
		print("sss")
		att=request.form['att']
		print(att)
		if att=="select":

			q="SELECT * FROM candidates WHERE candidate_id IN (SELECT candidate_id FROM applications INNER JOIN assign USING(application_id) WHERE exam_id='%s' AND institute_id='%s')" %(request.args['examid'],request.args['iid'])
		elif att=="Present":
			q="SELECT * FROM candidates WHERE candidate_id IN (SELECT candidate_id FROM applications INNER JOIN assign USING(application_id) WHERE exam_id='%s' AND institute_id='%s' and application_id in(select application_id from attendance inner join applications using (application_id) where exam_id='%s'))" %(request.args['examid'],request.args['iid'],request.args['examid'])
		elif att=="Absent":
			q="SELECT * FROM candidates WHERE candidate_id IN (SELECT candidate_id FROM applications INNER JOIN assign USING(application_id) WHERE exam_id='%s' AND institute_id='%s' and application_id not in(select application_id from attendance inner join applications using  (application_id) where exam_id='%s'))" %(request.args['examid'],request.args['iid'],request.args['examid'])
		elif att=="All":
			q="SELECT * FROM candidates WHERE candidate_id IN (SELECT candidate_id FROM applications INNER JOIN assign USING(application_id) WHERE exam_id='%s' AND institute_id='%s')" %(request.args['examid'],request.args['iid'])
	else:
		print("ss")
		q="SELECT * FROM candidates WHERE candidate_id IN (SELECT candidate_id FROM applications INNER JOIN assign USING(application_id) WHERE exam_id='%s' AND institute_id='%s')" %(request.args['examid'],request.args['iid'])
	
	print(q)
	res=select(q)
	data['cand']=res

	
	return render_template('adminviewcandidatesassigned.html',data=data)

@admin.route('/admin_institute',methods=['get','post'])
def admin_institute():
	data={}
	exam_id=request.args['examid']
	name=request.args['name']
	data['eid']=exam_id
	data['name']=name
	aid=request.args['aid']
	data['aid']=aid
	q="select * from assign inner join institutes using(institute_id)  where application_id='%s' " %(aid)
	res=select(q)
	if res:
		data['alloacted']=res[0]['name']
	

	if "submit" in request.form:
		ii=request.form['institutename']

		q="insert into assign values(null,'%s','%s',curdate(),'pending')" %(ii,aid,)
		insert(q)
		return redirect(url_for('admin.admin_view_applications',examid=exam_id))

	q="select * from exam_institutes inner join institutes using(institute_id) where exam_id='%s'" %(exam_id)
	res=select(q)
	data['app_inst']=res
	return render_template('admin_institute.html',data=data)

@admin.route('/admin_generate_QR',methods=['get','post'])
def admin_generate_QR():
	
	return render_template('admin_generate_QR.html')