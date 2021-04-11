from flask import Flask

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    return "<H1>AWS Elastic bean stalk deployment testing</H1>"

if __name__=="__main__":
    app.run()