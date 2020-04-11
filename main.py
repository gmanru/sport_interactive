from flask import Flask, render_template
app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('test.html')

@app.route('/my_posts')
def posts():
    return render_template('posts.html')

@app.route('/post_1')
def post1():
    return render_template('post1.html')

@app.route('/post_2')
def post2():
    return render_template('post2.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

if __name__ == '__main__':
    app.run(debug=True)
