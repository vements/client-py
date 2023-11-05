## Vements Client Library for Python

The Vements Client Library for Python is a Python library for accessing the Vements API.  It also includes a command line tool that can be used to interact with the API in scripts or in a terminal.


### Documentation

See the [Python API docs]() for more information on how to use this library.

### Installation

To install the Vements Client Library for Python, use the following command:

```bash
$ pip install vements
```

### Build 

There is no separate build step for the Python CLI tool, but you can simplify access with an alias:

```bash
$ alias vements='python -m vements'
```

### Usage 

The following example shows how to use the Vements Client Library for Python to create a new Vements client, and then use that client to create a new Vements scoreboard.

```python
import vements

client = vements.Client()
scoreboard = client.scoreboard.create(display="My Scoreboard", rank_dir="desc", public=False)
```

### Command Line Tool

The Python CLI tool supports all of the same operations as the CLI tool in other languages:

* achievement CRUD, list, leaderboard, record progress
* participant CRUD, list, progress, scores
* scoreboard CRUD, list, scoreboard, record score

The above commands all support the following options:

* `--api-key` to specify the API key
* `--verbose` to show verbose output

In addition to resource commands, these common commands are also supported:

* `api-version` to show the API version
* `client-version` to show the client library version

The library and CLI both support the following environment variables:

* `API_KEY` to specify the API key
* `SERVER_TAGS` to specify the tags used to select the server URL
