"""sendMessage json schema"""
valid_schema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "ok": {
      "type": "boolean"
    },
    "result": {
      "type": "object",
      "properties": {
        "message_id": {
          "type": "integer"
        },
        "from": {
          "type": "object",
          "properties": {
            "id": {
              "type": "integer"
            },
            "is_bot": {
              "type": "boolean"
            },
            "first_name": {
              "type": "string"
            },
            "username": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "is_bot",
            "first_name",
            "username"
          ]
        },
        "chat": {
          "type": "object",
          "properties": {
            "id": {
              "type": "integer"
            },
            "first_name": {
              "type": "string"
            },
            "last_name": {
              "type": "string"
            },
            "username": {
              "type": "string"
            },
            "type": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "first_name",
            "last_name",
            "username",
            "type"
          ]
        },
        "date": {
          "type": "integer"
        },
        "text": {
          "type": "string"
        }
      },
      "required": [
        "message_id",
        "from",
        "chat",
        "date",
        "text"
      ]
    }
  },
  "required": [
    "ok",
    "result"
  ]
}
