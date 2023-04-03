from flask import Flask, request, session, redirect, url_for, render_template
from datetime import datetime

app = Flask(__name__)

users = {}
messages = {'public': []}
channels = ['public']

# Page de connexion
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email in users and users[email]['password'] == password:
            session['email'] = email
            return redirect(url_for('main'))
        else:
            return render_template('login.html', error='Mauvais email ou mot de passe')
    else:
        return render_template('login.html', error='')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        if email in users:
            return render_template('register.html', error='Cet email est déjà utilisé')
        else:
            users[email] = {
                'first_name': request.form['first_name'],
                'last_name': request.form['last_name'],
                'password': request.form['password']
            }
            session['email'] = email
            return redirect(url_for('main'))
    else:
        return render_template('register.html', error='')

@app.route('/main', methods=['GET', 'POST'])
def main():
    if 'email' not in session:
        return redirect(url_for('login'))
    elif request.method == 'POST':
        channel = request.form['channel']
        if channel not in channels:
            channels.append(channel)
            messages[channel] = []
        return redirect(url_for('channel', channel=channel))
    else:
        email = session['email']
        user = users[email]
        return render_template('main.html', user=user, channels=channels)

@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect(url_for('login'))

@app.route('/channel/<channel>', methods=['GET', 'POST'])
def channel(channel):
    if 'email' not in session:
        return redirect(url_for('login'))
    elif channel not in channels:
        return redirect(url_for('main'))
    elif request.method == 'POST':
        email = session['email']
        user = users[email]
        time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        message = {
            'author': user['first_name'] + ' ' + user['last_name'],
            'time': time,
            'text': request.form['text']
        }
        messages[channel].append(message)
        return redirect(url_for('channel', channel=channel))
    else:
        email = session['email']
        user = users[email]
        return render_template('channel.html', user=user, channel=channel, messages=messages[channel])

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.run(debug=True)