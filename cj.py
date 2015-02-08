from flask import Flask, render_template, jsonify, request, g
import sqlite3

DATABASE = 'celebs.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
  return sqlite3.connect(app.config['DATABASE'])

@app.before_request
def before_request():
  g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
  db = getattr(g, 'db', None)
  if db is not None:
    db.close()

@app.route('/')
def index():
  return render_template('question.html')

@app.route('/_question')
def question():
  ids = request.args.get('ids').split()
  query = 'SELECT id, question, answerA, descriptionA, answerB, descriptionB FROM questions WHERE id NOT IN (' + ",".join("?"*len(ids)) + ') ORDER BY RANDOM() LIMIT 1;'
  v = g.db.execute(query, ids).fetchone()
  q = jsonify(id=v[0], question=v[1], answerA=v[2], descriptionA=v[3], answerB=v[4], descriptionB=v[5])
  return q

@app.route('/_answer')
def answer():
  i = request.args.get('id')
  v = g.db.execute('SELECT aCount, bCount FROM questions WHERE id = ?', [i]).fetchone()
  a = v[0]
  b = v[1]
  if request.args.get('answer') == 'a':
    a += 1
    g.db.execute('UPDATE questions SET aCount=? WHERE id=?;', [a, i])
    g.db.commit()
  elif request.args.get('answer') == 'b':
    b += 1
    g.db.execute('UPDATE questions SET bCount=? WHERE id=?;', [b, i])
    g.db.commit()
  aCount = int(round(100.0*a/(a+b)))
  bCount = int(round(100.0*b/(a+b)))
  return jsonify(aCount=aCount, bCount=bCount)

@app.route('/about')
def about():
  return render_template('about.html')


if __name__ == '__main__':
  app.run(host='0.0.0.0')