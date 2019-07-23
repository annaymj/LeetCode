Emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]

class Solution:
    def numUniqueEmails(self, emails) -> int:
        result = []
        for e in emails:
            e_split = e.split("@")
            
            local_name = e_split[0]
            domain_name = e_split[1]
            local_name = local_name.replace(".","")
            
            e_split2 = local_name.split("+")
            if len(e_split2) > 1:
                e = e_split2[0] + "@" + domain_name
            else:
                e = local_name + "@" + domain_name
                
            result.append(e)
        print(result)
        return len(set(result))


      
S = Solution()
S.numUniqueEmails(Emails)