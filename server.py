from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
 return render_template('index.html')

@app.route('/<string:page>')
def page_html(page):
 return render_template(page)

def DataBase(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n \n email: {email},\n subject: {subject}, \n message: {message}')

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        DataBase(data)
        return redirect('ThankYou.html')
    else:
        return redirect('oops.html')

if __name__ == '__main__':
    app.run(debug=True)