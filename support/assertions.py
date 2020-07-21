from jsonschema import validate


def assert_valid_schema(data):
    """Checks whether the given data matches the schema"""
    schema = {
        "type": "array",
        "items": {
            "properties": {
                "body": {"type": "string"},
                "id": {"type": "number"},
                "title": {"type": "string"},
                "userId": {"type": "number"}
            },
            "required": ["body", "id", "title", "userId"]
        },
        "additionalItems": False

    }

    return validate(data, schema)
