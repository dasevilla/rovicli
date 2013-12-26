from setuptools import setup, find_packages


with open('README.rst') as fp:
    long_description = fp.read()


setup(
    name='rovicli',
    version='0.1.0',

    description='Command line access to the Rovi API',
    long_description=long_description,

    author='Devin Sevilla',
    author_email='dasevilla@gmail.com',

    url='https://github.com/dasevilla/rovicli',
    download_url='https://github.com/dasevilla/rovicli/tarball/master',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Environment :: Console',
    ],

    install_requires=[
        'cliff',
        'cliff-tablib',
        'roviclient',
    ],

    packages=find_packages(),

    entry_points={
        'console_scripts': [
            'rovicli = rovicli.main:main',
        ],
        'rovicli': [
            'search_amgvideo = rovicli.search:AmgVideoSearch',
            'search_video = rovicli.search:VideoSearch',
            'search_music = rovicli.search:MusicSearch',
            'artwork = rovicli.info:ArtworkInfo',
            'info_video = rovicli.info:VideoInfo',
            'info_episode = rovicli.info:EpisodeInfo',
            'info_season = rovicli.info:SeasonInfo',
        ],
    },
)
