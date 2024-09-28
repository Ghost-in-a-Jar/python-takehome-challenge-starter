import logging
import time

import click

@click.command()
@click.option(
    "--print-delay",
    default=2,
    help="Delay in seconds before printing Hello World",
)
def main(
    print_delay: int,
):
    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger(__name__)

    time.sleep(print_delay)
    log.info("Hello World")


if __name__ == "__main__":
    main()
