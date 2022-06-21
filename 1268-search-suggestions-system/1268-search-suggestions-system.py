class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        search = ""
        answer = [[] for _ in range(len(searchWord))]
        length = 0
        for char in searchWord:
            search += char
            length += 1
            count = 0
            for product in products:
                if product[:length] == search:
                    answer[length-1].append(product)
                    count += 1
                if count == 3:
                    break
        return answer
                
            