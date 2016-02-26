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

Copy the provided `config.yaml.dist` to `config.yaml` and edit according to your needs.

- `global.github_api_token`: Optionally set the value of this key to a valid Github API token. Without a token, you might run into rate limits when using Seismograph frequently.
- `projects`: For each software project you want to track, add one key here. Name this key however you want, but make sure it's unique within this file.
- `projects.<project>.github`: This key is required per project. The value must be a string composed of the user or organization name, then a forward slash, then the actual repository name. For example, the [Bootstrap](https://github.com/twbs/bootstrap) repository would get the value `twbs/bootstrap`.

Example:

```yaml
global:
  github_api_token: 3kg476foba34zby9e8hpa83f4
projects:
  firstproject:
    github: giantswarm/kocho
  otherproject:
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
  forks: 0
  network: 0
  open_issues: 16
  stargazers: 48
  watchers: 48
mayu:
  forks: 1
  network: 1
  open_issues: 13
  stargazers: 34
  watchers: 34
```

## Future Plans

- Gather statistics from additional sources, like StackOverflow, IRC, Google Groups
- GitHub: Count commits, issues overall, pull requests
