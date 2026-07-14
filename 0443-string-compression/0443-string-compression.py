class Solution:
    def compress(self, chars: List[str]) -> int:
        left = 0
        right = 0

        while right < len(chars):
            current_chars = chars[right]
            count = 0

            while right < len(chars) and chars[right] == current_chars:
                right += 1
                count += 1

            chars[left] = current_chars
            left += 1

            if count > 1:
                for digit in str(count):
                    chars[left] = digit
                    left += 1

        return left


        