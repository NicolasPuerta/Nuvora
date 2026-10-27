
# Build-in library
import os
import uvicorn

# Librerias externas
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Propias libraries
from core.enviroments import ENV


app = FastAPI(
    title='Nuvora API',
    version='0.1.0',
)

origins = ENV.url_allowed_cors

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


for root, dirs, files in os.walk('routers'):
    if '__' not in root:
        path = root.split(os.sep)
        for file in files:
            if '__' not in file:
                file, _ = os.path.splitext(file)
                path_import = f'{".".join(path)}.{file}'
                module = __import__(path_import, globals(), locals(), [f'{file}_router'])
                router = getattr(module, f'{file}_router')
                app.include_router(router)


if __name__ == '__main__':
    uvicorn.run(app)
