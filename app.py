
from flask import Flask, render_template, request
import notion_graph.parser  # Import your script here
import subprocess

app = Flask(__name__, template_folder="templates_new")

@app.route('/', methods=['GET', 'POST'])

def home():
    if request.method == 'POST':
        command = ['pdm', 'run', 'start', '-p', 'ed228bfa2ece43f0a34a0aa95985a501', '-t', 'secret_37RsVuHNkIx573FXkg4geRqXcmiBSlBH45QxmVEXIQ9', '-o', './graph_out.html']
        process = subprocess.Popen(command, stdout=subprocess.PIPE)
        output, error = process.communicate()

        with open('graph_out.html') as f:
            graph_output = f.read()
            
        return render_template('output.html', output=graph_output)

    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
    
    print(app.template_folder)