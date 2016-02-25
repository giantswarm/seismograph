# seismograph

Utilities for gathering traction metrics around open source projects

## Installation

Optionally, create and active a virtual python environment.

```nohighlight
$ virtualenv venv
$ source venv/bin/activate
```

Install required python libraries:

```nohighlight
$ pip install -r requirements.txt
```

## Configuration

Copy the provided `config.yaml.dist` to `config.yaml` and edit to your needs. Then edit `config.yaml` according to your needs.

- `global.github_api_token`: Optionally set the value of this key to a valid Github API token. Without a token, you might run into rate limits when using Seismograph frequently.
- `global.projects`: For each software project you want to track, add one key here. Name this key however you want, but make sure it's unique within this file.
- `global.projects.<project>.github`: This key is required per project. The value must be a string composed of the user or organization name, then a forward slash, then the actual repository name. For example, the [Bootstrap](https://github.com/twbs/bootstrap) repository would get the value `twbs/bootstrap`.

Example:

```yaml
global:
  github_api_token: 3kg476foba34zby9e8hpa83f4
projects:
  firstproject
    github: giantswarm/kocho
  otherproject
    github: giantswarm/mayu
```

## Usage

Simply execute the python script like this:

```nohighlight
$ python fetch.py
```

As a result, you will see statistics printed in YAML-compatible format to standard output.

Example:

```yaml
kocho:
  forks_count: 0
  network_count: 0
  open_issues_count: 16
  stargazers_count: 48
  watchers_count: 48
mayu:
  forks_count: 1
  network_count: 1
  open_issues_count: 13
  stargazers_count: 34
  watchers_count: 34
```
