from types import SimpleNamespace
from typing import Literal

from octodns_netbox_dns import NetBoxDNSProvider


def _provider(
    ns_ttl_mode: Literal["soa_refresh", "record", "fixed"] = "soa_refresh",
    ns_ttl_value: int = 14400,
) -> NetBoxDNSProvider:
    return NetBoxDNSProvider(
        id=1,
        url="https://localhost:8000",
        token="",
        view=False,
        replace_duplicates=False,
        make_absolute=True,
        ns_ttl_mode=ns_ttl_mode,
        ns_ttl_value=ns_ttl_value,
    )


def test_ns_ttl_mode_soa_refresh() -> None:
    provider = _provider(ns_ttl_mode="soa_refresh")
    zone = SimpleNamespace(default_ttl=3600, soa_refresh=600)
    record = SimpleNamespace(type="NS", ttl=86400, name="@")

    assert provider._record_ttl(zone, record) == 600


def test_ns_ttl_mode_record() -> None:
    provider = _provider(ns_ttl_mode="record")
    zone = SimpleNamespace(default_ttl=3600, soa_refresh=600)
    record = SimpleNamespace(type="NS", ttl=86400, name="@")

    assert provider._record_ttl(zone, record) == 86400


def test_ns_ttl_mode_fixed_for_apex_ns() -> None:
    provider = _provider(ns_ttl_mode="fixed", ns_ttl_value=14400)
    zone = SimpleNamespace(default_ttl=3600, soa_refresh=600)
    record = SimpleNamespace(type="NS", ttl=86400, name="@")

    assert provider._record_ttl(zone, record) == 14400


def test_ns_ttl_mode_fixed_preserves_non_apex_ns() -> None:
    provider = _provider(ns_ttl_mode="fixed", ns_ttl_value=14400)
    zone = SimpleNamespace(default_ttl=3600, soa_refresh=600)
    record = SimpleNamespace(type="NS", ttl=3600, name="delegated")

    assert provider._record_ttl(zone, record) == 3600


def test_non_ns_records_use_record_ttl() -> None:
    provider = _provider(ns_ttl_mode="fixed", ns_ttl_value=14400)
    zone = SimpleNamespace(default_ttl=3600, soa_refresh=600)
    record = SimpleNamespace(type="A", ttl=7200, name="@")

    assert provider._record_ttl(zone, record) == 7200
