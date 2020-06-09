# NetJSON DeviceMonitoring schema,
# https://github.com/netjson/netjson/blob/master/schema/device-monitoring.json
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "$id": "https://raw.githubusercontent.com/netjson/netjson/master/schema/device-monitoring.json",
    "title": "NetJSON Device Monitoring",
    "description": "Monitoring information sent by a device.",
    "type": "object",
    "additionalProperties": True,
    "required": ["type"],
    "properties": {
        "type": {"type": "string", "enum": ["DeviceMonitoring"]},
        "general": {
            "type": "object",
            "title": "General",
            "additionalProperties": True,
            "properties": {
                "local_time": {"type": "integer"},
                "uptime": {"type": "integer"},
            },
        },
        "resources": {
            "type": "object",
            "title": "Resources",
            "additionalProperties": True,
            "properties": {
                "load": {
                    "type": "array",
                    "items": {"type": "number", "minItems": 3, "maxItems": 3},
                },
                "cpus": {"type": "integer"},
                "memory": {
                    "id": "memory",
                    "type": "object",
                    "properties": {
                        "total": {"type": "integer"},
                        "free": {"type": "integer"},
                        "buffered": {"type": "integer"},
                        "cached": {"type": "integer"},
                        "shared": {"type": "integer"},
                        "available": {"type": "integer"},
                    },
                    "required": ["total", "free", "buffered", "shared"],
                },
                "disk": {
                    "type": "array",
                    "additionalItems": False,
                    "title": "Disks",
                    "items": {
                        "type": "object",
                        "title": "Disk",
                        "additionalProperties": False,
                        "properties": {
                            "mount_point": {"type": "string"},
                            "filesystem": {"type": "string"},
                            "used_bytes": {"type": "integer"},
                            "available_bytes": {"type": "integer"},
                            "used_percent": {"type": "integer"},
                            "size_bytes": {"type": "integer"},
                        },
                        "required": [
                            "mount_point",
                            "filesystem",
                            "used_bytes",
                            "available_bytes",
                            "used_percent",
                            "size_bytes",
                        ],
                    },
                },
                "swap": {
                    "type": "object",
                    "properties": {
                        "total": {"type": "integer"},
                        "free": {"type": "integer"},
                    },
                },
                "connections": {
                    "type": "object",
                    "properties": {
                        "ipv4": {
                            "type": "object",
                            "properties": {
                                "tcp": {"type": "integer"},
                                "udp": {"type": "integer"},
                            },
                        },
                        "ipv6": {
                            "type": "object",
                            "properties": {
                                "tcp": {"type": "integer"},
                                "udp": {"type": "integer"},
                            },
                        },
                    },
                },
                "processes": {
                    "type": "object",
                    "properties": {
                        "running": {"type": "integer"},
                        "sleeping": {"type": "integer"},
                        "blocked": {"type": "integer"},
                        "zombie": {"type": "integer"},
                        "stopped": {"type": "integer"},
                        "paging": {"type": "integer"},
                    },
                },
                "cpu": {
                    "type": "object",
                    "properties": {
                        "frequency": {"type": "integer"},
                        "user": {"type": "integer"},
                        "system": {"type": "integer"},
                        "nice": {"type": "integer"},
                        "idle": {"type": "integer"},
                        "iowait": {"type": "integer"},
                        "irq": {"type": "integer"},
                        "softirq": {"type": "integer"},
                    },
                },
                "flash": {
                    "type": "object",
                    "properties": {
                        "total": {"type": "integer"},
                        "free": {"type": "integer"},
                    },
                },
                "storage": {
                    "type": "object",
                    "properties": {
                        "total": {"type": "integer"},
                        "free": {"type": "integer"},
                    },
                },
            },
        },
        "interfaces": {
            "type": "array",
            "title": "Interfaces",
            "uniqueItems": True,
            "additionalItems": True,
            "items": {
                "type": "object",
                "title": "Interface",
                "additionalProperties": True,
                "required": ["name"],
                "properties": {
                    "name": {"type": "string"},
                    "uptime": {"type": "integer"},
                    "statistics": {
                        "type": "object",
                        "properties": {
                            "collisions": {"type": "integer"},
                            "rx_frame_errors": {"type": "integer"},
                            "tx_compressed": {"type": "integer"},
                            "multicast": {"type": "integer"},
                            "rx_length_errors": {"type": "integer"},
                            "tx_dropped": {"type": "integer"},
                            "rx_bytes": {"type": "integer"},
                            "rx_missed_errors": {"type": "integer"},
                            "tx_errors": {"type": "integer"},
                            "rx_compressed": {"type": "integer"},
                            "rx_over_errors": {"type": "integer"},
                            "tx_fifo_errors": {"type": "integer"},
                            "rx_crc_errors": {"type": "integer"},
                            "rx_packets": {"type": "integer"},
                            "tx_heartbeat_errors": {"type": "integer"},
                            "rx_dropped": {"type": "integer"},
                            "tx_aborted_errors": {"type": "integer"},
                            "tx_packets": {"type": "integer"},
                            "rx_errors": {"type": "integer"},
                            "tx_bytes": {"type": "integer"},
                            "tx_window_errors": {"type": "integer"},
                            "rx_fifo_errors": {"type": "integer"},
                            "tx_carrier_errors": {"type": "integer"},
                        },
                    },
                    "wireless": {
                        "type": "object",
                        "additionalProperties": False,
                        "required": [
                            "channel",
                            "country",
                            "frequency",
                            "mode",
                            "noise",
                            "ssid",
                            "tx_power",
                        ],
                        "properties": {
                            "channel": {"type": "integer"},
                            "country": {"type": "string"},
                            "frequency": {"type": "integer"},
                            "mode": {"type": "string"},
                            "noise": {"type": "integer"},
                            "signal": {"type": "integer"},
                            "ssid": {"type": "string"},
                            "tx_power": {"type": "integer"},
                            "clients": {
                                "type": "array",
                                "title": "Wireless Clients",
                                "additionalItems": False,
                                "required": [
                                    "aid",
                                    "assoc",
                                    "auth",
                                    "authorized",
                                    "ht",
                                    "vht",
                                    "wds",
                                    "wmm",
                                    "wps",
                                    "mac",
                                    "mfp",
                                    "preauth",
                                    "rrm",
                                    "signature",
                                ],
                                "items": {
                                    "type": "object",
                                    "title": "Client",
                                    "additionalProperties": False,
                                    "properties": {
                                        "aid": {"type": "integer"},
                                        "assoc": {"type": "boolean"},
                                        "auth": {"type": "boolean"},
                                        "authorized": {"type": "boolean"},
                                        "ht": {"type": "boolean"},
                                        "vht": {"type": "boolean"},
                                        "wds": {"type": "boolean"},
                                        "wmm": {"type": "boolean"},
                                        "wps": {"type": "boolean"},
                                        "mac": {"type": "string"},
                                        "vendor": {"type": "string"},
                                        "mfp": {"type": "boolean"},
                                        "preauth": {"type": "boolean"},
                                        "signature": {"type": "string"},
                                        "rrm": {
                                            "type": "array",
                                            "minItems": 5,
                                            "maxItems": 5,
                                            "additionalItems": False,
                                            "items": {"type": "integer"},
                                        },
                                    },
                                },
                            },
                        },
                    },
                    "addresses": {
                        "type": "array",
                        "title": "Addresses",
                        "uniqueItems": True,
                        "additionalItems": True,
                        "items": {
                            "additionalProperties": True,
                            "title": "Address",
                            "type": "object",
                            "required": ["proto", "family", "address", "mask"],
                            "properties": {
                                "proto": {"type": "string"},
                                "family": {"type": "string"},
                                "address": {
                                    "type": "string",
                                    "anyOf": [{"format": "ipv4"}, {"format": "ipv6"}],
                                },
                                "mask": {"type": "integer"},
                            },
                        },
                    },
                },
            },
        },
        "dhcp_leases": {
            "type": "array",
            "title": "DHCP leases",
            "additionalItems": False,
            "items": {
                "type": "object",
                "title": "DHCP lease",
                "additionalProperties": False,
                "properties": {
                    "expiry": {"type": "number"},
                    "ip_address": {
                        "type": "string",
                        "anyOf": [{"format": "ipv4"}, {"format": "ipv6"}],
                    },
                    "mac_address": {"type": "string"},
                    "vendor": {"type": "string"},
                    "client_name": {"type": "string"},
                    "client_id": {"type": "string"},
                },
                "required": [
                    "expiry",
                    "ip_address",
                    "mac_address",
                    "client_name",
                    "client_id",
                ],
            },
        },
        "neighbors": {
            "type": "array",
            "title": "Neighbors",
            "additionalItems": False,
            "items": {
                "type": "object",
                "title": "Neighbor",
                "additionalProperties": False,
                "properties": {
                    "ip_address": {
                        "type": "string",
                        "anyOf": [{"format": "ipv4"}, {"format": "ipv6"}],
                    },
                    "mac_address": {"type": "string"},
                    "vendor": {"type": "string"},
                    "interface": {"type": "string"},
                    "state": {"type": "string"},
                },
                "required": ["ip_address", "interface"],
            },
        },
    },
}
