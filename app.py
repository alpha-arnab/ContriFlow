from flask import Flask, render_template

app = Flask(__name__)

FEATURES = [
    'Open Source Friendly',
    'GitHub Workflow Demo',
    'Beginner Contributions'
]

@app.route('/')
def home():
    title = 'ContriFlow'
    return render_template('index.html', title=title, features=FEATURES)

if __name__ == '__main__':
    app.run(debug=True)
