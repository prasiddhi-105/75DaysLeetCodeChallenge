class Solution:
    def totalFruit(self, fruits):
        left = 0
        basket = {}
        max_fruits = 0

        for right in range(len(fruits)):
            fruit = fruits[right]

            # Add fruit to basket
            basket[fruit] = basket.get(fruit, 0) + 1

            # If more than 2 fruit types, shrink window
            while len(basket) > 2:
                left_fruit = fruits[left]
                basket[left_fruit] -= 1

                if basket[left_fruit] == 0:
                    del basket[left_fruit]

                left += 1

            # Update maximum fruits collected
            max_fruits = max(max_fruits, right - left + 1)

        return max_fruits