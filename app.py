from flask import Flask, request, jsonify
from flasgger import Swagger
from imdb import IMDb
from utils import get_movie_details

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False
app.debug = True

swagger = Swagger(app)

@app.route('/hello_world', methods=['GET','POST'])
def say_hello():
    '''
    this is test route for flask app
    '''
    return "Hello World!"

@app.route('/get_movie_details')
def movie_details():
    """
    API route to get Movie Details
    ---
    tags:
      - Get Imdb Ratings of the Movie
    parameters:
        - name: Movie
          in: query
          type: string
          required: true
          description: Enter Movie name as same as in IMDb website
    responses:
      500:
        description: Error Please enter the correct movie name as same as in Imdb website!
      200:
        description: Movie Details
        schema:
          id: Movie details (API Response)
          properties:
            Title:
              type: string
              description: The movie title
              default: 'NA'
            Rating:
              type: number
              format: float
              description: The movie rating
              default: 'NA'
            Director:
              type: string
              description: The movie director
              default: 'NA'
            Cast:
              type: string
              description: The movie cast
              default: 'NA'
            Music_Director:
              type: string
              description: The music director
              default: 'NA'
            Genre:
              type: string
              description: The movie genre
              default: 'NA'
            Language:
              type: string
              description: The movie language
              default: 'NA'
            Kind:
              type: string
              description: The movie kind
              default: 'NA'
            Box_Office:
              type: string
              description: The movie box-office
              default: 'NA'
            # Plot:
            #   type: string
            #   description: The movie plot
            #   default: 'NA'
            # Plot_Outline:
            #   type: string
            #   description: The movie plot-outline
            #   default: 'NA'
            # Synopsis:
            #   type: string
            #   description: The movie Synopsis
            #   default: 'NA'
    """

    ia = IMDb()

    movie_name = request.args.get("Movie")

    print("movie name - ", movie_name)

    movie_names = ia.search_movie(movie_name)
    movie_id = movie_names[0].movieID
    print("movie id - ", movie_id)

    update_movie = movie_names[0]
    ia.update(update_movie)
    rating = update_movie.get('rating')
    print('This movie ratings ', rating)

    movie = ia.get_movie(movie_id, info=['taglines', 'plot', 'main'])

    movie_details_obj = get_movie_details.GetMovieDetails(movie)
    movie_details_dict = movie_details_obj.movie_details()

    box_office = movie_details_dict['box_office']
    languages = movie_details_dict['languages']
    genres = movie_details_dict['genres']
    cast = movie_details_dict['cast']
    director = movie_details_dict['director']
    composers = movie_details_dict['composers']
    synopsis = movie_details_dict['synopsis']
    plot = movie_details_dict['plot']
    kind = movie_details_dict['kind']
    title = movie_details_dict['title']
    plot_outline = movie_details_dict['plot_outline']
    cover_url = movie_details_dict['cover_url']

    print("* " * 20)


    return jsonify(Title=title,
                   Rating=rating,
                   Director=director,
                   Cast=cast,
                   Music_Director=composers,
                   Genre=genres,
                   Language=languages,
                   Kind=kind,
                   Box_Office=box_office,
                   # _="---  Plot  ---",
                   # Plot=plot,
                   # __="---  Plot Outline  ---",
                   # Plot_Outline=plot_outline,
                   # ___="---  synopsis  ---",
                   # Synopsis = synopsis
                   )

if __name__  == '__main__':
    # app.config["JSON_SORT_KEYS"] = False
    app.debug = True
    app.run(host="0.0.0.0",port=5777)
    #http://localhost:5777/apidocs/#/get_movie_details