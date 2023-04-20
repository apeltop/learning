# https://school.programmers.co.kr/learn/courses/30/lessons/178871

def solution(players, callings):
    answer = list(players)
    player_rating = {player: i for i, player in enumerate(players)}

    for calling in callings:
        called_player_index = player_rating[calling]
        player_rating[calling], player_rating[answer[called_player_index - 1]] = called_player_index - 1, called_player_index

        answer[called_player_index], answer[called_player_index - 1] = answer[called_player_index - 1], answer[called_player_index]

    return answer


print(solution(["mumu", "soe", "poe", "kai", "mine"],
               ["kai", "kai", "mine", "mine"]))  # ["mumu", "kai", "mine", "soe", "poe"]
