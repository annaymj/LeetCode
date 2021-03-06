```
Given a date string in the form Day Month Year, where:

Day is in the set {"1st", "2nd", "3rd", "4th", ..., "30th", "31st"}.
Month is in the set {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"}.
Year is in the range [1900, 2100].
Convert the date string to the format YYYY-MM-DD, where:

YYYY denotes the 4 digit year.
MM denotes the 2 digit month.
DD denotes the 2 digit day.
 
Example 1:
Input: date = "20th Oct 2052"
Output: "2052-10-20"

Example 2:
Input: date = "6th Jun 1933"
Output: "1933-06-06"

Example 3:
Input: date = "26th May 1960"
Output: "1960-05-26"
```

month_dict = {"Jan":1, "Feb":2, "Mar":3, "Apr":4, "May":5, "Jun":6, 
              "Jul":7, "Aug":8, "Sep":9, "Oct":10, "Nov":11, "Dec":12}


class Solution:
    def reformatDate(self, date: str) -> str:
        day_str, month_str, year_str = date.split(' ')
        
        day_str = day_str[:-2]
        
        if len(day_str) == 1:
            day_str = "0" + day_str
        
        if len(str(month_dict[month_str]))  == 1:
            month_str = "0" + str(month_dict[month_str])
        else:
            month_str = str(month_dict[month_str])
        
        result = "-".join((year_str, month_str, day_str))
        
        return result
        
