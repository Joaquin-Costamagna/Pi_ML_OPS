from fastapi import FastAPI
from funciones import developer
from funciones import userdata
#from funciones import UserForGenre --  NO PUDE LLEVARLA A CABO
from funciones import best_developer_year
from funciones import developer_reviews_analysis


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/best_developer_year/{year}")
async def Best_developer_year(year: str):
    try:
        year_int = int(year)
        result4 = best_developer_year(year_int)
        return result4
    except Exception as e:
        return {"error": str(e)}
    
'''    
@app.get("/UserForGenre/{genero}")
async def UserForGenre(genero: str):
    try:
        result = UserForGenre(genero)
        return result
    except Exception as e:
        return {"error": str(e)}
'''

@app.get("/userdata/{user_id}")
async def userdata_handler(user_id: str):
    try:
        result2 = userdata(user_id)
        return result2
    except Exception as e:
        return {"error": str(e)}


@app.get("/developer/{desarrollador}")
async def developer_def(desarrollador: str):
    result1 = developer(desarrollador)
    return result1 


@app.get("/developer_reviews_analysis/{desarrolladora}")
async def developer_def(desarrolladora: str):
    result5 = developer_reviews_analysis(desarrolladora)
    return result5 
