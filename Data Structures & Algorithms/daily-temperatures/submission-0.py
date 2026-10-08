class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
      result = [0]* len(temperatures)

      monotonic_stack = []
      for i, v in enumerate(temperatures):
        while monotonic_stack and v > monotonic_stack[-1][0]:
          temp, day = monotonic_stack.pop()
          result[day] = i - day

        monotonic_stack.append((v, i))

      return result