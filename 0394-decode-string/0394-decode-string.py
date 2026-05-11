class Solution:
    def decodeString(self, s):
        stack = []
        current_string = ""
        current_num = 0

        for ch in s:

            # If digit, build the number
            if ch.isdigit():
                current_num = current_num * 10 + int(ch)

            # If opening bracket
            elif ch == '[':
                stack.append((current_string, current_num))

                current_string = ""
                current_num = 0

            # If closing bracket
            elif ch == ']':
                prev_string, num = stack.pop()

                current_string = prev_string + num * current_string

            # Normal characters
            else:
                current_string += ch

        return current_string