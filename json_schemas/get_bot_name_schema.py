"""getMyName json schema"""
valid_schema = {
  "type": "object",
  "properties": {
    "ok": {
      "type": "boolean"
    },
    "result": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        }
      },
      "required": [
        "name"
      ]
    }
  },
  "required": [
    "ok",
    "result"
  ]
}
