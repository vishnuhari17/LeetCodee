def shortest_distance_to_character(s, c):
  """
  Given a string s and a character c that occurs in s, return an array of integers answer where answer.length == s.length and answer[i] is the distance from index i to the closest occurrence of character c in s.

  The distance between two indices i and j is abs(i - j), where abs is the absolute value function.

  Args:
    s: A string.
    c: A character.

  Returns:
    A list of integers representing the shortest distances from each index in s to the closest occurrence of c.
  """

  answer = [float("inf")] * len(s)
  prev_idx = -1
  for i, char in enumerate(s):
    if char == c:
      prev_idx = i
    answer[i] = min(answer[i], abs(i - prev_idx))

  return answer

s = "loveleetcode"
c = "e"

answer = shortest_distance_to_character(s, c)

print(answer)
