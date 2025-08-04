from octodns_netbox_dns import NetBoxDNSProvider


DEFAULT_CONFIG = {
    "id": 1,
    "url": "https://localhost:8000",
    "token": "",
    "make_absolute": True,
}
nbdns = NetBoxDNSProvider(**DEFAULT_CONFIG)  # type:ignore


def test_escape1() -> None:
    rcd_value = r"v=TLSRPTv1; rua=mailto:tlsrpt@example.com"
    value = nbdns._escape_semicolon(rcd_value)

    assert value == r"v=TLSRPTv1\; rua=mailto:tlsrpt@example.com"


def test_escape2() -> None:
    rcd_value = r"v=TLSRPTv1\; rua=mailto:tlsrpt@example.com"
    value = nbdns._escape_semicolon(rcd_value)

    assert value == r"v=TLSRPTv1\\; rua=mailto:tlsrpt@example.com"


def test_escape3() -> None:
    rcd_value = r"t=y\;o=~\;"
    value = nbdns._escape_semicolon(rcd_value)

    assert value == r"t=y\\;o=~\\;"


def test_escape4() -> None:
    rcd_value = r"t=y;o=~;"
    value = nbdns._escape_semicolon(rcd_value)

    assert value == r"t=y\;o=~\;"


def test_unescape1() -> None:
    rcd_value = r"v=TLSRPTv1\; rua=mailto:tlsrpt@example.com"
    value = nbdns._unescape_semicolon(rcd_value)

    assert value == r"v=TLSRPTv1; rua=mailto:tlsrpt@example.com"


def test_unescape2() -> None:
    rcd_value = r"v=TLSRPTv1\\; rua=mailto:tlsrpt@example.com"
    value = nbdns._unescape_semicolon(rcd_value)

    assert value == r"v=TLSRPTv1; rua=mailto:tlsrpt@example.com"


def test_unescape3() -> None:
    rcd_value = r"t=y\\;o=~\;"
    value = nbdns._unescape_semicolon(rcd_value)

    assert value == r"t=y;o=~;"


def test_unescape4() -> None:
    rcd_value = r"t=y;o=~;"
    value = nbdns._unescape_semicolon(rcd_value)

    assert value == r"t=y;o=~;"
