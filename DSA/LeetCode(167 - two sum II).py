# Pattern :  Arrary is sorted. To find sum by the two number, I use two pointers which calculte the from first digit and last digit. If the sum matches the target, it will be answer, if not then we check the whether sum is small or big and accordingly adjest index.
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        index1, index2 = 0, len(numbers)-1
        while index1 < index2:
            current = numbers[index1] + numbers[index2]
            if current == target:
                index1 +=1
                index2 +=1
                return [index1,index2]
            elif current < target:
                index1 += 1
            else:
                index2 -=1
        index1 +=1
        index2 +=1
        return []
