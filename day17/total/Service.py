import pandas as pd
import joblib

class InsuranceService :

    def __init__( self ) :
        self.model = joblib.load( 'insurance.pkl' )
        self.metrics = joblib.load( 'insurance_metrics.pkl' )

    def predict( self , item ) :
        sample = pd.DataFrame( [ {
            'age'      : int( item['age'] ) ,
            'sex'      : item['sex'] ,
            'bmi'      : float( item['bmi'] ) ,
            'children' : int( item['children'] ) ,
            'smoker'   : item['smoker'] ,
            'region'   : item['region']
        } ] )

        charge = float( self.model.predict( sample )[0] )

        return {
            'charge'   : round( charge , 0 ) ,          # 연간 예상 의료비
            'monthly'  : round( charge / 12 , 0 ) ,     # 월 평균
            'r2'       : self.metrics['test_r2'] ,      # 테스트 R²
            'cv_r2'    : self.metrics['cv_r2']          # 교차검증 R²
        }



result_service = InsuranceService()