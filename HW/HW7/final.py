import copy
if __name__ == '__main__':
    width, height = map(int, input().split())
    input_matrix = [[-1 for i in range(width)]for j in range(height)]
    for i in range(height):
        input_matrix[i] = list(map(int, input().split()))
    jumps = list(map(int, input().split()))
    #jumps.insert(0, 0)
    jumps.append(0)
    len_jump = len(jumps)
    for i in range(len_jump):
        if jumps[i]>=width-1 & jumps[i]>= height-1:
            jumps = jumps[0:i]
    len_jump = len(jumps)
    dp_plus = [] # s
    dp_minus = [] # s+1
    buffer_matrix = []
    #for k in range(len_jump):
    #   dp_plus.append([])
    for j in range(height):
        dp_plus.append([])
        dp_minus.append([])
        buffer_matrix.append([])
        for i in range(width):
            dp_plus[j].append(-1)
            dp_minus[j].append(-1)
            buffer_matrix.append(-1)
    #dp_plus = [[[0 for i in range(width)]for j in range(height)]for k in range(len_jump)]
    #for i in range(height):
    #    input_matrix_buffer = copy.deepcopy(input_matrix[i])
    #   dp_plus[0][i] = input_matrix_buffer
    #dp = dict()
    #dp[(0,0,0)] = input_matrix[0][0]
    dp_plus[0][0] = input_matrix[0][0]
    det_row = 0 # if i + det_row > width not need to jump anymore 0 can jump
    det_col = 0 # 0 can jump, 1 can't jump
    det = 0
    det_break_jump = 0
    det_jump = 1
    mini = 100000000000000
    for s in range(len_jump):
        if (dp_plus[height - 1][width - 1] != -1):
            mini = min(mini, dp_plus[height - 1][width - 1])
        det_row = 0
        if (det_jump == 0 ):
            break
        det_jump = 0
        dp_plus = copy.deepcopy(dp_minus)
        dp_minus = copy.deepcopy(buffer_matrix)
        for i in range(height):
            det_col = 0
            if i + jumps[s] + 1 > height - 1: # can't jump row for now
                det_row = 1
            for j in range(width):
                if j + jumps[s] + 1 > width - 1: # col can't jump for now
                    det_col = 1
                if dp_plus[i][j] != -1:
                    if det_col == 1: # col can't jump
                        if det_row == 0: # row can jump
                            if j == width - 1: # col can't walk
                                # if i < height - jumps[s] - 1: # can jump
                                if dp_plus[i+1][j] == -1:
                                    dp_plus[i+1][j] = dp_plus[i][j] + input_matrix[i+1][j]
                                    #dp[(i+1,j,s)] = dp[(i,j,s)] + input_matrix[i+1][j]
                                else:
                                    dp_plus[i + 1][j] = min(dp_plus[i+1][j],dp_plus[i][j]+input_matrix[i+1][j])
                                    #dp[(i+1,j,s)] = min(dp[(i+1,j,s)],dp[(i,j,s)] + input_matrix[i+1][j])
                                if s!= len_jump-1:
                                    if dp_minus[i+jumps[s]+1][j] == -1:
                                        dp_minus[i + jumps[s] + 1][j] = dp_plus[i][j] + input_matrix[i + jumps[s] + 1][j]
                                        #dp[(i+jumps[s]+1,j,s+1)] == -2
                                        det_jump = 1
                                    else:
                                        if dp_minus[i+jumps[s]+1][j] >= dp_plus[i][j] + input_matrix[i + jumps[s] + 1][j]:
                                            dp_minus[i + jumps[s] + 1][j] = dp_plus[i][j] + input_matrix[i + jumps[s] + 1][j]
                                            det_jump = 1
                            else: # col can walk
                                if dp_plus[i+1][j] == -1:
                                    dp_plus[i + 1][j] = dp_plus[i][j] + input_matrix[i + 1][j]
                                    #dp[(i+1,j,s)] == -2
                                #except:
                                    #dp[(i+1,j,s)] = dp[(i,j,s)] + input_matrix[i+1][j]
                                else:
                                    dp_plus[i+1][j] = min(dp_plus[i+1][j],dp_plus[i][j] + input_matrix[i + 1][j])
                                #try:
                                    #dp[(i,j+1,s)] == -2
                                if dp_plus[i][j+1] == -1:
                                    dp_plus[i][j+1] = dp_plus[i][j] + input_matrix[i][j+1]
                                #except:
                                    #dp[(i,j+1,s)] = dp[(i,j,s)] + input_matrix[i][j+1]
                                else:
                                    #dp[(i,j+1,s)] = min(dp[(i,j+1,s)],dp[(i,j,s)] + input_matrix[i][j+1])
                                    dp_plus[i][j + 1] = min(dp_plus[i][j+1],dp_plus[i][j] + input_matrix[i][j+1])
                                #try:
                                    #dp[(i+jumps[s]+1,j,s+1)] == -2
                                if s != len_jump - 1:
                                    if dp_minus[i+jumps[s]+1][j] == -1:
                                        dp_minus[i + jumps[s] + 1][j] = dp_plus[i][j] + input_matrix[i + jumps[s] + 1][j]

                                        #except:
                                        #dp[(i + jumps[s] + 1, j, s + 1)] = dp[(i, j, s)] + input_matrix[i + jumps[s] + 1][j]
                                        det_jump = 1
                                    else:
                                        if dp_minus[i + jumps[s] + 1][j] >= dp_plus[i][j] + input_matrix[i + jumps[s] + 1][j]:
                                            dp_minus[i + jumps[s] + 1][j] = min(dp_minus[i + jumps[s] + 1][j],dp_plus[i][j] + input_matrix[i + jumps[s] + 1][j])
                                            det_jump = 1
                        else: # det_row = 1 row can't jump
                            if j == width - 1: # col can't walk
                                if i != height - 1: # row can walk
                                    if dp_plus[i+1][j] == -1:
                                        dp_plus[i + 1][j] = dp_plus[i][j] + input_matrix[i+1][j]
                                    else:
                                        dp_plus[i+1][j] = min(dp_plus[i+1][j],dp_plus[i][j] + input_matrix[i+1][j])
                            else: # col can walk
                                if i != height - 1: # row can walk
                                    if dp_plus[i + 1][j] == -1:
                                        dp_plus[i + 1][j] = dp_plus[i][j] + input_matrix[i + 1][j]
                                    else:
                                        dp_plus[i + 1][j] = min(dp_plus[i + 1][j],
                                                                   dp_plus[i][j] + input_matrix[i + 1][j])
                                    if dp_plus[i][j + 1] == -1:
                                        dp_plus[i][j + 1] = dp_plus[i][j] + input_matrix[i][j + 1]
                                    # except:
                                    # dp[(i,j+1,s)] = dp[(i,j,s)] + input_matrix[i][j+1]
                                    else:
                                        # dp[(i,j+1,s)] = min(dp[(i,j+1,s)],dp[(i,j,s)] + input_matrix[i][j+1])
                                        dp_plus[i][j + 1] = min(dp_plus[i][j + 1],
                                                                   dp_plus[i][j] + input_matrix[i][j + 1])
                                else: # row can't walk

                                    if dp_plus[i][j + 1] == -1:
                                        dp_plus[i][j + 1] = dp_plus[i][j] + input_matrix[i][j + 1]
                                    # except:
                                    # dp[(i,j+1,s)] = dp[(i,j,s)] + input_matrix[i][j+1]
                                    else:
                                        # dp[(i,j+1,s)] = min(dp[(i,j+1,s)],dp[(i,j,s)] + input_matrix[i][j+1])
                                        dp_plus[i][j + 1] = min(dp_plus[i][j + 1],
                                                                   dp_plus[i][j] + input_matrix[i][j + 1])

                    else: # det_col = 0, col can jump
                        if det_row == 0:# row can jump
                            if dp_plus[i + 1][j] == -1:
                                dp_plus[i + 1][j] = dp_plus[i][j] + input_matrix[i + 1][j]
                            else:
                                dp_plus[i + 1][j] = min(dp_plus[i + 1][j],
                                                           dp_plus[i][j] + input_matrix[i + 1][j])
                            if dp_plus[i][j + 1] == -1:
                                dp_plus[i][j + 1] = dp_plus[i][j] + input_matrix[i][j + 1]
                            # except:
                            # dp[(i,j+1,s)] = dp[(i,j,s)] + input_matrix[i][j+1]
                            else:
                                # dp[(i,j+1,s)] = min(dp[(i,j+1,s)],dp[(i,j,s)] + input_matrix[i][j+1])
                                dp_plus[i][j + 1] = min(dp_plus[i][j + 1],
                                                           dp_plus[i][j] + input_matrix[i][j + 1])
                            if s != len_jump - 1:
                                if dp_minus[i + jumps[s] + 1][j] == -1:
                                    dp_minus[i + jumps[s] + 1][j] = dp_plus[i][j] + input_matrix[i + jumps[s] + 1][
                                        j]

                                    # except:
                                    # dp[(i + jumps[s] + 1, j, s + 1)] = dp[(i, j, s)] + input_matrix[i + jumps[s] + 1][j]
                                    det_jump = 1
                                else:
                                    if dp_minus[i + jumps[s] + 1][j] >= dp_plus[i][j] + \
                                            input_matrix[i + jumps[s] + 1][j]:
                                        dp_minus[i + jumps[s] + 1][j] = min(dp_minus[i + jumps[s] + 1][j],
                                                                                  dp_plus[i][j] +
                                                                                  input_matrix[i + jumps[s] + 1][j])
                                        det_jump = 1
                            #try:
                                #dp[(i, j + jumps[s] + 1, s + 1)] == -2
                                if dp_minus[i][j+jumps[s]+1] == -1:
                                #except:
                                    #dp[(i, j + jumps[s] + 1, s + 1)] = dp[(i, j, s)] + input_matrix[i][j+ jumps[s] + 1]
                                    dp_minus[i][j + jumps[s] + 1] = dp_plus[i][j] + input_matrix[i][j + jumps[s] + 1]
                                    det_jump = 1
                                else:
                                    if dp_minus[i][j + jumps[s] + 1] >= dp_plus[i][j] + input_matrix[i][j + jumps[s] + 1]:
                                        dp_minus[i][j + jumps[s] + 1] = dp_plus[i][j] + input_matrix[i][j + jumps[s] + 1]
                                        det_jump = 1
                        else: # det_row = 1  row can't jump
                            if i == height - 1:  # row can't walk
                                if dp_plus[i][j + 1] == -1:
                                    dp_plus[i][j + 1] = dp_plus[i][j] + input_matrix[i][j + 1]
                                # except:
                                # dp[(i,j+1,s)] = dp[(i,j,s)] + input_matrix[i][j+1]
                                else:
                                    # dp[(i,j+1,s)] = min(dp[(i,j+1,s)],dp[(i,j,s)] + input_matrix[i][j+1])
                                    dp_plus[i][j + 1] = min(dp_plus[i][j + 1],
                                                               dp_plus[i][j] + input_matrix[i][j + 1])
                                if s != len_jump - 1:
                                    if dp_minus[i][j + jumps[s] + 1] == -1:
                                        # except:
                                        # dp[(i, j + jumps[s] + 1, s + 1)] = dp[(i, j, s)] + input_matrix[i][j+ jumps[s] + 1]
                                        dp_minus[i][j + jumps[s] + 1] = dp_plus[i][j] + input_matrix[i][
                                            j + jumps[s] + 1]
                                        det_jump = 1
                                    else:
                                        if dp_minus[i][j + jumps[s] + 1] >= dp_plus[i][j] + input_matrix[i][
                                            j + jumps[s] + 1]:
                                            dp_minus[i][j + jumps[s] + 1] = dp_plus[i][j] + input_matrix[i][
                                                j + jumps[s] + 1]
                                            det_jump = 1
                            else:  # row can walk
                                if dp_plus[i + 1][j] == -1:
                                    dp_plus[i + 1][j] = dp_plus[i][j] + input_matrix[i + 1][j]
                                else:
                                    dp_plus[i + 1][j] = min(dp_plus[i + 1][j],
                                                               dp_plus[i][j] + input_matrix[i + 1][j])

                                if dp_plus[i][j + 1] == -1:
                                    dp_plus[i][j + 1] = dp_plus[i][j] + input_matrix[i][j + 1]
                                # except:
                                # dp[(i,j+1,s)] = dp[(i,j,s)] + input_matrix[i][j+1]
                                else:
                                    # dp[(i,j+1,s)] = min(dp[(i,j+1,s)],dp[(i,j,s)] + input_matrix[i][j+1])
                                    dp_plus[i][j + 1] = min(dp_plus[i][j + 1],
                                                               dp_plus[i][j] + input_matrix[i][j + 1])
                                if s != len_jump - 1:
                                    if dp_minus[i][j + jumps[s] + 1] == -1:
                                        # except:
                                        # dp[(i, j + jumps[s] + 1, s + 1)] = dp[(i, j, s)] + input_matrix[i][j+ jumps[s] + 1]
                                        dp_minus[i][j + jumps[s] + 1] = dp_plus[i][j] + input_matrix[i][
                                            j + jumps[s] + 1]
                                        det_jump = 1
                                    else:
                                        if dp_minus[i][j + jumps[s] + 1] >= dp_plus[i][j] + input_matrix[i][
                                            j + jumps[s] + 1]:
                                            dp_minus[i][j + jumps[s] + 1] = dp_plus[i][j] + input_matrix[i][
                                                j + jumps[s] + 1]
                                            det_jump = 1

    # renew near element
    #for i in range(height):
    #    for j in range(width):

    #mini = dp_plus[0][height-1][width-1]
    #for i in range(len_jump):
    #    if dp_plus[i][height-1][width-1] != -1:
    #        if mini > dp_plus[i][height-1][width-1]:
    #            mini = dp_plus[i][height-1][width-1]
    print(mini)
