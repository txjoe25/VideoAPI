from system.core.controller import *
class Mains(Controller):
    def __init__(self, action):
        super(Mains, self).__init__(action)
    def index(self):
        return self.load_view('main/index.html')
    def get_movie(self):
        artist = request.form['user_input'].replace(' ', '')
        url = "https://itunes.apple.com/search?term=" + artist + "&entity=musicVideo"
        # notice this is 'requests' not 'request'
        # we are using the request modules, 'get' function to send a request from our controller
        # then we use ".content" to get the content we are looking for
        response = requests.get(url).content
        # we then send the response back to our client which sent the initial post request
        return response