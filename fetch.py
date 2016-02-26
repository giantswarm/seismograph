import yaml
import github
import json
import sys

def parse_yaml(path):
    with open(path, "r") as handle:
        content = handle.read()
        data = yaml.load(content, Loader=yaml.Loader)
        return data


def github_stats(client, organization, repository_name):
    github_org = g.get_organization(organization)
    repo = github_org.get_repo(repository_name)
    stats = {
        "forks": repo.forks_count,
        "network": repo.network_count,
        "open_issues": repo.open_issues_count,
        "stargazers": repo.stargazers_count,
        "watchers": repo.watchers_count
    }
    return stats

if __name__ == "__main__":
    config = parse_yaml("./config.yaml")

    output = {}

    g = None
    if config['global']['github_api_token'] is not None:
        g = github.Github(config['global']['github_api_token'])
    else:
        g = github.Github()

    for key in config['projects']:
        orgname, projectname = config['projects'][key]["github"].split("/", 1)
        output[key] = github_stats(g, orgname, projectname)

    print(yaml.dump(output, default_flow_style=False))
