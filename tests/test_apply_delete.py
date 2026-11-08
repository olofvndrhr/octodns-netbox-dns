from types import SimpleNamespace
from typing import Any

import octodns.record
import octodns.zone

from octodns_netbox_dns import NetBoxDNSProvider


class FakeRecord(SimpleNamespace):
    """A netbox record which tracks whether it got deleted."""

    def __init__(self, **kwargs: Any) -> None:
        """Create a record with sane defaults."""
        kwargs.setdefault("id", 1)
        kwargs.setdefault("type", "A")
        super().__init__(deleted=False, **kwargs)

    def delete(self) -> bool:
        self.deleted = True
        return True


class FakeRecordEndpoint:
    """Stand-in for the netbox dns records endpoint."""

    def __init__(self, items: list[Any]) -> None:
        """Create an endpoint returning the given records."""
        self.items = items
        self.filters: dict[str, Any] = {}

    def filter(self, **kwargs: Any) -> list[Any]:
        self.filters = kwargs
        # netbox drops an empty "name" filter instead of matching nothing
        name = kwargs.get("name")
        items = [item for item in self.items if name in ("", None) or item.name == name]
        return [item for item in items if item.type == kwargs.get("type")]


def _provider(nb_records: list[Any]) -> NetBoxDNSProvider:
    provider = NetBoxDNSProvider(
        id=1,
        url="https://localhost:8000",
        token="",
        view=False,
    )
    provider.records = FakeRecordEndpoint(nb_records)  # type: ignore
    provider.api = SimpleNamespace(  # type: ignore
        plugins=SimpleNamespace(
            netbox_dns=SimpleNamespace(
                records=provider.records,  # type: ignore
                zones=SimpleNamespace(
                    get=lambda **_kwargs: SimpleNamespace(id=1, name="example.com")
                ),
            )
        )
    )

    return provider


def _delete_plan(name: str, value: str) -> Any:
    zone = octodns.zone.Zone("example.com.", [])
    record = octodns.record.Record.new(zone, name, {"type": "A", "ttl": 300, "value": value})

    return SimpleNamespace(desired=zone, changes=[octodns.record.Delete(record)])


def test_deleting_an_apex_record_queries_the_apex_name() -> None:
    apex = FakeRecord(id=1, name="@", value="203.0.113.10")
    provider = _provider([apex])

    provider._apply(_delete_plan("", "203.0.113.10"))

    assert provider.records.filters["name"] == "@"  # type: ignore
    assert apex.deleted is True


def test_deleting_an_apex_record_keeps_other_names_with_the_same_value() -> None:
    apex = FakeRecord(id=1, name="@", value="203.0.113.10")
    www = FakeRecord(id=2, name="www", value="203.0.113.10")
    provider = _provider([apex, www])

    provider._apply(_delete_plan("", "203.0.113.10"))

    assert apex.deleted is True
    assert www.deleted is False


def test_deleting_a_normal_record_is_unchanged() -> None:
    www = FakeRecord(id=2, name="www", value="203.0.113.10")
    provider = _provider([www])

    provider._apply(_delete_plan("www", "203.0.113.10"))

    assert provider.records.filters["name"] == "www"  # type: ignore
    assert www.deleted is True
