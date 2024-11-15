import re
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
    def subname(self):
        return None
    def subschool(self):
        return None
    def encall(self):
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
    def __init__(self, strdump):
        self.strdump = strdump
    
    # 주민등록번호(Resident Number) 마스킹
    def maskres(self, rawText):
        p = re.compile(r'(\d{2})(0[1-9]|1[0-2])(0[1-9]|[1-2]\d|3[0-1])[-\s]?(1|2|3|4)(\d{6})')
        
        def checkBirth(match):
            date_of_birth = f"{match.group(1)}{match.group(2)}{match.group(3)}"
            gen = match.group(5)
            return f"{date_of_birth}-{gen}******"
        
        try:
            protectedText = p.sub(checkBirth, rawText)
            return protectedText
        except Exception as e:
            raise RuntimeError(f"Error Detected: {e}")

    # 전화번호(Phone Number) 마스킹
    def maskphone(self, rawText):
        p = re.compile()
        return protectedText