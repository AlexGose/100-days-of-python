from flask import Flask, render_template, request
import requests
import smtplib
import os

response = requests.get('https://api.npoint.io/2a4be25f4f1d7f080ec5')
blogs_data = response.json()

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('index.html', blogs_data=blogs_data)


@app.route('/about.html')
def about():
    return render_template('about.html')


@app.route('/contact.html', methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        return render_template('contact.html', method='GET')
    else:
        send_email(request.form['name'], request.form['email'],
                   request.form['phone'], request.form['message'])
        return render_template('contact.html', method='POST')


def send_email(name, email, phone, message):
    message_string = f"Subject: Message from {name}\n\nname:{name}\n"
    message_string += f"email:{email}\nphone:{phone}\nmessage:{message}"

    my_email = os.getenv("EMAIL_ADDRESS")
    password = os.getenv("EMAIL_PASSWORD")
    smtp_server = os.getenv("SMTP_SERVER")
    smtp_port = int(os.getenv("SMTP_PORT"))

    with smtplib.SMTP(smtp_server, port=smtp_port) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email,
                            msg=message_string)


@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template('post.html', blog=blogs_data[post_id-1])


if __name__ == '__main__':
    app.run(debug=True)
