import argparse, glob, os, json, re, datetime
from pysolr import Solr

date_pattern=re.compile("@\\d+@")



conn = Solr('http://127.0.0.1:8983/solr/')

if __name__ == '__main__':
    filenames=glob.glob('example/blog/*.json')
    documents=[]
    for filename in filenames:
        path, id= os.path.split(filename)
        parsed=json.loads(file(filename).read())
        parsed['path']=path
        parsed['id']=id
        for key in parsed:
            value=parsed[key]
            if value.startswith('@') and date_pattern.match(value):
                timestamp=int(value[1:-1])
                parsed[key]=datetime.datetime.fromtimestamp(timestamp)
        documents.append(parsed)
        
    print documents
    conn.add(documents)
        