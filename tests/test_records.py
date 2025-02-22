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


def test_a():
    rcd_type = "A"
    rcd_value = "127.0.0.1"
    value = nbdns._format_rdata(rcd_type, rcd_value)

    assert value == "127.0.0.1"


def test_aaaa():
    rcd_type = "AAAA"
    rcd_value = "fc07::1"
    value = nbdns._format_rdata(rcd_type, rcd_value)

    assert value == "fc07::1"


def test_alias():
    pass  # not supported


def test_caa():
    rcd_type = "CAA"
    rcd_value = '0 issue "letsencrypt.org"'
    value = nbdns._format_rdata(rcd_type, rcd_value)

    assert value == {
        "flags": 0,
        "tag": "issue",
        "value": "letsencrypt.org",
    }


def test_cname():
    rcd_type = "CNAME"
    rcd_value = "test.example.com."
    value = nbdns._format_rdata(rcd_type, rcd_value)

    assert value == "test.example.com."


def test_dname():
    rcd_type = "DNAME"
    rcd_value = "example.com."
    value = nbdns._format_rdata(rcd_type, rcd_value)

    assert value == "example.com."


def test_ds():
    pass  # not supported


def test_loc():
    rcd_type = "LOC"
    rcd_value = "0 0 0 N 0 0 0 W 1 1 10000 10"
    value = nbdns._format_rdata(rcd_type, rcd_value)

    assert value == {
        "lat_degrees": 0,
        "lat_minutes": 0,
        "lat_seconds": 0.0,
        "lat_direction": "N",
        "long_degrees": 0,
        "long_minutes": 0,
        "long_seconds": 0.0,
        "long_direction": "W",
        "altitude": 1.0,
        "size": 1.0,
        "precision_horz": 10000.0,
        "precision_vert": 10.0,
    }


def test_mx():
    rcd_type = "MX"
    rcd_value = "10 mx.example.com"
    value = nbdns._format_rdata(rcd_type, rcd_value)

    assert value == {
        "preference": 10,
        "exchange": "mx.example.com.",
    }


def test_naptr():
    pass  # not supported


def test_ns():
    rcd_type = "NS"
    rcd_value = "ns.example.com."
    value = nbdns._format_rdata(rcd_type, rcd_value)

    assert value == "ns.example.com."


def test_ptr():
    rcd_type = "PTR"
    rcd_value = "host.example.com."
    value = nbdns._format_rdata(rcd_type, rcd_value)

    assert value == "host.example.com."


def test_spf():
    pass  # not supported


def test_srv():
    rcd_type = "SRV"
    rcd_value = r"0 5 25565 mc.example.com"
    value = nbdns._format_rdata(rcd_type, rcd_value)

    assert value == {
        "priority": 0,
        "weight": 5,
        "port": 25565,
        "target": "mc.example.com.",
    }


def test_sshfp():
    rcd_type = "SSHFP"
    rcd_value = "4 2 123456789abcdef67890123456789abcdef67890123456789abcdef123456789"
    value = nbdns._format_rdata(rcd_type, rcd_value)

    assert value == {
        "algorithm": 4,
        "fingerprint_type": 2,
        "fingerprint": "123456789abcdef67890123456789abcdef67890123456789abcdef123456789",
    }


def test_tlsa():
    pass  # not supported


def test_txt1():
    rcd_type = "TXT"
    rcd_value = "v=TLSRPTv1; rua=mailto:tlsrpt@example.com"
    value = nbdns._format_rdata(rcd_type, rcd_value)

    assert value == r"v=TLSRPTv1\; rua=mailto:tlsrpt@example.com"


def test_txt2():
    rcd_type = "TXT"
    rcd_value = r"v=TLSRPTv1\; rua=mailto:tlsrpt@example.com"
    value = nbdns._format_rdata(rcd_type, rcd_value)

    assert value == r"v=TLSRPTv1\\; rua=mailto:tlsrpt@example.com"


def test_txt3():
    rcd_type = "TXT"
    rcd_value = r"v=DKIM1; k=rsa; p=/0f+sikE+k9ZKbn1BJu0/soWht/+Zd/nc/+Gy//mQ1B5sCKYKgAmYTSWkxRjFzkc6KAQhi+/IzaFogEV050wcscdC8Rc8lAQzDUFrMs2ZZK1vFtkwIDAQAB"
    value = nbdns._format_rdata(rcd_type, rcd_value)

    assert (
        value
        == r"v=DKIM1\; k=rsa\; p=/0f+sikE+k9ZKbn1BJu0/soWht/+Zd/nc/+Gy//mQ1B5sCKYKgAmYTSWkxRjFzkc6KAQhi+/IzaFogEV050wcscdC8Rc8lAQzDUFrMs2ZZK1vFtkwIDAQAB"
    )


def test_txt4():
    rcd_type = "TXT"
    rcd_value = r"t=y\;o=~\;"
    value = nbdns._format_rdata(rcd_type, rcd_value)

    assert value == r"t=y\\;o=~\\;"


def test_txt5():
    rcd_type = "TXT"
    rcd_value = r"t=y;o=~;"
    value = nbdns._format_rdata(rcd_type, rcd_value)

    assert value == r"t=y\;o=~\;"


def test_urlfwd():
    pass  # not supported
