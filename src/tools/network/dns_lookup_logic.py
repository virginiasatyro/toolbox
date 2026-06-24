from typing import Dict, List

import dns.resolver


def lookup_dns_records(domain: str) -> Dict[str, List[str]]:
    """Lookup common DNS record types for a domain.

    Returns a dict mapping record type to list of string records.
    """
    record_types = ["A", "AAAA", "MX", "TXT", "NS"]
    results: Dict[str, List[str]] = {}

    resolver = dns.resolver.Resolver()

    for rtype in record_types:
        try:
            answers = resolver.resolve(domain, rtype)
            records: List[str] = []
            for r in answers:
                if rtype == "MX":
                    records.append(str(r.exchange).rstrip('.'))
                elif rtype == "TXT":
                    # TXT answers may be bytes sequences
                    records.append("".join([part.decode() if isinstance(part, bytes) else str(part) for part in r.strings]))
                else:
                    records.append(str(r).rstrip('.'))
            results[rtype] = records
        except Exception:
            results[rtype] = []

    return results
