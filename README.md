# meltano_parameter_maintainer
A python application to maintain SSM Parameters in AWS for the purpose of the Meltano ELT tool.

[![Open in Visual Studio Code](https://open.vscode.dev/badges/open-in-vscode.svg)](https://open.vscode.dev/s7clarke10/meltano_parameter_maintainer)

## How to use it

TBA

## Usage

This section dives into basic usage of `meltao_parameter_maintainer` by walking through the process
of adding and maintainign parameters. It assumes that you have a knowledge of AWS and specifically the AWS SSM Parameter Store.

### Install

First, make sure Python 3 is installed on your system or follow these
installation instructions for [Mac](http://docs.python-guide.org/en/latest/starting/install3/osx/) or
[Ubuntu](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-ubuntu-16-04).

It's recommended to use a virtualenv:

```bash
  python3 -m venv venv
  pip install pipelinewise-tap-mssql
```

or

```bash
  python3 -m venv venv
  . venv/bin/activate
  pip install --upgrade pip
  pip install .
```
