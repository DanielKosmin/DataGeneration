import json
from flask import Flask, request, jsonify
from data_generation.services.generation import generate_synthetic_data
from data_generation.models.models import DataGenerationPayload

app = Flask(__name__)


@app.route('/data_generation/v1/generate', methods=['POST'])
def generate_json_data():
    payload = request.get_json()

    try:
        if 'number_test_records' in payload and 'payload_key' in payload:
            request_object = DataGenerationPayload(**payload)
            return jsonify(
                json.loads(
                    generate_synthetic_data(request_object.number_test_records, request_object.payload_key))), 201
        else:
            return jsonify({"error": "Missing required fields"}), 400
    except ValueError as e:
        return jsonify({"error": e.args[0]}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
