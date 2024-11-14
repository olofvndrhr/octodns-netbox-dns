# netbox-plugin-dns provider for octodns

> works with https://github.com/peteeckel/netbox-plugin-dns

## config

```yml
providers:
    config:
        class: octodns_netbox_dns.NetBoxDNSProvider
        # Netbox url
        # [mandatory, default=null]
        url: "https://some-url"
        # Netbox API token
        # [mandatory, default=null]
        token: env/NETBOX_API_KEY
        # View of the zone. Can be either a string -> the view name
        # "null" -> to only query zones without a view
        # false -> to ignore views
        # [optional, default=false]
        view: false
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
        # Disable cert. verification for netbox https.
        # [optional, default=false]
        insecure_request: false
```

## compatibility

> actively tested on the newest `netbox-plugin-dns` and `netbox` versions

| provider    | [netbox-plugin-dns](https://github.com/peteeckel/netbox-plugin-dns) | [netbox](https://github.com/netbox-community/netbox) |
| ----------- | ------------------------------------------------------------------- | ---------------------------------------------------- |
| `>= v0.3.3` | `>=0.21.0`                                                          | `>=3.6.0`                                            |
| `>= v0.3.6` | `>=1.0.0`                                                           | `>=4.0.0`                                            |

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
