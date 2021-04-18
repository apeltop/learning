# https://leetcode.com/explore/featured/card/google/67/sql-2/3044/
from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        emailSet = set()
        for email in emails:
            localName, domainName = email.split("@")
            localName = localName.replace('.', '')
            plusIndex = localName.find('+')
            if plusIndex > -1:
                localName = localName[:plusIndex]
            emailSet.add(f'{localName}@{domainName}')
        return len(emailSet)


print(Solution().numUniqueEmails(
    ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]))  # 2
