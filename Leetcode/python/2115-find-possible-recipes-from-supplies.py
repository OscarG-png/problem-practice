from typing import List


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        canCook = {s:True for s in supplies}
        recipeIndex = {r:i for i, r in enumerate(recipes)}

        def dfs(r):
            if r in canCook:
                return canCook[r]
            if r not in recipeIndex:
                return False

            canCook[r] = False
            for nei in ingredients[recipeIndex[r]]:
                if not dfs(nei):
                    return False
            canCook[r] = True
            return canCook[r]


        return [r for r in recipes if dfs(r)]
