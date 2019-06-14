from flask import Flask,request,render_template
import os
from werkzeug.utils import secure_filename
from flask import send_from_directory

app = Flask(__name__)

@app.route('/')
def hello(name=None):
    return render_template('index.html', name=name)

#新建images文件夹，UPLOAD_PATH就是images的路径
UPLOAD_PATH = os.path.join(os.path.dirname(__file__),'images')

@app.route('/upfile')
def upfile():
    return render_template('upload.html')


#this is ok
@app.route('/up_file', methods=['GET', 'POST'])
def up_file():
    if request.method == "POST":
        print("this is up_file=============")
        file = request.files['file']
        #  file_name = "test.csv"
        file_name = file.filename
        file.save(os.path.join(UPLOAD_PATH, file_name))

        return 'ok upload success yms ! server return reply'






@app.route('/upload/',methods=['GET','POST'])
def settings():
    if request.method == 'GET':
        return render_template('upload.html')
    else:
        print("ok im come!")
        desc = request.form.get('desc')#接收描述信息数据
        avatar = request.files.get('avatar') #接收文件数据
        # 对文件名进行包装，为了安全,不过对中文的文件名显示有问题
        filename = secure_filename(avatar.filename)
        avatar.save(os.path.join(UPLOAD_PATH,filename))
        print(desc)
        return 'file upload success'

#访问上传的文件
#浏览器访问：http://127.0.0.1:5000/images/django.jpg/  就可以查看文件了
@app.route('/images/<filename>/',methods=['GET','POST'])
def get_image(filename):
    return send_from_directory(UPLOAD_PATH,filename)





if __name__ == '__main__':
    app.run(debug=True)