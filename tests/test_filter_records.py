from octodns_netbox_dns import NetBoxDNSProvider


class Change:
    def __init__(self, rtype: str):
        self.record = Record(rtype)


class Record:
    def __init__(self, rtype: str):
        self._type = rtype


DEFAULT_CONFIG = {
    "id": 1,
    "url": "https://localhost:8000",
    "token": "",
    "view": False,
    "replace_duplicates": False,
    "make_absolute": True,
}


def test1():
    nbdns = NetBoxDNSProvider(**DEFAULT_CONFIG)
    for n in ["SOA", "NS"]:
        change = Change(n)
        include_rcd = nbdns._include_change(change)

        assert not include_rcd


def test2():
    nbdns = NetBoxDNSProvider(**DEFAULT_CONFIG)
    for n in ["A", "AAA", "CNAME", "TXT", "MX", "PTR"]:
        change = Change(n)
        include_rcd = nbdns._include_change(change)

        assert include_rcd
