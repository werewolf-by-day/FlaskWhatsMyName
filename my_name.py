from flask import Flask, render_template, request, redirect
app = Flask(__name__)

app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def create_user():
   print "Got Post Info"
   name = request.form['name']
   return redirect('/')
   print request.form
app.run(debug=True)
