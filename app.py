from flask import Flask

app = Flask(__name__)

@app.route('/api', methods=['GET', 'POST'])
def get_api():
    if request.method == 'POST':
        print(request.form)
        return '{"challenge":"35902439"}'

if __name__ == '__main__':
    app.run(port=80)