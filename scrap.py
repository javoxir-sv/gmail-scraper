import argparse
import pathlib
from scraper.scraper import collect


def main():
    parser = argparse.ArgumentParser(
        prog="scrap.py",
        description="Scrapes the `sweet` out of your gmail.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        epilog="""
        gmail-scraper is a nice Python-based utility designed for data extraction and automation within your Gmail inbox. Provides `--query` option which supports full Gmail search query syntax for targeted data collection.
        This tool uses OAuth 2.0 for accessing Google Cloud. Spam messages are labeled as "SPAM", legit ones are "BEEF".
        But it still keeps the original labels as a backup, under `labels` key in the output/JSON file.

        """,
    )

    parser.add_argument(
        "-c",
        "--credentials",
        type=pathlib.Path,
        required=False,
        help="Path to the Google Cloud OAuth 2.0 credentials JSON file.",
    )
    parser.add_argument(
        "-t",
        "--token",
        type=pathlib.Path,
        help="Path to the authorized user token file. If not provided, one will be created.",
    )
    parser.add_argument(
        "-o",
        "--out",
        type=pathlib.Path,
        help="Path where the scraped data will be saved as a JSON file.",
    )
    parser.add_argument(
        "-p",
        "--port",
        type=int,
        default=8080,
        help="Local port to use for the OAuth authentication callback.",
    )
    parser.add_argument(
        "-q",
        "--query",
        default="newer_than:1d",
        help='Gmail search query string. See: https://ashababnoor.github.io/cheatsheets/gmail-search-syntax. For selecting all the messages use: -q "is:anywhere" or just leave it empty -q "".',
    )

    args = parser.parse_args()

    collect(
        token_path=args.token,
        creds_path=args.credentials,
        output_path=args.out,
        port=args.port,
        query=args.query,
    )


if __name__ == "__main__":
    main()
