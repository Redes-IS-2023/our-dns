testing_ep_doc = {
    "summary": "Get data from Firebase (use for testing only)",
    "parameters": [
        {
            "name": "param",
            "in": "path",
            "type": "string",
            "description": "Base64 encoded path to the data in Firebase",
            "required": True,
        }
    ],
    "responses": {
        "200": {
            "description": "Data retrieved successfully",
            "schema": {"type": "object"},
        },
        "400": {"description": "Invalid param"},
        "404": {"description": "Data not found"},
    },
}
