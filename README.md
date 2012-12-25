schism
======

TODO List:

- [ ] Load collections from disk to Solr
- [ ] render collections from solr
- [ ] override default templates
- [ ] Load collections from S3 to Solr
- [ ] Custom renderers 
- [ ] JSON/ API

___what is Schism and why?___

(This is currently all speculative)

Schism is a system for adding content to a Solr index, transforming it into various formats, and serving it over HTTP.
It is not opinionated about how that content is *stored*, although
implementations for MongoDB, S3 + JSON, and filesystem + JSON are provided. 

Components:

- An Indexer that feeds hierarchical content into Solr.
- A Query interface that provides access to the Solr index
- A Views system that lets you stitch together Queries and transformations
- A restful JSON API that exposes all content to outside developers

It was created to support an environment where content was being produced and managed in multiple systems (Wordpress and Django), and a separation of concerns between managing and serving content became desirable. Other values were: ease of management, ease of deployment, template unification, and a consistent web services API for all content.
