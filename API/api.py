from bottle import run, route, get, post, response

from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client

import json

gdb = GraphDatabase("http://172.16.1.171:7474/")

# Return all music with title not null
@route('/api/')
def index():
    response.content_type = 'application/json'
    query = "MATCH (n) WHERE n.title IS NOT NULL RETURN n"
    results = gdb.query(query, data_contents=True)
    return (json.dumps(results.rows)).decode('unicode_escape')

# Return all genre
@route('/api/all/genre/')
def all_genres():
    response.content_type = 'application/json'
    query = "MATCH (n:Genre) RETURN n.name"
    results = gdb.query(query, data_contents=True)
    return "{ \"genres\": [" + (json.dumps(results.rows)).decode('unicode_escape').replace('[', '').replace(']', '') + "]}"

# Return 200 random music
@route('/api/random/')
def all_genres():
    response.content_type = 'application/json'
    query = "MATCH (g:Genre)<-[:HAS_GENRE]-(a:Artist)-[:OWNS]->(m:Music) WITH g, a, m, rand() AS number RETURN { Genre : g.name, Artist : a.name, Titre : m.title } ORDER BY number LIMIT 200"
    results = gdb.query(query, data_contents=True)
    return "{ \"random\": [" + (json.dumps(results.rows)).decode('unicode_escape').replace('[', '').replace(']', '') + "]}"

# Return <nb> of music by <genre>
@get('/api/genre/<genre>/<nb>')
def genre(genre, nb):
    response.content_type = 'application/json'
    genre = genre.replace('%20', ' ').replace('\'', '\\\'')
    query = "MATCH (n:Genre {name: '" + genre + "'})<-[:HAS_GENRE]-(artist)-[:OWNS]->(music) RETURN { Artist : artist.name, Titre : music.title } LIMIT " + nb + ""
    results = gdb.query(query, data_contents=True)
    return "{ \"" + genre + "\": [" + (json.dumps(results.rows)).decode('unicode_escape').replace('[', '').replace(']', '') + "]}"

# Return <nb> of music by <artist>
@get('/api/artist/<artist>/<nb>')
def artist(artist, nb):
    response.content_type = 'application/json'
    artist = artist.replace('%20', ' ').replace('\'', '\\\'')
    query = "MATCH (m:Music)<-[:OWNS]-(a:Artist {name: '" + artist + "'}) RETURN m.title LIMIT " + nb + ""
    results = gdb.query(query, data_contents=True)
    return "{ \"" + artist + "\": [" + (json.dumps(results.rows)).decode('unicode_escape').replace('[', '').replace(']', '') + "]}"

run(host='172.16.1.171', port=5000)
