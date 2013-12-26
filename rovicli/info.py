import logging

from roviclient.video import VideoApi

from main import RoviCommand


class BaseInfo(RoviCommand):
    """Show details about a file"""

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(BaseInfo, self).get_parser(prog_name)
        parser.add_argument('cosmoid')
        return parser

    def _find_artwork(self, format_id, images):
        for image in images:
            if image['formatid'] == format_id:
                return image['url']
        return None

    def take_action(self, parsed_args):
        pass


class VideoInfo(BaseInfo):

    def get_description(self):
        return 'Get video info'

    def take_action(self, parsed_args):
        rovi = VideoApi(parsed_args.api_key, parsed_args.api_secret)
        r = rovi.video_info(cosmoid=parsed_args.cosmoid,
                            include='synopsis,images')
        video_detail = r.json()['video']

        columns = ('cosmosid',
                   'title',
                   'synopsis',
                   'image_url',
                   'release_year',
                   )

        data = (video_detail['ids']['cosmoId'],
                video_detail['masterTitle'],
                video_detail['synopsis']['synopsis'],
                self._find_artwork(57, video_detail['images']),
                video_detail['releaseYear'],
                )
        return (columns, (data,))


class EpisodeInfo(BaseInfo):

    def get_description(self):
        return 'Get episode info'

    def get_parser(self, prog_name):
        parser = super(EpisodeInfo, self).get_parser(prog_name)
        parser.add_argument('-s', '--season', help='season', type=int, required=True)
        parser.add_argument('-e', '--episode', help='episode', type=int, required=True)
        return parser

    def take_action(self, parsed_args):
        rovi = VideoApi(parsed_args.api_key, parsed_args.api_secret)
        r = rovi.episode_info(cosmoid=parsed_args.cosmoid,
                              season=parsed_args.season,
                              episode=parsed_args.episode,
                              include='synopsis,images')
        video_detail = r.json()['video']

        columns = ('cosmosid',
                   'title',
                   'synopsis',
                   'image_url',
                   )

        data = (video_detail['ids']['cosmoId'],
                video_detail['masterTitle'],
                video_detail['synopsis']['synopsis'],
                self._find_artwork(57, video_detail['images']),
                )
        return (columns, (data,))


class SeasonInfo(BaseInfo):

    def get_description(self):
        return 'Get season info'

    def get_parser(self, prog_name):
        parser = super(SeasonInfo, self).get_parser(prog_name)
        parser.add_argument('-s', '--season', help='season', type=int, required=True)
        return parser

    def take_action(self, parsed_args):
        rovi = VideoApi(parsed_args.api_key, parsed_args.api_secret)
        r = rovi.season_info(cosmoid=parsed_args.cosmoid,
                             season=parsed_args.season,
                             include='all')

        episodes = r.json()['episodes']

        columns = ('cosmosid',
                   'episode title',
                   )

        data = []
        for episode in episodes:
            data.append((
                episode['ids']['cosmoId'],
                episode.get('title'),
            ))
        return (columns, data)


class ArtworkInfo(BaseInfo):
    def take_action(self, parsed_args):
        rovi = VideoApi(parsed_args.api_key, parsed_args.api_secret)
        r = rovi.images(cosmoid=parsed_args.cosmoid)
        images = r.json()['images']

        columns = (
            'author',
            'copyright_owner',
            'format_id',
            'url',
            'height',
            'width',
        )

        data = ((image['author'], image['copyrightOwner'], image['formatid'], image['url'], image['height'], image['width']) for image in images)
        return (columns, data)
