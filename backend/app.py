from flask import Flask, render_template,request
import os

frontend_path = os.path.join(os.path.dirname(__file__), '..', 'frontend')

app = Flask(
    __name__,
    template_folder=os.path.join(frontend_path, 'templates'),
    static_folder=os.path.join(frontend_path, 'static')
)

@app.route('/')
def home():
    return render_template('index.html')



@app.route('/quadratic', methods=['GET', 'POST'])
def quadratic():
    if request.method == 'POST':
        pass
    return "Welcome Quadratic Page"


if __name__ == '__main__':
            app.run(debug=True)

