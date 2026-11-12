# 비즈니스 로직 == AI 모델 예측
import pandas as pd

class ItemService:
    def __init__(self): # 생성자
        self.df = pd.DataFrame([ # self.변수명 = 값
            {'id':1, 'name':'콜라','price':1000},
            {'id':2, 'name':'사이다','price':1500}
        ])

    # 함수
    def items(self):
        # df.to_dict(orient='records') -> 행 마다 딕셔너리 변환 하여 리스트 반환 함수
        return self.df.to_dict(orient='records')

    def save(self,item):
        # 1. 저장할 딕셔너리를 df 변경
        save_df = pd.DataFrame([item])
        # 2. 기존 df에 연결 , .pd.concat()
        self.df = pd.concat([self.df, save_df], ignore_index=True)
        return True

    def update(self,item):
        uid = item.get('id')    # 1. 수정할 id조회
        if uid not in self.df['id'].values: # 2. 현재 df 입력받은 수정할 id가 없으면
            return False
        idx = self.df[self.df['id'] == uid].index # 3. 현재 df에 입력받은 수정할 id가 같다면 index조회
        # 4. 찾은 인덱스에 값 수정
        # items.keys() : 딕셔너리.keys() -> [속성명, 속성명]
        self.df.loc[idx , item.keys()] = item.values()
        return True
# 서비스 객체 생성
item_service = ItemService()
