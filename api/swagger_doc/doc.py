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

get_dns_records_ep_doc = {
    "summary": "Gets all DNS records data from Firebase",
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
        "404": {"description": "Data not found"},
    },
}

get_dns_record_ep_doc = {
    "summary": "Get a DNS record data from Firebase",
    "parameters": [
        {
            "name": "param",
            "in": "path",
            "type": "string",
            "description": "Domain name",
            "example": "google.com",
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

post_dns_record_ep_doc = {
    "summary": "Post a new DNS record data to Firebase",
    "parameters": [
        {
            "in": "body",
            "name": "data",
            "description": "New Json record data",
            "required": True,
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
        }
    ],
}

put_dns_record_ep_doc = {
    "summary": "Updates a DNS record data to Firebase",
    "parameters": [
        {
            "name": "param",
            "in": "path",
            "type": "string",
            "description": "Domain name",
            "example": "google.com",
            "required": True,
        },
        {
            "in": "body",
            "name": "data",
            "description": "New record data to be updated",
            "required": True,
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
    ],
}

delete_dns_record_ep_doc = {
    "summary": "Deletes a DNS record data to Firebase",
    "parameters": [
        {
            "name": "param",
            "in": "path",
            "type": "string",
            "description": "Domain name",
            "example": "google.com",
            "required": True,
        },
    ],
}

get_dns_global_ep_doc = {
    "summary": "Get all DNS global document from Firestore that matches the code",
    "parameters": [
        {
            "name": "param",
            "in": "path",
            "type": "string",
            "description": "Country Code",
            "example": "DE",
            "required": True,
        }
    ],
    "responses": {
        "200": {
            "description": "Data retrieved successfully",
            "schema": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "string",
                        "example": "001NzhiUybsGfShYxuqh",
                    },
                    "from": {
                        "type": "string",
                        "example": "0.0.0.0",
                    },
                    "to": {
                        "type": "string",
                        "example": "255.255.255.255",
                    },
                    "to": {
                        "type": "string",
                        "example": "DE",
                    },
                },
            },
        },
        "400": {"description": "Invalid param"},
        "404": {"description": "Data not found"},
    },
}
