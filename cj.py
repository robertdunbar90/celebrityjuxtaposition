from flask import Flask, render_template, jsonify
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('question.html')

@app.route('/_question')
def question():
  return jsonify(question='Who is your favorite Knowles?',
    answerA='Nick', answerB='Beyonce')

@app.route('/_answer')
def answer():
  return jsonify(aCount=3, bCount=2)

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')