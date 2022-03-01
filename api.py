from flask import *
from database import *
import demjson
import uuid
from core import *

api=Blueprint('api',__name__)

@api.route('/login')
def login():
	data={}
	username=request.args['username']
	password=request.args['password']
	q="select * from login where username='%s' and password='%s'" %(username,password)
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	return demjson.encode(data)


@api.route('/candidate_register',methods=['get','post'])
def candidate_register():
	data={}
	fname=request.form['fname']
	lname=request.form['lname']
	dob=request.form['dob']
	place=request.form['place']
	gender=request.form['gender']
	phone=request.form['phone']
	email=request.form['email']
	hname=request.form['hname']
	username=request.form['username']
	password=request.form['password']
	pincode=request.form['pincode']
	image=request.files['image']
	path="static/"+str(uuid.uuid4())+image.filename
	image.save(path)
	q="insert into login values(null,'%s','%s','candidates')"%(username,password)
	id=insert(q)
	q="insert into candidates values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" %(id,fname,lname,gender,dob,hname,place,pincode,phone,email,path)
	insert(q)
	print(q)
	data['status']="success"
	return demjson.encode(data)

@api.route('/candidateviewexam')
def candidateviewexam():
	data={}
	q="select * from exam_master"
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	data['method']="candidateviewexam"
	return demjson.encode(data)


@api.route('/candidateviewapplication')
def candidateviewapplication():
	data={}
	lid=request.args['lid']
	q="select * from applications inner join exam_master using (exam_id) inner join candidates using (candidate_id) where candidate_id=(select candidate_id from candidates where login_id='%s') " %(lid)
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	return demjson.encode(data)

@api.route('/applyexam')
def applyexam():
	data={}
	lid=request.args['lid']
	eid=request.args['eid']
	q="insert into applications values(null,'%s',(select candidate_id from candidates where login_id='%s'),now(),'','pending')" %(eid,lid)
	insert(q)
	data['status']="success"
	data['method']="applyexam"
	return demjson.encode(data)


@api.route('/view_halltickets')
def view_halltickets():
	data={}
	aid=request.args['aid']
	q="SELECT * FROM assign INNER JOIN institutes USING (institute_id) inner join applications using (application_id) inner join candidates using (candidate_id)  inner join exam_master using (exam_id) where application_id='%s'" %(aid)
	res=select(q)
	print(res)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	return demjson.encode(data)



@api.route('/view_profile')
def view_profile():
	data={}
	lid=request.args['lid']
	q="SELECT * FROM  candidates WHERE candidate_id=(select candidate_id from candidates where login_id='%s')"%(lid)
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	data['method']="view_profile"
	return demjson.encode(data)

@api.route('/candidateupdateprofile')
def candidateupdateprofile():
	data={}
	lid=request.args['lid']
	fname=request.args['fname']
	lname=request.args['lname']
	dob=request.args['dob']
	hname=request.args['hname']
	place=request.args['place']
	pin=request.args['pin']
	phone=request.args['phone']
	email=request.args['email']

	q="update candidates set first_name='%s',last_name='%s',dob='%s',house_name='%s',place='%s',pincode='%s',phone='%s',email='%s' where login_id='%s'"%(fname,lname,dob,hname,place,pin,phone,email,lid)
	update(q)
	print(q)

	data['status']="success"
	data['method']="candidateupdateprofile"
	return demjson.encode(data)



@api.route('/view_staff_profile')
def view_staff_profile():
	data={}
	lid=request.args['lid']
	q="SELECT * FROM staff WHERE staff_id=(select staff_id from staff where login_id='%s')"%(lid)
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	data['method']="view_staff_profile"
	return demjson.encode(data)


@api.route('/staffupdateprofile')
def staffupdateprofile():
	data={}
	lid=request.args['lid']
	fname=request.args['fname']
	lname=request.args['lname']
	phone=request.args['phone']
	email=request.args['email']

	q="update staff set first_name='%s',last_name='%s',phone='%s',email='%s' where login_id='%s'"%(fname,lname,phone,email,lid)
	update(q)
	print(q)

	data['status']="success"
	data['method']="staffupdateprofile"
	return demjson.encode(data)


@api.route('/view_candidates')
def view_candidates():
	data={}
	lid=request.args['lid']
	eid=request.args['eid']
	q="SELECT *,`candidates`.`first_name` AS cfname,`candidates`.`last_name` AS clname,`candidates`.`place`AS cplace,`candidates`.`phone`AS cphone,`candidates`.`email` AS cemail FROM candidates INNER JOIN applications USING (candidate_id) INNER JOIN exam_master USING (exam_id) INNER JOIN assign USING(application_id) WHERE institute_id=(SELECT institute_id FROM staff WHERE login_id='%s' and exam_id='%s')"%(lid,eid)
	print(q)
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	data['method']="view_candidates"
	return demjson.encode(data)


@api.route('/viewqrscannedcandidate')
def viewqrscannedcandidate():
	data={}
	lid=request.args['id']
	# lid=13
	q="""SELECT *,CONCAT(`candidates`.`first_name`,' ',`candidates`.`last_name`) as cname FROM `applications` 
    INNER JOIN `candidates` ON `applications`.`candidate_id`=`candidates`.`candidate_id`
    INNER JOIN assign ON `assign`.`application_id`=`applications`.`application_id`
    INNER JOIN `institutes` ON `institutes`.`institute_id`=`assign`.`institute_id` where applications.application_id='%s'"""%(lid)
	print(q)
	res=select(q)
	if res:
		q="SELECT * FROM seats INNER JOIN `classroom` USING(classroom_id) INNER JOIN block USING(block_id) WHERE application_id='%s' " %(lid)
		res1=select(q)
		data['status']="success"
		data['cname']=res[0]['cname']
		data['photo']=res[0]['photo']
		data['latis']=res[0]['latitude']
		data['longis']=res[0]['longitude']
		data['aid']=res[0]['application_id']
		data['iname']=res[0]['name']
		data['block']="Block : "+str(res1[0]['block_name']) 
		data['classname']="Class Name : "+str(res1[0]['class_name'])
		data['seat']="Seat : "+str(res1[0]['seat_no'])
	else:
		data['status']="failed"
	return demjson.encode(data)

@api.route('/view_details')
def view_details():
	data={}
	aid=request.args['aid']
	
	q="SELECT * FROM seats INNER JOIN `classroom` USING(classroom_id) INNER JOIN block USING(block_id) WHERE application_id='%s' " %(aid)
	res1=select(q)
	if res1:
		data['status']="success"
		
		data['block']="Block : "+str(res1[0]['block_name']) 
		data['classname']="Class Name : "+str(res1[0]['class_name'])
		data['seat']="Seat : "+str(res1[0]['seat_no'])
	else:
		data['status']="failed"
	data['method']="view_details"
	return demjson.encode(data)


@api.route('/staffviewexam')
def staffviewexam():
	lid=request.args['lid']
	data={}
	q="select * from exam_master where exam_id in (select exam_id from exam_institutes where institute_id in (select institute_id from staff where login_id='%s'))" %(lid) 
	print(q)
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	data['method']="staffviewexam"
	return demjson.encode(data)



@api.route('/verifyuser/',methods=['get','post'])
def verifyuser():

	data = {}

	image=request.files['image']
	content=request.form['content']
	print("fdg"+content)
	eid=request.form['eid']

	path="static/tests.jpg"
	image.save(path)
	idval=val(path,eid)
	# print(idval)
	# if idval==" ":
	q="select * from facialdetails where candidate_id='%s'" %(idval)
	print(q) 
	res=select(q)
	print(res)
	# print("cc"+content)
	# print("ff"+res[0]['fdetail_id'])
	if res:
		# if int(content)==int(res[0]['fdetail_id']):
		data['status']='success'
		data['val']=idval
		# else:
		# 	data['status']='failed'
		# else:
		# 	data['status']='failed'
		print(data['status'])
	else:
		data['status']='failed'

	
	data['method']='verifyuser'
	
	return demjson.encode(data)


@api.route('/viewcandidatedetails')
def viewcandidatedetails():
	cid=request.args['cid']
	eid=request.args['eid']
	data={}
	q="select * from applications where exam_id='%s' and candidate_id='%s'" %(eid,cid)
	res2=select(q)
	q="select * from attendance where application_id='%s'" %(res2[0]['application_id'])
	res=select(q)
	if not res:
		q="insert into attendance values(null,'%s')" %(res2[0]['application_id'])
		insert(q)

	q="SELECT *,candidates.phone as numm FROM `applications` inner join candidates using (candidate_id) inner join exam_master on applications.exam_id=exam_master.exam_id INNER JOIN `assign` ON `applications`.`application_id`=`assign`.`application_id` INNER JOIN `institutes` ON `assign`.`institute_id`=`institutes`.`institute_id` WHERE applications.candidate_id='%s' AND applications.exam_id='%s'" %(cid,eid)
	print(q)
	res=select(q)
	# print(res)
	if res:
		q="SELECT * FROM seats INNER JOIN `classroom` USING(classroom_id) INNER JOIN block USING(block_id) WHERE `application_id`='%s'" %(res[0]['application_id'])
		print(q)
		res1=select(q)
		print(res1)
		data['status']="success"
		data['data']=res
		data['seat']="Block : "+str(res1[0]['block_name'])+" " +"Class : "+ str(res1[0]['class_name']) +" "+"Seat NO : "+str(res1[0]['seat_no'])
	else:
		data['status']="failed"
	data['method']="viewcandidatedetails"
	return demjson.encode(data)
