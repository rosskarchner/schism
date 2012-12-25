import argparse
from resolver import resolve


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='load a Schism document store into Solr')
    parser.add_argument('configuration',
                        metavar='CONFIG',
                        help='a Resolver statement pointing to a SchismSite')
    args = parser.parse_args()
    site = resolve(args.configuration)
    document_paths = site.list_documents()

    documents = []
    for document_path in document_paths:
        documents.append(site.retrieve_document(document_path))
    site.index.add(documents)
