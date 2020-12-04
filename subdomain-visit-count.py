"""
https://leetcode.com/problems/subdomain-visit-count/submissions/
"""


# This is pretty brute force... Worse case run time is O(n*m) where n =
# number of elements in cpdomains and m is the maximum number of subdomains.
def subdomainVisits(cpdomains):
    hash_table = {}

    for _domain in cpdomains:

        count, domain = _domain.split(" ")
        split_domain = domain.split(".")

        for i in range(len(split_domain)):
            subdomain = ".".join(split_domain[i:])

            existing_count = hash_table.get(subdomain, 0)
            new_count = existing_count + int(count)
            hash_table[subdomain] = new_count

    new_counts = []

    for domain, count in hash_table.items():
        new_counts.append(f"{count} {domain}")

    return new_counts
