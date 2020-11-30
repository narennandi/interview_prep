class Solution:
    def numberToWords(self, num):
        to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
        'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
        bigs = {1000000000:'Billion', 1000000:'Million', 1000:'Thousand'}

        def words(n):
            if n < 20:
                return to19[n-1:n]

            if n < 100:
                return [tens[n//10-2]] + words(n%10)
            if n < 1000:
                return [to19[n//100-1]] + ['Hundred'] + words(n%100)
            
            else:
                for i in [1000000000, 1000000, 1000]:
                    if n//i > 0:
                        return words(n//i) + [bigs[i]] + words(n%i)

        return ' '.join(words(num)) or 'Zero'

num = 95

res = Solution()
r = res.numberToWords(num)
print(r)