import json

class Solution:
    def countNumberswith4(self, n : int) -> int:
        # code here
        if n<4:
            return 0
        elif n==4:
            return 1
        else:
            total = 0
            
            for i in range(n):
                i+=1
                for j in str(i):
                    if int(j) == 4:
                        total+=1
                        break
        
            return total

if __name__ == "__main__":

    with open('data.json', 'r') as file:
        data = json.load(file)

    correct = 0
    incorrect = 0

    errors = list()

    for sample in data['samples']:

        n = sample['n']

        obj = Solution()
        res = obj.countNumberswith4(n)

        if res == sample['count']:
            correct+=1
        else:
            incorrect+=1
            sample['yours'] = res
            errors.append(sample)
    
    print('Total Correct: ', correct)
    print('Total Incorrect: ', incorrect)

    if incorrect > 0:
        print('Incorrect Items:')
        print(errors)