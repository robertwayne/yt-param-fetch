import re


class YoutubeHandler:

    @staticmethod
    def get_video_params(url):
        """Takes a youtube video URL (except attribution links) and returns a dictionary with each URL parameter.

        Keyword arguments:
            url -- a youtube url
        """
        regex_pattern = re.compile(r'(?<=\?)(.+?)(?=&|\Z)|'
                                   r'(?<=&)(.+?)(?=&)|'
                                   r'(?<=/vi/)(.+?)(?=\?|\Z)|'
                                   r'(?<=/v/)(.+?)(?=\?|\Z)|'
                                   r'(?<=&)(.*)(?!=\Z)|'
                                   r'(?<=\.be/)(.?)(?=&)|'
                                   r'(?<=\.be/)(.+?)(?=\?)|'
                                   r'(?<=\?)(.+?)(?=\?|\Z)|'
                                   r'(?<=\?)(.*)(?!=\Z)|'
                                   r'(?<=\.be/)(.*)')
        video_params = regex_pattern.findall(f'{url}')

        # flattens the regex result and removes empty string
        cleaned_video_params = list(filter(None, [item for sublist in video_params for item in sublist]))

        video_params_dict = {}
        for param in cleaned_video_params:
            param_pattern = re.compile(r'(.+)(?<=/)|(?!==)(.*=)')
            param_id_pattern = re.compile(r'=(.*)')

            param_type = param_pattern.search(param)
            param_id = param_id_pattern.search(param)

            # forces the param_type for non-standard URL's using /v/, /vi/ or /
            if param_type is None or param_id is None:
                cleaned_param_type = 'v='
                cleaned_param_id = param
            else:
                cleaned_param_type = param_type.group()
                cleaned_param_id = param_id.group(1)

            video_params_dict[cleaned_param_type] = video_params_dict.get(cleaned_param_type, cleaned_param_id)

        return video_params_dict
