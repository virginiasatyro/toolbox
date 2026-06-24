from __future__ import annotations

from dataclasses import dataclass
import json
import socket
from typing import Any, Callable
from urllib.parse import quote, urlparse
from urllib.request import urlopen

GEOLOCATION_FIELDS = "status,message,country,isp,query"
GEOLOCATION_URL = "http://ip-api.com/json/{ip}?fields={fields}"


@dataclass(frozen=True)
class DomainIpInfo:
    domain: str
    ip: str
    country: str
    isp: str

    def to_display_text(self) -> str:
        return (
            f"Domain: {self.domain}\n"
            f"IP: {self.ip}\n"
            f"Country: {self.country}\n"
            f"ISP: {self.isp}"
        )


def resolve_domain_to_ip(domain: str) -> list[str]:
    """Resolve a domain name to a list of IP addresses (v4 and v6).

    Returns a list of unique IP address strings. Raises socket.gaierror on failure.
    """
    results: list[str] = []
    infos = socket.getaddrinfo(domain, None, socket.AF_UNSPEC, socket.SOCK_STREAM)

    for info in infos:
        addr = info[4][0]
        if addr not in results:
            results.append(addr)

    return results


def lookup_site_ip_info(
    site_url: str,
    geolocation_lookup: Callable[[str], dict[str, Any]] | None = None,
) -> DomainIpInfo:
    domain = extract_domain(site_url)
    addresses = resolve_domain_to_ip(domain)

    if not addresses:
        raise ValueError(f"No IP addresses found for {domain}")

    ip = addresses[0]
    geolocation = (
        geolocation_lookup(ip) if geolocation_lookup else lookup_ip_geolocation(ip)
    )

    if geolocation.get("status") == "fail":
        message = geolocation.get("message", "geolocation lookup failed")
        raise ValueError(f"Could not look up geolocation for {ip}: {message}")

    return DomainIpInfo(
        domain=domain,
        ip=str(geolocation.get("query") or ip),
        country=str(geolocation.get("country") or "Unknown"),
        isp=str(geolocation.get("isp") or "Unknown"),
    )


def extract_domain(site_url: str) -> str:
    normalized = site_url.strip()
    if not normalized:
        raise ValueError("Site URL is required")

    if "://" not in normalized:
        normalized = f"http://{normalized}"

    parsed = urlparse(normalized)
    domain = parsed.hostname

    if not domain:
        raise ValueError("Enter a valid site URL")

    domain = domain.rstrip(".").lower()
    if not domain or any(char.isspace() for char in domain):
        raise ValueError("Enter a valid site URL")

    return domain


def lookup_ip_geolocation(ip: str) -> dict[str, Any]:
    url = GEOLOCATION_URL.format(
        ip=quote(ip, safe=":"),
        fields=quote(GEOLOCATION_FIELDS, safe=","),
    )

    with urlopen(url, timeout=5) as response:
        payload = response.read().decode("utf-8")

    data = json.loads(payload)
    if not isinstance(data, dict):
        raise ValueError("Unexpected geolocation response")

    return data
