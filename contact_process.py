import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask import Flask, request

app = Flask(__name__, static_folder='.')

@app.route('/contact.html')
def contact():
    return app.send_static_file('contact.html')

@app.route('/')
def home():
    return app.send_static_file('index.html')


# Route for CSS files
@app.route('/css/<path:path>')
def send_css(path):
    return app.send_static_file(f'css/{path}')

# Route for JavaScript files
@app.route('/js/<path:path>')
def send_js(path):
    return app.send_static_file(f'js/{path}')

# Route for image files
@app.route('/img/<path:path>')
def send_img(path):
    return app.send_static_file(f'img/{path}')

@app.route('/send_email', methods=['POST'])
def send_email():
    to_email = "spn8@spondonit.com"
    from_email = request.form['email']
    name = request.form['name']
    subject = request.form['subject']
    message = request.form['message']

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = "You have a message from your Bitmap Photography."

    body = f"""
    <html>
      <head></head>
      <body>
        <table style="width: 100%;">
          <tr>
            <td style="border:none;"><strong>Name:</strong> {name}</td>
            <td style="border:none;"><strong>Email:</strong> {from_email}</td>
          </tr>
          <tr>
            <td style="border:none;"><strong>Subject:</strong> {subject}</td>
          </tr>
          <tr>
            <td colspan='2' style="border:none;">{message}</td>
          </tr>
        </table>
      </body>
    </html>
    """
    msg.attach(MIMEText(body, 'html'))

    mailserver = smtplib.SMTP('localhost', 1025)
    mailserver.login('', '')
    mailserver.sendmail(from_email, to_email, msg.as_string())
    mailserver.quit()

    return "Email sent successfully!"

if __name__ == '__main__':
    app.run(debug=True, port=5500)
