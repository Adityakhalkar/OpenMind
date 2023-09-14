from flask import Flask, render_template, url_for, request, redirect
import openai
app = Flask(__name__)
@app.route('/home')
@app.route('/Home')
@app.route('/HOME')
def index():
    return render_template('index.html')

@app.route('/base', methods=["POST","GET"])
def base():
    if request.method == "POST":
        global type
        type = request.form["type"]
        global topic
        topic = request.form["topic"]
        global domain
        domain = request.form["domain"]
        return ai(type=type, topic=topic, domain=domain)
    else:
        return render_template('base.html')
        
    

def ai(type,topic,domain):
    openai.api_key = "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"
    prereq = "You are working in the name 'OpenMind' right now, which is a educational ai supplying sources for Online education\n from now on you will talk as [OpenMind]: (prompt you generate)\n"
    "your input will be of type \" Please suggest me some (source) to learn about (topicname) \""
    "all you need to do is, link the user with sources, for example, if i ask \"please suggest me some documents to learn about python\" you can link me to python documentation website"
    "please suggest me some videos to learn about pygame\n\n"
    if type == "Video":
        prompt = prereq+"please suggest me some"+type+"on the topic"+topic+"of the topic"+domain+"I dont want any text, just give me links"
        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content":prompt}])
        l=completion.choices[0].message.content.split("=")
        result=''
        for i in l[1:2]:
            result=result+"<iframe width='560' height='315' src='https://www.youtube.com/embed/"+i[:12]+"' allowfullscreen></iframe>"
        return render_template('result.html', response=result,type=type, domain=domain)
    elif type == "Documents":
        prompt = prereq+"Can you provide me with useful links related to"+domain+topic+"?This could include the official"+domain+"beginner's guides, tutorials, or any other relevant Python resources"
        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content":prompt}])
        result = "<p>"+str(completion.choices[0].message.content)+"</p>"
        return render_template('result.html', response=result, type=type, domain= domain, topic=topic)
    elif type == "Podcast":
        prompt = prereq+"please suggest me some Podcasts on the topic"+topic+"of the topic"+domain+"I dont want any text, just give me links from spotify"
        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content":prompt}])
        result = "<p>"+str(completion.choices[0].message.content)+"</p>"
        return render_template('result.html', response=result, type=type, domain= domain, topic=topic)
    elif type == "books":
        prompt = prereq+"please suggest me some books on the topic"+topic+"of the domain"+domain+"I dont want any text, just give me links from amazon for the books"
        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content":prompt}])
        result = "<p>"+str(completion.choices[0].message.content)+"</p>"
    else:
        pass
    

if __name__=="__main__":
    app.run(debug=True)
