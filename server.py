from flask import Flask, request, url_for, render_template
import sqlite3
import os

app = Flask(__name__)


def get_template(page, navbar='components/navbar.html', page_title=''):
	return render_template('template.html', page=page, navbar=navbar, page_title=page_title)



@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)



@app.route('/')
def index():
	return get_template(page='pages/home.html')

@app.route('/dashboard/applications')
def applications():
	return get_template(page='pages/dashboard.html', navbar='components/_navbar.html', page_title='Applications')

@app.route('/dashboard/applications/new')
def new_application():
	return get_template(page='pages/new_application.html', navbar='components/_navbar.html', page_title='New Application')

@app.route('/dashboard/contents')
def contents():
	return get_template(page='pages/contents.html', navbar='components/_navbar.html', page_title='Contents')

@app.route('/dashboard/contents/new')
def new_contents():
	return get_template(page='pages/new_content.html', navbar='components/_navbar.html', page_title='New Contents')

@app.route('/login')
def login():
	return get_template(page='pages/login.html')

@app.route('/signup')
def signup():
	return get_template(page='pages/signup.html')


if __name__ == '__main__':
	app.run(port=80, debug=True)