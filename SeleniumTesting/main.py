from flask import Flask, render_template

app = Flask(__name__)


def db_connection_usage():
    return 'x'


@app.route('/<string:my_name>/')
def index(my_name: str):

    return render_template(
        'index.html',
        my_name=my_name,
        your_name='alexander'
    )


@app.route('/integer/<int:identificator>/')
def print_id(identificator: int):
    return render_template(
        'index.html',
        my_name=identificator,
        your_name='alexander'
    )


@app.route('/button_click', methods=['POST'])
def use_db_connection():
    return db_connection_usage()


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
