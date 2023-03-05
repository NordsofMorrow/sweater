"""Console script for sweater."""

import click


@click.command()
def main():
    """Main entrypoint."""  # noqa: D401
    click.echo("sweater")
    click.echo("=" * len("sweater"))
    click.echo("A fabric-based remote command invoker for lazy people who do repetitive stuff")


if __name__ == "__main__":
    main()  # pragma: no cover
