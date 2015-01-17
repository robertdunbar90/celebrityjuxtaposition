from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('question.html')

@app.route('/_question')
def question():
  return jsonify(question='Who is your favorite Knowles?',
    answerA='Nick', answerB='Beyonce', id=23)

@app.route('/_answer')
def answer():
  a = 1
  b = 1
  if request.args.get('answer') == 'a': a += 1
  elif request.args.get('answer') == 'b': b += 1
  aCount = 100*a/(a+b)
  bCount = 100*b/(a+b)
  return jsonify(aCount=aCount, bCount=bCount)

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')