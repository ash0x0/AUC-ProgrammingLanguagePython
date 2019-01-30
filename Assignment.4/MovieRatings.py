class MovieRatings:

        def __init__(self, user_name):
            """user_name: a string representing the name of the person these movie ratings belong to"""
            self.name = user_name
            self.scores = {}

        def rate(self, movie_name, rating):
            """movie_name: a string representing a movie
                rating: a float out of ten representing this user's rating of the movie"""
            self.scores[movie_name] = float(rating)

        def get_highest_rating(self):
            """Returns a float representing the highest rating of all the movies this user has rated. Returns 0 if the user has not yet rated any movies"""
            if len(self.scores.values()) == 0:
                return 0
            else:
                return max(self.scores, key=self.scores.get)

        def __repr__(self):
            """This breaks the some big python rules but I don't care. This whole module should be taken out back and set on fire"""
            return self.name, self.scores

        def iterate_movies(self):
            """Generator for iterating over the movie rating scores for this person that yields a tuple with the movie name and its rating"""
            for i in self.scores.keys():
                yield (i, self.scores.get(i))


# container for the all the ratings
ratings = []


# it seems I have completely forgotten regex but splicing isn't so bad.
def parse_file(filename):
    # open file read only
    infile = open(filename, 'r')
    # read lines into list
    lines = infile.readlines()
    # close file
    infile.close()
    # iterate over the list of file lines
    for line in lines:
        # if the first character in the line has '-' it's a person's name
        if line[0] == '-':
            # create the person's MovieRatings object with the name on the line
            # removing the preceding '-' and succeeding ':'
            ratings.append(MovieRatings(line.strip()[1:-1]))
        # otherwise the current line has a 'MovieName: Rating' format
        else:
            # strip the line to remove whitespaces from the splicing
            line = line.strip()
            # splice the line around ':' to separate movie name and rating then insert the rating into the
            # MovieRatings object into the list
            # Note that the index -1 is merely an observation of how this loop will iterate, person then ratings
            ratings[-1].rate(line[:line.find(':')], line[line.find(':') + 1:])


def main():
    parse_file("MovieRatings.txt")

    dict = {}
    # This is packed
    # iterate over the ratings list which has MovieRatings objects
    for i in ratings:
        # iterate over each MovieRatings object using its generator, the generator yields tuples with the movie name
        # and the movie rating for the person
        for j in i.iterate_movies():
            # at this step the dictionary has the format 'MovieName: (Sum of all ratings, Number of ratings)'
            # if the movie is already in the dictionary update it
            if j[0] in dict:
                # update the movie in the dictionary by adding the newly acquired rating to the sum of previous ratings
                # (running summation) and incrementing its old count by one
                dict.update({j[0]: (dict.get(j[0])[0] + j[1], dict.get(j[0])[1] + 1)})
            # if the movie is in the dictionary insert it with a count of one
            else:
                # create a new entry with the format 'MovieName: (Rating, 1)'
                dict.update({j[0]: (j[1], 1)})
    # this loop turns the dictionary from tuples of sum and count into averages
    for i in dict:
        # get the average by getting dicing sum from the dictionary entry value tuple by count
        dict.update({i: round((dict.get(i)[0]/dict.get(i)[1]), 2)})
    # print the final dictionary which has the form 'MovieName: AverageRating'
    print(dict)


if __name__ == "__main__":
    main()

