# simple-api-server

A simple, boilerplate API server in Python using the Flask framework to respond to challenge requests.

## Default Endpoints

> `/`

Sending any kind of request to this endpoint will result in a text ouput:

```md
Hello, world!
```

> `/api`

`POST`ing to this endpoint any kind of JSON payload will return:

```json
{
    "challenge": "35902439"
}
```

If you send this endpoint anything other than a JSON payload or a `POST` request, it will return:

```json
{
    "error": "invalid input"
}
```

## Usage

To run, run

```bash
python app.py
```

## License

Created by Gideon Tong under the [MIT License](LICENSE.md).
