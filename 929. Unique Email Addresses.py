class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        unique = set()
        
        for email in emails:
            local, domain = email.split('@')
            local = ''.join((local.split('+')[0]).split('.'))
            unique.add((local, domain))
        
        return len(unique)
