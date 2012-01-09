
Munin Plugins for MongoDB
============

Plugins
----------
* mongo_ops   : operations/second
* mongo_mem   : mapped, virtual and resident memory usage
* mongo_btree : btree access/misses/etc...
* mongo_conn  : current connections
* mongo_lock  : write lock info  

Requirements
-----------
* simplejson or python >= 2.6
* MongoDB 1.4+ 

Configuration
-----------
You may need to create an init file for the mongo_* munin plugins: /etc/munin/plugin-conf.d/mongo

[mongo*]
env.user munin
env.password munin_pass
env.port port


