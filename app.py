from flask import Flask, abort
import random
import os

app = Flask('service')

@app.route('/random')
def index():
  r = random.randint(1,6)
  print(f'Rolled a {r}')
  return str(r)

@app.route('/health')
def health():
  r = random.randint(1,1000)
  if r == 1:
    print(f'error: {random.randint(500,599)}')
    abort(500)
  return '', 200
