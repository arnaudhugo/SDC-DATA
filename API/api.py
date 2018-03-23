from bottle import run, route, get, post, response, error, abort

from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client

import json

apikey = 'YOUR_API_KEY'

gdb = GraphDatabase("http://YOUR_IP:7474/")

@error(404)
def error404(error):
    return 'Nothing here, sorry !'

# Return all music with title not null
@route('/api/<key>')
def index(key):
    response.content_type = 'application/json'
    response.headers['Access-Control-Allow-Origin'] = '*'
    if apikey == key:
        query = "MATCH (n) WHERE n.title IS NOT NULL RETURN n"
        results = gdb.query(query, data_contents=True)
        return (json.dumps(results.rows)).decode('unicode_escape')
    else:
        abort(401, "Sorry, access denied.")

# Return all genre
@route('/api/all/genre/<key>')
def all_genres(key):
    response.content_type = 'application/json'
    response.headers['Access-Control-Allow-Origin'] = '*'
    if apikey == key:
        query = "MATCH (n:Genre) RETURN n.name"
        results = gdb.query(query, data_contents=True)
        return "{ \"genres\": [" + (json.dumps(results.rows)).decode('unicode_escape').replace('[', '').replace(']', '') + "]}"
    else:
        abort(401, "Sorry, access denied.")

# Return 200 random music
@route('/api/random/<nb>/<key>')
def all_genres(nb, key):
    response.content_type = 'application/json'
    response.headers['Access-Control-Allow-Origin'] = '*'
    if apikey == key:
        query = "MATCH (g:Genre)<-[:HAS_GENRE]-(a:Artist)-[:OWNS]->(m:Music) WITH g, a, m, rand() AS number RETURN { Genre : g.name, Artist : a.name, Titre : m.title } ORDER BY number LIMIT " + nb + ""
        results = gdb.query(query, data_contents=True)
        return "{ \"random\": [" + (json.dumps(results.rows)).decode('unicode_escape').replace('[', '').replace(']', '') + "]}"
    else:
        abort(401, "Sorry, access denied.")

# Return <nb> of music by <genre>
@get('/api/genre/<genre>/<nb>/<key>')
def genre(genre, nb, key):
    response.content_type = 'application/json'
    response.headers['Access-Control-Allow-Origin'] = '*'
    genre = genre.replace('%20', ' ').replace('\'', '\\\'')
    if apikey == key:
        query = "MATCH (n:Genre {name: '" + genre + "'})<-[:HAS_GENRE]-(artist)-[:OWNS]->(music) RETURN { Artist : artist.name, Titre : music.title } LIMIT " + nb + ""
        results = gdb.query(query, data_contents=True)
        return "{ \"" + genre + "\": [" + (json.dumps(results.rows)).decode('unicode_escape').replace('[', '').replace(']', '') + "]}"
    else:
        abort(401, "Sorry, access denied.")

# Return <nb> of music by <artist>
@get('/api/artist/<artist>/<nb>/<key>')
def artist(artist, nb, key):
    response.content_type = 'application/json'
    response.headers['Access-Control-Allow-Origin'] = '*'
    artist = artist.replace('%20', ' ').replace('\'', '\\\'')
    if apikey == key:
        query = "MATCH (m:Music)<-[:OWNS]-(a:Artist {name: '" + artist + "'}) RETURN m.title LIMIT " + nb + ""
        results = gdb.query(query, data_contents=True)
        return "{ \"" + artist + "\": [" + (json.dumps(results.rows)).decode('unicode_escape').replace('[', '').replace(']', '') + "]}"
    else:
        abort(401, "Sorry, access denied.")

run(host='YOUR_IP', port=5000)
