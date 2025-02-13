from data_generation.models.models import GenerationRequest
import json


def generate_synthetic_data(num_json_objects: int, list_key: str) -> str:
    return json.dumps(
        {list_key: [GenerationRequest().to_obj() for _ in range(num_json_objects)]},
        indent=2,
    )


if __name__ == "__main__":
    print(generate_synthetic_data(100, "inputRecords"))
