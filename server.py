from flask import Flask, request, json, Response
app = Flask(__name__)

@app.route('/test', methods=['GET'])
def hello():
    name = "Hello World"
    return name

@app.route('/sensor', methods=['GET'])
def get_sensor_data():
    device_id = request.args.get('device_id')
    date = request.args.get('date')
    temp = request.args.get('temperature')
    seq_num = request.args.get('seq_num')

    return Response(json.dumps({'success': True}), mimetype='application/json')

if __name__ == "__main__":
    port = 8080
    host='0.0.0.0'
    app.run(host=host, port=port, debug=True, processes=3)
