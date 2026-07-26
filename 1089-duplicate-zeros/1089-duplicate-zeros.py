class Solution(object):
    def duplicateZeros(self, arr):
        i = -1
        vir = 0
        while vir<len(arr):
            i += 1
            if arr[i] == 0:
                vir += 2
            else:
                vir += 1
        i -= len(arr)
        j = -1
        if vir > len(arr):
            arr[j] = 0
            i -= 1
            j -= 1
        while i >= -len(arr) and j >= -len(arr):
            if arr[i] != 0:
                arr[j] = arr[i]    
                j -= 1
            else:
                arr[j],arr[j-1] = 0,0
                j -=2
            i -= 1
        return arr