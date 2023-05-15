from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def dfs(candidates, begin, size, path, res, target):
            if target == 0:
                res.append(path)
                return

            for index in range(begin, size):
                residue = target - candidates[index]
                if residue < 0:
                    break
                print('递归前 => {}，剩余 = {}'.format(path, target - candidates[index]))
                # dfs(candidates, index, size, path + [candidates[index]], res, residue)
                path = path + [candidates[index]]
                # path = path + [candidates[index]]
                dfs(candidates, index, size, path, res, residue)
                print('递归后 => {}'.format(path))

        size = len(candidates)
        if size == 0:
            return []
        candidates.sort()
        path = []
        res = []
        dfs(candidates, 0, size, path, res, target)
        return res
    
        
if __name__ == "__main__":
    result = Solution().combinationSum(candidates=[2,3,5], target=8)
    print(result)