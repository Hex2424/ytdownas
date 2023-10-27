from flask import Flask
from flask import send_file
from flask import Flask, render_template
from flask import request
from flask import redirect
from concurrent.futures import ThreadPoolExecutor
import ytdownas
import os
import re
# executor = ThreadPoolExecutor(max_workers=10)
debug_log = ""

app = Flask(__name__, template_folder='html', static_folder='css')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_debug_log')
def get_debug_log():
    global debug_log
    return debug_log

@app.route('/handle_post', methods=['POST'])
def handle_post():
    global debug_log
    if request.method == 'POST' and request.form['input'] != "":
        print(request.form)
        query = request.form['input']
        seed = request.form['seed']
  
        if seed == "":
            seed = 1
        else:
            seed = int(seed)
        
        debug_log = f"Collecting ingridients : '{query}'"
        url, title = ytdownas.getVideoUrlTitle(query, seed)

        debug_log = f"Cooking ingridients : '{query}'"
        path = ytdownas.downloadVideo(url, title)

        if os.path.exists(path):
            mp3FileName = f"{title}.mp3"
            debug_log = f"Cooking recipe..."
            status = send_file(path, as_attachment=True, download_name=mp3FileName)
            debug_log = f"Here is your cake..."
            os.remove(path)
            return status
        
    debug_log = f"Song name can't be empty"

    return redirect("/")

if __name__ == '__main__':
    app.run(port=5000,host="192.168.1.186",debug=True) 

