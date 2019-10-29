hxpro.memcached
===============

memcached - high-performance memory object caching system

Requirements
------------

 - CentOS 7
 - The ipaddr filter requires python's netaddr be installed on the ansible controller

Role Variables
--------------

    memcached_cachesize: 100
    memcached_bind_ip: 127.0.0.1

Example Playbook
----------------

    - hosts: servers
      roles:
         - role: hxpro.memcached
           memcached_cachesize: 300
           memcached_bind_ip: 192.168.1.1

License
-------

WTFPL

Author Information
------------------

Matěj Koudelka <matej@hxpro.cz>
