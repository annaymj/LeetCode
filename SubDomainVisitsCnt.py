#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 13:53:00 2019

@author: annayu
Example 1:
Input: 
["9001 discuss.leetcode.com"]
Output: 
["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]
Explanation: 
We only have one website domain: "discuss.leetcode.com". 
As discussed above, the subdomain "leetcode.com" and "com" will also be visited. 
So they will all be visited 9001 times.

Example 2:
Input: 
["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
Output: 
["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
Explanation: 
We will visit "google.mail.com" 900 times, "yahoo.com" 50 times, "intel.mail.com" once 
and "wiki.org" 5 times. For the subdomains, we will visit "mail.com" 900 + 1 = 901 times, 
"com" 900 + 50 + 1 = 951 times, and "org" 5 times.



"""

import collections

cpdomains = ["9001 discuss.leetcode.com"]
cpdomains2 = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
cpdomains3 = ["900 google.mail.com", "5 wiki.org"]

class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        result = {}
        output = []
        
        for i in range(len(cpdomains)):
            num = cpdomains[i].split(" ")[0]
            domains = self.split_domain(cpdomains[i].split(" ")[1])
            
            # check if domain is already in the result dictionary
            for name in domains:
                if name not in result.keys():
                    result[name] = int(num)
                else:
                    result[name] += int(num)
                    
        for k in result.keys():
            output.append(str(result[k])+ " " + k)
        
        return output
            
    
    def split_domain(self,domain):
        domain_combination = []
        items = domain.split(".")
        
        for i in range(len(items)):
            name = '.'.join(items) 
            domain_combination.append(name)
            items.pop(0)
        
        return domain_combination
    
    def subdomainVisits2(self, cpdomains):
        ans = collections.Counter()
        for domain in cpdomains:
            count, domain = domain.split()
            count = int(count)
            frags = domain.split('.')
            for i in range(len(frags)):
                ans[".".join(frags[i:])] += count

        return ["{} {}".format(ct, dom) for dom, ct in ans.items()]
            
        
S = Solution()
S.subdomainVisits(cpdomains)    
S.subdomainVisits(cpdomains2)

S.subdomainVisits(cpdomains2)