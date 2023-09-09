from flask import Flask, render_template, url_for, request, redirect
import openai
app = Flask(__name__)
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/base', methods=["POST","GET"])
def base():
    if request.method == "POST":
        global type
        type = request.form["type"]
        global topic
        topic = request.form["topic"]
        return ai(type=type, topic=topic)
    else:
        return render_template('base.html')
    
@app.route('/login', methods=["POST","GET"])
def login():
    if request.method == "POST":
        username = request.form["usr"]
        password = request.form["pswd"]
        if username == "MeekOmni" and password == "thisisrandompass":
            return redirect('/rajasthani')
        else:
            return redirect('/index')
    else:
        return render_template('login.html')

@app.route('/rajasthani')
def admin():
    return render_template('admin.html')
def ai(type,topic):
    openai.api_key = "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"
    prereq = "You are working in the name 'OpenMind' right now, which is a educational ai supplying sources for Online education\n from now on you will talk as [OpenMind]: (prompt you generate)\n also remember that the prompt you generate must not contain any words and just links to sources, if you get any error or cant tell something just respond -1"
    "your input will be of type \" Please suggest me some (source) to learn about (topicname) \""
    "all you need to do is, link the user with sources, for example, if i ask \"please suggest me some documents to learn about python\" you can link me to python documentation website"
    "please suggest me some videos to learn about pygame\n\n"
    prompt = prereq+"please suggest me some"+type+"on the topic"+topic
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content":prompt}])
    return render_template('result.html', response = completion.choices[0].message.content)

    

if __name__=="__main__":
    app.run(debug=True)
