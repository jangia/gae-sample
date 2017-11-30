from google.appengine.ext import ndb


class Sporocilo(ndb.Model):
    vnos = ndb.StringProperty()
    nastanek = ndb.DateTimeProperty(auto_now_add=True)