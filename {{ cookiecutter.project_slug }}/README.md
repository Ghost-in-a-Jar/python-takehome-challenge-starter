# {{ cookiecutter.project_name }}

This is a simple traffic light simulator written in Python. It displays an ASCII representation of a traffic light and 
allows the user to specify the duration of each light color. The simulator runs until the user exits the program via a KeyboardInterrupt.

## Running with docker
Running with docker is the easiest way because you don't have to setup a python environment.

```bash
make docker-build docker-run
```

After building the image:
```bash
docker run --rm {{ cookiecutter.project_slug }} --print-delay 3
```

## Install Dependency Manager (Poetry)
    
```bash
make install-poetry
```
The installer creates a poetry wrapper in a well-known, platform-specific directory:

* `$HOME/.local/bin` on Unix.
* `%APPDATA%\Python\Scripts` on Windows.
* `$POETRY_HOME/bin` if `$POETRY_HOME` is set.
If this directory is not present in your `$PATH`, you can add it in order to invoke Poetry as poetry.

OSX example:
```bash
 echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bash_profile
```

You can run `poetry --version` to verify that the installation was successful.

## Install python dependencies

```bash
make install
```

## Usage

Run with a default of 2 seconds for each light color:
```bash
make run
```

Run with a custom duration for each light color:
```bash
poetry run start --print-delay 3
```

If you would like to activate the virtual environment created by poetry, you can run:
```bash
poetry shell
```

## Testing

```bash
make test
```

## Formatting and Linting

```bash
make format
```

```bash
make lint
```

