"""setMyName json schema"""
valid_schema = {
  "type": "object",
  "properties": {
    "ok": {
      "type": "boolean"
    },
    "result": {
      "type": "boolean"
    }
  },
  "required": [
    "ok",
    "result"
  ]
}
