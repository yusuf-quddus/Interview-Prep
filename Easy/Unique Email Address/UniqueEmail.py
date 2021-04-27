class Solution(object):
    """
    :type emails: List[str]
    :rtype: int
    """  
    def numUniqueEmails(self, emails):
        unique_email = []
        for email in emails:
            i = 0
            unique = ""
            local = email.split("@")
            domain = "@" + local[1]
            local = local[0].replace('.', '')
            while((i < len(local)) and local[i] != '+'):
                unique = unique + local[i]
                i += 1
            mail = unique + domain
            if mail not in unique_email:
                unique_email.append(mail)
        return len(unique_email)