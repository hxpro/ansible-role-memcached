import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_memcached_running_and_enabled(host):
    memcached = host.service("memcached")
    assert memcached.is_running
    assert memcached.is_enabled


def test_memcached_port_listening(host):
    assert host.socket("tcp://127.0.0.1:11211").is_listening
