from schism import SchismSite
from schism.drivers.storage import FileSystem
from pysolr import Solr

solr = Solr('http://127.0.0.1:8983/solr/')


data=FileSystem('data')


site= SchismSite(data, index=solr)