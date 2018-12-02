from flask import render_template
from app import t_app
from app.forms import TargetDomain
import subprocess

@t_app.route('/', methods=['GET', 'POST'])
def index():
	form = TargetDomain()		
	if form.validate_on_submit():
		target = str(form.url1.data)
		print target
		front = str(form.url2.data)
		print front
		cmd=["curl", "-s", "-H " "Host: ", target, "-H", "Connection: close", front]
		p=subprocess.Popen(cmd, stdout=subprocess.PIPE)
		#p2=subprocess.Popen(['grep', 'title'], stdin=p.stdout, stdout=subprocess.PIPE)
		output=p.stdout.read().decode('utf-8')
		print output

	form.url1.data = ""
	form.url2.data = ""
	return render_template('index.html', form=form)


