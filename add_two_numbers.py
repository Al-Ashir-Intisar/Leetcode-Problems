class Solution(object):
    def addTwoNumbers(self, l1, l2):

        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        added_list = []
        carry_on = 0
        lenght_l1 = len(l1)
        lenght_l2 = len(l2)
        if lenght_l1 > lenght_l2:
            length = lenght_l1
            i = lenght_l2
            while i < lenght_l1:
                l2.append(0)
                i += 1
        elif lenght_l1 == lenght_l2:
            length = lenght_l1
            l1.append(0)
            l2.append(0)
        else:
            length = lenght_l2
            j = lenght_l1
            while j < lenght_l2:
                l1.append(0)
                j += 1

        
        print(l1, l2)
        for i in range(length):
            added = l1[i] + l2[i] + carry_on
            to_add = added
            carry_on = 0
            if added >= 10:
                carry_on = 1
                to_add = added - 10
            added_list.append(to_add)
        if carry_on == 1:
            added_list.append(carry_on)
        
        #print(carry_on)
        print(l1, l2, added_list)


solution = Solution()
solution.addTwoNumbers([9,9,9,9,9,9,9], [9,9,9,9])