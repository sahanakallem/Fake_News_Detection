from flask import Flask, request, jsonify
from flask_cors import CORS
from lstm import predict as predict_lstm, vocab

app = Flask(__name__)
CORS(app, resources={r"/predict": {"origins": "*"}}, support_credentials=True)

def predict_other_model(title):
    return "Real or Fake (from other model)"

@app.route('/predict', methods=['POST'])
def get_prediction():
    data = request.get_json(force=True)
    title = data['title']
    model = data.get('model', 'lstm')

    if model == 'lstm':
        result = predict_lstm(title, vocab)  # Passing vocab here
    elif model == 'otherModel':
        result = predict_other_model(title)
    else:
        return jsonify({'error': 'Model not supported'}), 400

    return jsonify(prediction=result)

if __name__ == '__main__':
    app.run(debug=True)
