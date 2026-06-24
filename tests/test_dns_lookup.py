from src.tools.network.dns_lookup_logic import lookup_dns_records


def test_lookup_dns_records_returns_expected_structure():
    result = lookup_dns_records("example.com")
    assert isinstance(result, dict)
    for key in ["A", "AAAA", "MX", "TXT", "NS"]:
        assert key in result
        assert isinstance(result[key], list)
