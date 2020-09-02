from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/test',methods=['POST'])
def test():
    print ("you got me")
    payload = request.form.get('payload')
    print (payload)
    return jsonify({'message': 'ok' }), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)