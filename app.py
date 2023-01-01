from flask import Flask,render_template,request,redirect
import sqlite3
app = Flask(__name__)

# --------------------------------indexpage---------------------------
@app.route('/')
def index():
    return render_template('index.html')

# --------------------------------registerpage---------------------------
@app.route('/register',methods=['POST','GET'])
def register():
    if request.method == "POST":
# sqlite
        connection = sqlite3.connect("userdata.db")
        cursor = connection.cursor()

#Html form
        name=request.form['name']
        username=request.form['username']
        Email=request.form['email']
        password=request.form['password']
        conformpassword=request.form['conformpassword']
        data=[name,username,Email,password,conformpassword]
        #print(name,username,email,password,conformpassword)
        query="INSERT INTO registerdata(name,username,Email,password,conformpassword) VALUES (?,?,?,?,?)"
        cursor.execute(query,data)
        connection.commit()
        return redirect('/login')
    return render_template('register.html')

# --------------------------------loginpage---------------------------
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == "POST":
# sqlite
        connection = sqlite3.connect("userdata.db")
        cursor = connection.cursor()

#Html form
        username=request.form['username']
        password=request.form['pswrd']

       # print(username,password)
#query
        query = "SELECT username,password FROM registerdata where username='"+username+"' and password='"+password+"'"
        cursor.execute(query)

        results = cursor.fetchall()

#validation
        if len(results) == 0:
            return "userid and password is incorrect"
        else:
            return redirect("/home")
    return render_template('login.html')

# --------------------------------homepage---------------------------
@app.route('/home')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)