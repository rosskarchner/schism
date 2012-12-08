import argparse
import glob
import os
import json
import re
import datetime
from resolver import resolve

date_pattern = re.compile("@\\d+@")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='load a Schism document store into Solr')
    parser.add_argument('configuration',
                        metavar='CONFIG',
                        help='a Resolver statement pointing to a SchismSite')
    args = parser.parse_args()
    site = resolve(args.configuration)
    filenames = site.list_objects('.json')
    documents = []
    for filename in filenames:
        path, id = os.path.split(filename)
        import pdb;pdb.set_trace()
        parsed = json.loads(file(filename).read())
        parsed['path'] = path
        parsed['id'] = id
        for key in parsed:
            value = parsed[key]
            if value.startswith('@') and date_pattern.match(value):
                timestamp = int(value[1:-1])
                parsed[key] = datetime.datetime.fromtimestamp(timestamp)
        documents.append(parsed)

    site.index.add(documents)
