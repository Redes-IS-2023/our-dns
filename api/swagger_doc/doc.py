get_dns_testing_ep_doc = {
    "summary": "Get dns data from Firebase (use for testing only)",
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
            "schema": {
                "type": "object",
                "properties": {
                    "type": {
                        "type": "string",
                        "example": "single | multi | geo | weight",
                    },
                    "resolve": {"type": "array", "example": "[1.1.1.1, 2.2.2.2]"},
                },
            },
        },
        "400": {"description": "Invalid param"},
        "404": {"description": "Data not found"},
    },
}

post_dns_package_ep_doc = {
    "summary": "Post package encoded in base64 to DNS server",
    "parameters": [
        {
            "in": "body",
            "name": "data",
            "description": "String data encoded in base64 format",
            "required": True,
            "schema": {
                "type": "string",
                "format": "byte",
                "description": "Base64 encoded package",
            },
        }
    ],
    "responses": {
        "200": {"description": "Package retrieved successfully"},
    },
    "400": {"description": "Invalid param"},
}
