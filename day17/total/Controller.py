from fastapi import APIRouter

router = APIRouter(prefix='/api')

from Service import result_service

@router.post('/predict')
async def predict(item:dict):
    return result_service.predict(item)




