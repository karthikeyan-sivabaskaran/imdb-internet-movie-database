
class GetMovieDetails(object):

    def __init__(self,movie):
        self.movie = movie

    def get_details(self,info_type):
        return self.movie.get(info_type)

    def movie_details(self):

        movie_details = {}

        movie_details['box_office'] = ', '.join('-' if self.get_details('box office') is None else {k + " - " + v for k, v in self.get_details('box office').items()})

        movie_details['languages'] = ', '.join('-' if self.get_details('languages') is None else self.get_details('languages'))

        movie_details['genres'] = ', '.join('-' if self.get_details('genres') is None else self.get_details('genres'))

        movie_details['cast'] = ', '.join('-' if self.get_details('cast') is None else [i['name'] for i in list(self.get_details('cast'))])

        movie_details['director'] = '-' if self.get_details('director') is None else self.get_details('director')[0]['name']

        movie_details['composers'] = '-' if self.get_details('composers') is None else self.get_details('composers')[0]['name']

        movie_details['synopsis'] = '-' if self.get_details('synopsis') is None else self.get_details('synopsis')[0]

        movie_details['plot'] = '-' if self.get_details('plot') is None else self.get_details('plot')[0]

        movie_details['kind'] = '-' if self.get_details('kind') is None else self.get_details('kind')

        movie_details['title'] = '-' if self.get_details('title') is None else self.get_details('title')

        movie_details['plot_outline'] = '-' if self.get_details('plot outline') is None else self.get_details('plot outline')

        movie_details['cover_url'] = '-' if self.get_details('cover url') is None else self.get_details('cover url')

        return movie_details
