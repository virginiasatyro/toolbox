from src.tools.network.domain_ip_logic import resolve_domain_to_ip


def test_resolve_domain_to_ip_returns_list():
    # Use a well-known domain; network access required for this test.
    result = resolve_domain_to_ip("example.com")
    assert isinstance(result, list)
    # At least one address string is expected
    assert all(isinstance(addr, str) for addr in result)
