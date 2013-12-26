=========
 Rovi CLI
=========

::

  usage: rovicli [--version] [-v] [--log-file LOG_FILE] [-q] [-h] [--debug]

  Command line access to the Rovi API

  optional arguments:
    --version            show program's version number and exit
    -v, --verbose        Increase verbosity of output. Can be repeated.
    --log-file LOG_FILE  Specify a file to log output. Disabled by default.
    -q, --quiet          suppress output except warnings and errors
    -h, --help           show this help message and exit
    --debug              show tracebacks on errors

  Commands:
    artwork
    help           print detailed help for another command
    info episode   Get episode info
    info season    Get season info
    info video     Get video info
    search amgvideo  AMG Video search
    search music   Music search
    search video   Video search


Developing
==========

::

  $ mkvirtualenv rovicli
  $ git clone git://github.com/dasevilla/rovicli.git rovicli
  $ cd rovicli
  $ pip install -r requirements.txt
  $ python setup.py develop
  $ tox # Test source using pep8, pyflakes
