# 스파이들은 매일 다른 옷을 조합하여 입어 자신을 위장합니다.

# 예를 들어 스파이가 가진 옷이 아래와 같고 오늘 스파이가 동그란 안경, 긴 코트, 파란색 티셔츠를 입었다면 다음날은 청바지를 추가로 입거나 동그란 안경 대신 검정 선글라스를 착용하거나 해야 합니다.

# 종류	이름
# 얼굴	동그란 안경, 검정 선글라스
# 상의	파란색 티셔츠
# 하의	청바지
# 겉옷	긴 코트
# 스파이가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때 서로 다른 옷의 조합의 수를 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# clothes의 각 행은 [의상의 이름, 의상의 종류]로 이루어져 있습니다.
# 스파이가 가진 의상의 수는 1개 이상 30개 이하입니다.
# 같은 이름을 가진 의상은 존재하지 않습니다.
# clothes의 모든 원소는 문자열로 이루어져 있습니다.
# 모든 문자열의 길이는 1 이상 20 이하인 자연수이고 알파벳 소문자 또는 '_' 로만 이루어져 있습니다.
# 스파이는 하루에 최소 한 개의 의상은 입습니다.
# 입출력 예
# clothes	return
# [[yellow_hat, headgear], [blue_sunglasses, eyewear], [green_turban, headgear]]	5
# [[crow_mask, face], [blue_sunglasses, face], [smoky_makeup, face]]	3

# import itertools


def solution(clothes):
    obj = {}
    for item in clothes:
        thing = item[1]
        if thing in obj:
            obj[thing] += 1
        else:
            obj[thing] = 1

    many = 1
    for key in obj:
        many *= (obj[key] + 1)
    return many - 1

    # 경우의 수 개념이 약해서 고생했다.
    # 최소 하나는 고르는 경우의 수 => 각 케이스 별 경우의 수 + 1(이걸 안고르는 경우의 수)를 전부 곱한뒤 거기서 -1(아무것도 안고르는 경우의 수)

    # if len(obj) == 1:
    #     return len(clothes)
    # else:
    #     how_many = len(clothes)
    #     for num in range(2, len(obj)+1):
    #         temp_li = list(itertools.combinations(obj, num))
    #         temp_num = 0
    #         for arr in temp_li:
    #             ttemp_num = 1
    #             for idx in arr:
    #                 ttemp_num *= obj[idx]
    #             temp_num += ttemp_num
    #         how_many += temp_num
    #     return how_many
