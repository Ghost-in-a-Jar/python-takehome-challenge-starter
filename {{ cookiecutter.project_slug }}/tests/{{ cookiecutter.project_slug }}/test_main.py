from click.testing import CliRunner
from main import main
from testfixtures import log_capture, LogCapture  # type: ignore


@log_capture()
def test_main_default_args(log_capture: LogCapture):
    runner = CliRunner()

    result = runner.invoke(main)
    assert result.exit_code == 0
    log_capture.check(
        (
            "{{ cookiecutter.project_slug }}.main",
            "INFO",
            "Hello World",
        )
    )

@log_capture()
def test_main_args(log_capture: LogCapture):
    runner = CliRunner()

    result = runner.invoke(main, ["--print-delay", "3"])
    assert result.exit_code == 0
    log_capture.check(
        (
            "{{ cookiecutter.project_slug }}.main",
            "INFO",
            "Hello World",
        )
    )