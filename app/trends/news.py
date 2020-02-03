class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,movie_id,title,overview,poster,vote_average,vote_count):
        self.movie_id = movie_id
        self.title = title
        self.overview = overview
        self.poster = 'https://image.tmdb.org/t/p/w500/'+ str(poster)
        self.vote_average = vote_average
        self.vote_count = vote_count