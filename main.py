from flask import Flask, render_template, request
from flask_ckeditor import CKEditor
from datetime import datetime
import time

app = Flask(__name__)
app.config['CKEDITOR_PKG_TYPE'] = 'basic'
ckeditor = CKEditor(app)

today = datetime.today().strftime('%Y/%m/%d - %H:%M:%S')

@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        data = request.form.get('ckeditor')
        print(data)
        with open('input_log.txt',mode='a') as file:
            file.write(today + '\n' + data + '\n\n')
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)