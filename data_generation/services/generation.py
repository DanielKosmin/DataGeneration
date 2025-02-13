from data_generation.models.models import GenerationRequest
import json


def generate_synthetic_data(num_json_objects: int, list_key: str) -> str:
    records = [GenerationRequest() for _ in range(num_json_objects)]
    records_objs = [obj.to_obj() for obj in records]
    return json.dumps({list_key: records_objs}, indent=2)


if __name__ == "__main__":
    print(generate_synthetic_data(100, "inputRecords"))
