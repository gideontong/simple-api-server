# simple-api-server

A simple API server in Python to respond to challenge requests. Essentially boilerplate, but it will respond to

```json
{
    "challenge": "data"
}
```

with `1` appended to the end like so:

```json
{
    "challenge": "data1"
}
```

and respond to everything else with the fields replaced with `data`.

## Usage

To run, run

```bash
python app.py
```

## License

Created by Gideon Tong under the MIT License.
