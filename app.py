from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def data():
    data = request.get_json()
    a = np.array(data["a"])
    b = np.array(data["b"])
    x, residuals, rank, s = np.linalg.lstsq(a,b, rcond=None)
    print("residuals",residuals)
    print(residuals == [])
    if residuals.size == 0:
        return jsonify({'response': list(np.round(x, 2))}), 200
    else:
        return jsonify({'response': []}), 200


if __name__ == '__main__':
    app.run(port=5000, debug=True)
