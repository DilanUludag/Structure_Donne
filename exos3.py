class Solution:


    def topK(self, nums, k):
        # Step 1: Count the frequency of each element
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1


        # Step 2: Convert the dictionary into a list of tuples
        freq_list = [(key, value) for key, value in freq_map.items()]

        # Step 3: Sort the list based on frequency and the element itself
        freq_list.sort(key=lambda x: (x[1], -x[0]))
        print(freq_list)

        # Step 4: Extract the top k elements
        result = [freq_list[i][0] for i in range(k)]

        return result


if __name__ == '__main__':
        obj = Solution()
        ans = obj.topK([6 ,1, 1, 1, 2, 2, 3], 2)
        for i in ans:
            print(i, end=" ")
        print()

# } Driver Code Ends