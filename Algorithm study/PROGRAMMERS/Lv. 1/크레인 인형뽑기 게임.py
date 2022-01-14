def solution(board, moves):
    answer = 0
    basket = [0]
    for j in range(len(moves)):
        for i in range(len(board)):
            if board[i][moves[j] - 1]:
                if basket[-1] == board[i][moves[j] - 1]:
                    basket.pop()
                    answer += 1
                else:
                    basket.append(board[i][moves[j] - 1])
                board[i][moves[j] - 1] = 0
                break
    return answer * 2


print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))