
from flask import Flask, render_template, request
import notion_graph.parser  # Import your script here

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Run your script here
        notion_graph.parser.main()  # Replace with your function
        return render_template('output.html')  # Display the output
    return render_template('index.html')  # Display the home page with the button