yt-param-fetch
====
Simple module to get parameters from a youtube URL. Works on standard, non-standard, and shortened links. Currently
does not handle attribution links correctly.

Example
----
```
Python 3.7.1
Type "help", "copyright", "credits" or "license" for more information.

>>> # Using the module to build the dictionary.
>>> from  youtube_handler import YoutubeHandler
>>> yt = YoutubeHandler()
>>> url_params = yt.get_video_params('https://www.youtube.com/watch?v=y9eFk8TuV9k&feature=youtu.be&t=2925')
>>> print(url_params)

{'v=': 'y9eFk8TuV9k', 'feature=': 'youtu.be', 't=': '2925'}

>>> # Acquiring a video ID.
>>> video_id = url_params['v=']
>>> print(video_id)

y9eFk8TuV9k
```