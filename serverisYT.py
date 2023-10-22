from flask import Flask
from flask import send_file
from flask import Flask, render_template
from flask import request
from flask import redirect
import ytdownas
import os




app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download/<filename>')
def downloadFile (filename):
    #For windows you need to use drive name [ex: F:/Example.pdf]
    filePath = ytdownas.downloadVideo(filename)
    status = send_file(filePath, as_attachment=True)
    os.remove(filePath)
    return status

@app.route('/handle_post', methods=['POST'])
def handle_post():
  
    if request.method == 'POST' and request.form['input'] != "":
        inputy = request.form['input']
        if "&&" in inputy:
            inputy = inputy.split("&&")
        else:
            # inputy = [inputy]
            status = redirect("/download/inputy", code=302)

        
        # print(inputy)

        # # for path in inputy:
        # #     filePath = ytdownas.downloadVideo(path)
        # #     status = send_file(filePath, as_attachment=True)
        # #     os.remove(filePath)
        
        return status
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(port=5000,debug=True) 


