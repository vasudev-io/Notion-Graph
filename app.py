
from flask import Flask, render_template, request
import notion_graph.parser  # Import your script here
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def home():
    if request.method == 'POST':
        command = ['ls', '-l']  # Replace with your command
        process = subprocess.Popen(command, stdout=subprocess.PIPE)
        output, error = process.communicate()

        # Pass the output to another template
        return render_template('output.html', output=output.decode('utf-8'))

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)