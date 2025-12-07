input_array = [
  [4077, 5314],
  [527473787, 527596071],
  [709, 872],
  [2487, 3128],
  [6522872, 6618473],
  [69137, 81535],
  [7276, 8396],
  [93812865, 93928569],
  [283900, 352379],
  [72, 83],
  [7373727756, 7373754121],
  [41389868, 41438993],
  [5757, 6921],
  [85, 102],
  [2, 16],
  [205918, 243465],
  [842786811, 842935210],
  [578553879, 578609405],
  [9881643, 10095708],
  [771165, 985774],
  [592441, 692926],
  [7427694, 7538897],
  [977, 1245],
  [44435414, 44469747],
  [74184149, 74342346],
  [433590, 529427],
  [19061209, 19292668],
  [531980, 562808],
  [34094, 40289],
  [4148369957, 4148478173],
  [67705780, 67877150],
  [20, 42],
  [8501, 10229],
  [1423280262, 1423531012],
  [1926, 2452],
  [85940, 109708],
  [293, 351],
  [53, 71]

#  [1, 2],
#  [995, 1000]

#   [11, 22],
#   [95, 115],
#   [998, 1012],
#   [1188511880, 1188511890],
#   [222220, 222224],
#   [1698522, 1698528],
#   [446443, 446449],
#   [38593856, 38593862],
#   [565653, 565659],
#   [824824821, 824824827],
#   [2121212118, 2121212124]
]

sum = 0
for idx, arr in enumerate(input_array):
    mismatch = False
    for id in range(arr[0], arr[1]+1):
        mismatch = False
        s = str(id)
        ch1 = s[0]
        s_need = s[1:]
        pattern_len = 0

        if(len(s)%2 == 0):
            n = int(len(s)/2)
            if(s[0:n] == s[n:]):
                sum+=id
                continue
        # print(s, ch1, s_need)

        for i,ch in enumerate(s_need):
            if ch == ch1:
                pattern_len = i+1
                break

        # print(pattern_len)
        if pattern_len == 0:
            continue
        
        s_pattern = s[0:pattern_len]
        pattern_len = len(s_pattern)
        
        repetition_count = len(s) / pattern_len

        if len(s) != int(repetition_count) * pattern_len:
            continue
        repetition_count = int(repetition_count)

        # print(s_pattern, pattern_len, repetition_count)

        for i in range(pattern_len, len(s), pattern_len):

            if s_pattern != s[i:(i+pattern_len)]:
                mismatch = True
                # print(mismatch)
            # print(s_pattern, s[i:(i+pattern_len)]) 

        # print(mismatch)
        if not mismatch:
            print(id)
            sum+=id
            print("cumul sum", sum)
        # print(sum)
            
print("finalSum=", sum)


