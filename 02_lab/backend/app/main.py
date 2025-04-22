from __init__ import create_app

app = create_app()

@app.route('/api')
def hello_world():
    return {'message': 'Hello from the backend!'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
