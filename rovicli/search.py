import logging

from roviclient.search import SearchApi
from dateutil import parser as date_parser

from main import RoviCommand


class BaseSearch(RoviCommand):
    """
    Show a list of files in the current directory.

    The file name and size are printed by default.
    """

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(BaseSearch, self).get_parser(prog_name)
        parser.add_argument('query')
        return parser


class AmgVideoSearch(BaseSearch):

    def get_description(self):
        return 'AMG Video search'

    def get_parser(self, prog_name):
        parser = super(AmgVideoSearch, self).get_parser(prog_name)
        parser.add_argument('-t', '--entity-type', required=True,
                            choices=['movie', 'tvseries', 'credit'])
        return parser

    def take_action(self, parsed_args):
        rovi = SearchApi(parsed_args.api_key, parsed_args.api_secret)
        print parsed_args.api_key, parsed_args.api_secret
        r = rovi.amg_video_search(parsed_args.entity_type, parsed_args.query)
        items = r.json()['searchResponse']['results']

        def convert(items):
            for item in items:
                yield (
                    item['movie']['ids']['cosmoId'],
                    item['movie']['title'],
                    item['movie']['releaseYear'],
                )

        columns = (
            'cosmos_id',
            'title',
            'release_year',
        )
        data = convert(items)

        return (columns, data)


class MusicSearch(BaseSearch):

    def get_description(self):
        return 'Music search'

    def take_action(self, parsed_args):
        rovi = SearchApi(parsed_args.api_key, parsed_args.api_secret)
        r = rovi.music_search(parsed_args.entity_type, parsed_args.query)
        items = r.json()['searchResponse']['results']

        def convert(items):
            for item in items:
                yield (
                    item['movie']['ids']['cosmoId'],
                    item['movie']['title'],
                    item['movie']['releaseYear'],
                )

        columns = (
            'cosmos_id',
            'title',
            'release_year',
        )
        data = convert(items)

        return (columns, data)


class VideoSearch(BaseSearch):

    def get_description(self):
        return 'Video search'

    def get_parser(self, prog_name):
        parser = super(VideoSearch, self).get_parser(prog_name)
        parser.add_argument('-t', '--entity-type', required=True,
                            choices=['movie', 'tvseries', 'onetimeonly'])
        return parser

    def take_action(self, parsed_args):
        rovi = SearchApi(parsed_args.api_key, parsed_args.api_secret)
        r = rovi.video_search(parsed_args.entity_type, parsed_args.query)
        items = r.json()['searchResponse']['results']

        def convert(items):
            for item in items:
                video_result = item['video']

                item_id = video_result['ids']['cosmoId']

                item_release_year = video_result.get('releaseYear')
                if item_release_year is None:
                    air_date = video_result.get('originalAirDate')
                    if air_date is not None:
                        parsed_air_date = date_parser.parse(air_date)
                        item_release_year = parsed_air_date.year

                item_title = video_result.get('title')
                if item_title is None:
                    item_title = video_result.get('masterTitle')

                yield (
                    item_id,
                    item_title,
                    item_release_year,
                )

        columns = (
            'cosmos_id',
            'title',
            'release_year',
        )
        data = convert(items)

        return (columns, data)
