import unittest
from yt_param_fetch.youtube_handler import YoutubeHandler


class TestGetVideoParameterMethod(unittest.TestCase):
    yt = YoutubeHandler()

    def test_standard_url_format(self):
        self.assertEqual(self.yt.get_video_params('https://www.youtube.com/watch?v=Erpj23v9CAk&feature=youtu.be&t=1152'),
                         {'v=': 'Erpj23v9CAk', 'feature=': 'youtu.be', 't=': '1152'})

    def test_clean_url_format(self):
        self.assertEqual(self.yt.get_video_params('https://youtu.be/oTJRivZTMLs?list=PLToa5JuFMsXTNkrLJbRlB--76IAOjRM9b'),
                         {'v=': 'oTJRivZTMLs', 'list=': 'PLToa5JuFMsXTNkrLJbRlB--76IAOjRM9b'})

    def test_vi_url_format(self):
        self.assertEqual(self.yt.get_video_params('http://youtube.com/vi/dQw4w9WgXcQ'),
                         {'v=': 'dQw4w9WgXcQ'})

    def test_v_url_format(self):
        self.assertEqual(self.yt.get_video_params('http://www.youtube-nocookie.com/v/6L3ZvIMwZFM?version=3&hl=en_US&rel=0'),
                         {'v=': '6L3ZvIMwZFM', 'version=': '3', 'hl=': 'en_US', 'rel=': '0'})

    def test_short_url_format(self):
        self.assertEqual(self.yt.get_video_params('https://youtu.be/W9CLdkkNn20'),
                         {'v=': 'W9CLdkkNn20'})


if __name__ == 'main':
    unittest.main()
