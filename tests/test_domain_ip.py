from src.tools.network import domain_ip_logic
from src.tools.network.domain_ip_logic import extract_domain, lookup_site_ip_info


def test_extract_domain_accepts_url_with_http():
    assert extract_domain("http://example.com/path") == "example.com"


def test_extract_domain_accepts_url_without_http():
    assert extract_domain("example.com/path") == "example.com"


def test_extract_domain_keeps_subdomain_and_removes_port():
    assert (
        extract_domain("https://www.example.com:443/search?q=test")
        == "www.example.com"
    )


def test_lookup_site_ip_info_returns_domain_ip_country_and_isp(monkeypatch):
    monkeypatch.setattr(
        domain_ip_logic,
        "resolve_domain_to_ip",
        lambda domain: ["93.184.216.34"],
    )

    result = lookup_site_ip_info(
        "https://example.com/docs",
        geolocation_lookup=lambda ip: {
            "status": "success",
            "query": ip,
            "country": "United States",
            "isp": "Example ISP",
        },
    )

    assert result.domain == "example.com"
    assert result.ip == "93.184.216.34"
    assert result.country == "United States"
    assert result.isp == "Example ISP"
    assert result.to_display_text() == (
        "Domain: example.com\n"
        "IP: 93.184.216.34\n"
        "Country: United States\n"
        "ISP: Example ISP"
    )
