from flask import Flask, render_template,request
from solver.number_base import base2
import os

frontend_path = os.path.join(os.path.dirname(__file__), '..', 'frontend')

app = Flask(
    __name__,
    template_folder=os.path.join(frontend_path, 'templates'),
    static_folder=os.path.join(frontend_path, 'static')
)


OPTIONS = {
    "median": 'solve_median',
    "mean": 'solve_mean',
    "mode": 'solve_mode',
    "range": 'solve_range'
}




@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    error = None

    if request.method == 'POST':
        select_option = request.form.get('topic')
        values = request.form.get('question', '').strip()

        if not select_option or not values:
            error = "Please select a topic and enter a question."
        else:
            handler = OPTIONS.get(select_option)
            if handler:
                result = handler(values)

    return render_template('index.html', error=error, result=result)


@app.route('/quadratic', methods=['GET', 'POST'])
def quadratic():
    if request.method == 'POST':
        pass
    return "Welcome Quadratic Page"


if __name__ == '__main__':
            app.run(debug=True)

