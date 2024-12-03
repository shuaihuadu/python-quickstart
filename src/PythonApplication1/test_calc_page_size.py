class Part:
    start_part: int
    end_part: int

    def __init__(self, start_part, end_part):
        self.start_part = start_part
        self.end_part = end_part


def calc_actual_start_end(part: Part):
    page_size = part.end_part - part.start_part + 1
    return 1, page_size


result1 = calc_actual_start_end(Part(1, 10))
print(result1)
result2 = calc_actual_start_end(Part(11, 20))
print(result2)
result3 = calc_actual_start_end(Part(21, 30))
print(result3)
result4 = calc_actual_start_end(Part(31, 40))
print(result4)
result5 = calc_actual_start_end(Part(41, 50))
print(result5)
result6 = calc_actual_start_end(Part(51, 60))
print(result6)
result7 = calc_actual_start_end(Part(61, 70))
print(result7)
result8 = calc_actual_start_end(Part(71, 78))
print(result8)
print(result1[0])
print(result1[1])

input("Press Enter to continue...")