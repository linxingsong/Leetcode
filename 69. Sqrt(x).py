class Solution:
    def mySqrt(self, x: int) -> int:
        #using function to sovle
        #return math.trunc(math.sqrt(x))

        #binary search

        if x <= 1:
            return x
        
        mid = x // 2
        upper_bound = x
        lower_bound = 0
        
        while lower_bound+1 != upper_bound:
            
            trial = mid ** 2
            next_trial = (mid+1)**2
            
            if trial <= x < next_trial:
                return mid
            elif trial > x:
                upper_bound = mid
                mid = ( lower_bound + upper_bound )// 2
            else:
                lower_bound = mid
                mid = ( lower_bound + upper_bound )// 2
                
        return lower_bound