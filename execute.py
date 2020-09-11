from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

@app.route('/')
def main():
    return render_template(
        'ox.html', 
        displayTitle = "OX Quiz Example Template", 
        displayText = "displayText example", 
        displayProblem = "displayProblem example"
    )

if __name__ == '__main__':
    app.debug = True
    app.run()