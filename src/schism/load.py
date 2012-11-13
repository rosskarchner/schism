import argparse, glob, os, json
from pysolr import Solr

conn = Solr('http://127.0.0.1:8983/solr/')

if __name__ == '__main__':
    filenames=glob.glob('example/blog/*.json')
    documents=[]
    for filename in filenames:
        path, id= os.path.split(filename)
        parsed=json.loads(file(filename).read())
        parsed['path']=path
        parsed['id']=id
        documents.append(parsed)
        
    print documents
    conn.add(documents)
        