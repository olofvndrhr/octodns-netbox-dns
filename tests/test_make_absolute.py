from octodns_netbox_dns import NetBoxDNSProvider


DEFAULT_CONFIG = {
    "id": 1,
    "url": "https://localhost:8000",
    "token": "",
    "view": False,
    "replace_duplicates": False,
    "make_absolute": True,
}

nbdns = NetBoxDNSProvider(**DEFAULT_CONFIG)


def test_absolute():
    rcd = "example.com"
    absolute = nbdns._make_absolute(rcd)

    assert absolute == "example.com."


def test_noop():
    rcd = "example.com."
    absolute = nbdns._make_absolute(rcd)

    assert absolute == "example.com."


def test_disabled():
    args = {**DEFAULT_CONFIG, "make_absolute": False}
    nbdns = NetBoxDNSProvider(**args)
    rcd = "example.com"
    relative = nbdns._make_absolute(rcd, force=False)

    assert relative == "example.com"


def test_force():
    args = {**DEFAULT_CONFIG, "make_absolute": False}
    nbdns = NetBoxDNSProvider(**args)
    rcd = "example.com"
    absolute = nbdns._make_absolute(rcd, force=True)

    assert absolute == "example.com."
