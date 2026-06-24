
import pytest
from faker import Faker
from utils.jsonhandling import jsonhandling



def test_getApi(playwright):
    context = playwright.request.new_context()
    # response1 = context.get("https://dummyjson.com/token")
    # bearerToken = response1.json()
    response = context.get("https://dummyjson.com/products")
    # response = context.get("https://dummyjson.com/products", headers={"Authorization":"Bearer 123456"})
    # response = context.get("https://dummyjson.com/products", headers={"Authorization":f"Bearer ${bearerToken}"})
    response = context.get("https://dummyjson.com/products", headers={"Authorization":"Bearer 123456"}, params={"limit":5})
    print(response.status)
    assert response.status==200
    print(response.json())
    # responsebody = response.json()
    # print(responsebody["products"][0]["title"])
    # assert responsebody["products"][0]["title"]!=None


# @pytest.mark.api
def postApi(playwright):
    title = Faker.name()
    context = playwright.request.new_context()
    requestBody =jsonhandling("testData\\b1.json")
    requestBody["title"]=title
    response = context.post("https://dummyjson.com/products/add", headers={"Authorization":"Bearer 123456"}, data=requestBody)
    assert response.status ==201
    responseBody = response.json()
    print(responseBody["id"])
    return responseBody["id"], responseBody["price"]