from flask import Flask

application=Flask(__name__)

@application.route('/',methods=['GET','POST'])
def index():
    return "<H1>AWS Elastic bean stalk deployment testing</H1>"

if __name__=="__main__":
    application.run()