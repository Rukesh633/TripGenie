import subprocess
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Flag to check if Streamlit app is already running
streamlit_running = False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/streamlit')
def streamlit_app():
    global streamlit_running

    if not streamlit_running and request.args.get('action') == 'plan_a_tour':
        # Run Streamlit app using subprocess
        subprocess.Popen(["streamlit", "run", "streamlit/code.py"])
        streamlit_running = True

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)