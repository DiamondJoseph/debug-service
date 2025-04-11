[![CI](https://github.com/DiamondJoseph/debug_service/actions/workflows/ci.yml/badge.svg)](https://github.com/DiamondJoseph/debug_service/actions/workflows/ci.yml)
[![Coverage](https://codecov.io/gh/DiamondJoseph/debug_service/branch/main/graph/badge.svg)](https://codecov.io/gh/DiamondJoseph/debug_service)

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0)

# service

Test service for demonstrating debug options for a PR to [the python-copier-template](https://github.com/DiamondLightSource/python-copier-template/pull/251).

This service is configured with two endpoints: a `healthz` endpoint used by Kubernetes and a `test` endpoint which is purposefully broken to demonstrate debugging and testing on the cluster.

The example values.yaml in the root of this repository, when configured with your account details, deploys the broken version of the app. Connect to a devcontainer from a local vscode instance, make a fix internal to the cluster and push the changes to this repository.

Source          | <https://github.com/DiamondJoseph/debug_service>
:---:           | :---:
Docker          | `docker run ghcr.io/diamondjoseph/debug_service:latest`
Releases        | <https://github.com/DiamondJoseph/debug_service/releases>
