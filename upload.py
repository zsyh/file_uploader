from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # 检查是否有文件被上传
        if 'file' not in request.files:
            return 'No file uploaded.'
        
        file = request.files['file']
        
        # 检查文件名是否为空
        if file.filename == '':
            return 'No selected file.'
        
        # 保存文件到当前文件夹
        file.save(file.filename)
        
        return 'File uploaded successfully.'
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
