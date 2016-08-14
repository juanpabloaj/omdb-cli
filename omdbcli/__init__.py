# -*- coding: utf-8 -*-
import omdb
import argparse


def show_search(search):
    results = omdb.search(search)

    keys = ['title', 'year', 'runtime', 'imdb_id']
    for result in results:

        fields = [result[key] for key in keys if key in result.keys()]

        print(*fields, sep='\t')


def show_request_by_imdb_id(imdb_id):
    res = omdb.request(i=imdb_id)
    print(res.json())


def show_request_by_title(title):
    res = omdb.request(t=title)
    print(res.json())


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-s', '--search', type=str, default=None,
        help='Search a string in omdb'
    )

    parser.add_argument(
        '-i', '--imdb', type=str, default=None,
        help='Search by imdb ID in omdb'
    )

    parser.add_argument(
        '-t', '--title', type=str, default=None,
        help='Search by title in omdb'
    )

    args = parser.parse_args()

    if args.search:
        show_search(args.search)
    elif args.imdb:
        show_request_by_imdb_id(args.imdb)
    elif args.title:
        show_request_by_title(args.title)

if __name__ == '__main__':
    main()
