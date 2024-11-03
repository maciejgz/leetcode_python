from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_name = {}
        graph = {}
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                if email not in graph:
                    graph[email] = set()
                graph[email].add(acc[1])
                graph[acc[1]].add(email)
                email_to_name[email] = name

        visited = set()
        res = []
        for email in graph:
            if email not in visited:
                visited.add(email)
                stack = [email]
                emails = []
                while stack:
                    node = stack.pop()
                    emails.append(node)
                    for nei in graph[node]:
                        if nei not in visited:
                            visited.add(nei)
                            stack.append(nei)
                res.append([email_to_name[email]] + sorted(emails))
        return res


if __name__ == "__main__":
    sol = Solution()
    print(
        sol.accountsMerge(
            [
                ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
                ["John", "johnsmith@mail.com", "john00@mail.com"],
                ["Mary", "mary@mail.com"],
                ["John", "johnnybravo@mail.com"],
            ]
        )
    )
    print(
        sol.accountsMerge(
            [
                ["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"],
                ["Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"],
                ["Ethan", "Ethan5@m.co", "Ethan4@m.co", "Ethan0@m.co"],
                ["Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"],
                ["Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co"],
            ]
        )
    )
