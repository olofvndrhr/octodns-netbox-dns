# netbox-plugin-dns provider for octodns

[octodns](https://github.com/octodns/octodns) provider for [netbox-plugin-dns](https://github.com/peteeckel/netbox-plugin-dns)

> syncs dns records from and to netbox via [octodns](https://github.com/octodns/octodns)

## config

```yml
providers:
    config:
        class: octodns_netbox_dns.NetBoxDNSProvider
        # Netbox instance url
        # [mandatory]
        url: "https://some-url"
        # Netbox API token
        # [mandatory]
        token: env/NETBOX_API_KEY
        # Filter by zone view. Can either be the name of the view, or "null".
        # "null" -> do not filter by view.
        # [optional, default=null]
        view: null
        # When records sourced from multiple providers, allows provider
        # to replace entries coming from the previous one.
        # Implementation matches YamlProvider's 'populate_should_replace'
        # [optional, default=false]
        replace_duplicates: false
        # Make CNAME, MX and SRV records absolute if they are missing the trailing "."
        # [optional, default=false]
        make_absolute: false
        # Disable automatic PTR record creating in the NetboxDNS plugin.
        # [optional, default=true]
        disable_ptr: true
        # Disable certificate verification for unsecure https.
        # [optional, default=false]
        insecure_request: false
        # Only include zones with this status when dynamic zones are used, e.g. "*".
        # [optional, default=active]
        zone_status_filter: active
        # Only include records with this status when records are listed from a zone.
        # [optional, default=active]
        record_status_filter: active
        # Maximal page size of queries.
        # A value of 0 means: show every item. Can cause errors with the NetBox setting: MAX_PAGE_SIZE
        # [optional, default=0]
        max_page_size: 0
```

## compatibility

> actively tested on the newest `netbox-plugin-dns` and `netbox` versions

| provider     | [netbox-plugin-dns](https://github.com/peteeckel/netbox-plugin-dns) | [netbox](https://github.com/netbox-community/netbox) |
| ------------ | ------------------------------------------------------------------- | ---------------------------------------------------- |
| `>= v0.3.3`  | `>=0.21.0`                                                          | `>=3.6.0`                                            |
| `>= v0.3.6`  | `>=1.0.0`                                                           | `>=4.0.0`                                            |
| `>= v0.3.11` | `>=1.2.3`                                                           | `>=4.2.0`                                            |

## limitations

the records can only be synced to netbox-dns if the zone is already existing.
the provider _CAN NOT_ create zones (as of now).

## install

### via pip

```bash
pip install octodns-netbox-dns
```

### via pip + git

```bash
pip install octodns-netbox-dns@git+https://github.com/olofvndrhr/octodns-netbox-dns.git@main
```

### via pip + `requirements.txt`

add the following line to your requirements file

```bash
octodns-netbox-dns@git+https://github.com/olofvndrhr/octodns-netbox-dns.git@main
```
