class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
    
        for i in range(len(nums)):
            # Zbiór elementów widzianych przed aktualnym i
            seen = {}  # wartość -> indeks (wystarczy zbiór)
        
            for j in range(i + 1, len(nums)):
                third = -(nums[i] + nums[j])
            
                if third in seen:
                # Zamrożony tuple posortowanych 3 elementów – eliminuje duplikaty
                    triplet = tuple(sorted([nums[i], nums[j], third]))
                    result.add(triplet)
            
                seen[nums[j]] = j  # dodaj nums[j] do seen PO sprawdzeniu
    
        return [list(t) for t in result]