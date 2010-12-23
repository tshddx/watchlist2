import os,struct,urllib,urllib2,xml.etree.cElementTree as ElementTree

config = {}
config['apikey'] = "3e7807c4a01f18298f64662b257d7059"
config['urls'] = {}
config['urls']['person.getInfo'] = "http://api.themoviedb.org/2.1/Person.getInfo/en/xml/%(apikey)s/%%s" % (config)

class TmdBaseError(Exception):
    pass

class TmdNoResults(TmdBaseError):
    pass

class TmdHttpError(TmdBaseError):
    pass

class TmdXmlError(TmdBaseError):
    pass

class XmlHandler:
    """Deals with retrieval of XML files from API"""
    def __init__(self, url):
        self.url = url

    def _grabUrl(self, url):
        try:
            urlhandle = urllib2.urlopen(url)
        except IOError, errormsg:
            raise TmdHttpError(errormsg)
        if urlhandle.code >= 400:
            raise TmdHttpError("HTTP status code was %d" % urlhandle.code)
        return urlhandle.read()

    def getEt(self):
        xml = self._grabUrl(self.url)
        try:
            et = ElementTree.fromstring(xml)
        except SyntaxError, errormsg:
            raise TmdXmlError(errormsg)
        return et

def parsePerson(person_element):
    cur_person = {}
    for item in person_element.getchildren():
        if item.tag.lower() == "name":
            cur_person['name'] = item.text
        if item.tag.lower() == "id":
            cur_person['id'] = item.text
    return cur_person
    
# def search(self, title):
#     """Searches for a film by its title.
#     Returns SearchResults (a list) containing all matches (Movie instances)
#     """
#     title = urllib.quote(title.encode("utf-8"))
#     url = config['urls']['movie.search'] % (title)
#     etree = XmlHandler(url).getEt()
#     search_results = SearchResults()
#     for cur_result in etree.find("movies").findall("movie"):
#         cur_movie = self._parseSearchResults(cur_result)
#         search_results.append(cur_movie)
#     return search_results
    
def getPersonInfo(id):
    """Returns person info by his or her TheMovieDb ID.
    Returns a dictionary
    """
    url = config['urls']['person.getInfo'] % (id)
    etree = XmlHandler(url).getEt()
    PersonsTree = etree.find("people").findall("person")

    if len(PersonsTree) == 0:
        raise TmdNoResults("No results for id %s" % id)
    return parsePerson(PersonsTree[0])
