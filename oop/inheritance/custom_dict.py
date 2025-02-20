class LongNameDict(dict[str, int]):
    def longest_key(self) -> str:
        longest = None
        for key in self:
            if longest is None or len(key) > len(longest):
                longest = key
        return longest

articles_read = LongNameDict()
articles_read['lucy'] = 42
articles_read['c_c_phillips'] = 6
articles_read['steve'] = 7
print(articles_read.longest_key())
# This is a built-in method that does the same thing as 'longest_key'
print(max(articles_read, key = len))

