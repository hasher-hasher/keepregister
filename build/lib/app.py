import click
import datetime


@click.command()
@click.argument('file', type=click.Path(exists=True), metavar='<file_name>')
@click.argument('text', metavar='<text>')
def write(file, text):
    """This terminal app register a text with date and hour for you to keep track of your done work."""

    # Getting today's date info
    now = datetime.datetime.now()

    two_digits = lambda digit: digit if len(str(digit)) > 1 else '0{}'.format(digit)

    # Open and write input inside file
    f = open(file, "a+")
    f.write('{}/{}/{} {}:{}:{} - {}\n'.format(
        two_digits(now.day),
        two_digits(now.month),
        now.year, two_digits(now.hour),
        two_digits(now.minute),
        two_digits(now.second),
        text))
