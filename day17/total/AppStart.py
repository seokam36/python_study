# 서버 실행
from fastapi import FastAPI
import uvicorn
app = FastAPI()
if __name__ == "__main__":
    uvicorn.run( 'AppStart:app' ,
                 host="127.0.0.1" ,
                 port=8000 , reload=True )

# CORS 허용
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware ,
    allow_origins=["*"] ,
    allow_methods=["*"] ,
    allow_headers=["*"]
)

# 컨트롤러에 라우터 연결
import Controller
app.include_router( Controller.router )