import hashlib
from config import heuristicsNameData



"""
# 데이터 가명처리(Pseudonymization):
1) 휴리스틱 가명화
2) 암호화
3) 교환 방법
"""
class Pseudonymize:
    def __init__(self, objname, strdump):
        self.objname = objname
        self.strdump = strdump
    def heuristics(self):
        return None
    def encryptall(self):
        return None
    def swapall(self):
        return None



"""
# 데이터 총계처리(Aggregation):
1)총계처리
2)부분총계
3)라운딩
4)재배열
"""
class Aggregate:
    def __init__(self, objname, strdump):
        self.objname = objname
        self.strdump = strdump



"""
# 데이터 삭제(Data Reduction):
1)식별자 삭제
2)식별자 부분삭제
3)레코드 삭제
4)식별요소 전부삭제
"""
class ReduceDate:
    #hmm



"""
# 데이터 범주화(Data Suppression):
1)감추기
2)랜덤 라운딩
3)범위방법
4)제어 라운딩
"""
class SuppressData:
    #hmm



"""
# 데이터 마스킹(Masking):
1)임의 잡음 추가
2)공백과 대체
"""
class Mask:
    #hmm