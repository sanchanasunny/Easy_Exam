from public import *
staff=Blueprint('staff',__name__)

@staff.route('/staff_home')

def staff_home():
	return render_template('staff_home.html')
