movie_rank = ["극한직업", "아바타", "범죄도시"]

# 리스트에 원소 추가
movie_rank.append("배트맨")
print(movie_rank)

# 특정 위치에 값을 끼워넣기
movie_rank.insert(1, "슈퍼맨")  #insert(인덱스, 원소)
print(movie_rank)

# 리스트 데이터 삭제
del movie_rank[3]
print(movie_rank)

# 리스트의 데이터 개수
print(len(movie_rank))

# 리스트의 평균 구하기
nums = [1,2,3,4,5]
average = sum(nums) / len(nums)
print(average)