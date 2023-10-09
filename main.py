from fastapi.testclient import TestClient
from fastapi import FastAPI,  UploadFile

app = FastAPI()


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}


client = TestClient(app)


def test_upload_image():
    files = {'file': ('nekroxmas.jpg', open("nekroxmas.jpg", 'rb'))}
    response = client.post("/uploadfile/", files=files)
    assert response.status_code == 200
    assert response.json() == {"filename": "nekroxmas.jpg"}

