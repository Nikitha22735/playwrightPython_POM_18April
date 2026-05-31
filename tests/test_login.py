import json
import os

from playwright.sync_api import sync_playwright,expect
import pytest
from pages.homePage import homePage
from pages.loginPage import loginPage
from utils.jsonhandling import jsonhandling
from utils.excelhandling import handlingExcel

filePathJson = "testData/credentials.json"


@pytest.mark.login
def test_positiveLogin(page,launchAmazon,homePageObj,loginPageObj):
    creds = jsonhandling(filePathJson)
    homePageObj.clickOnAccountsNdList()
    # loginPageObj.enterEmailID(os.getenv("usname"))
    creds = handlingExcel()
    loginPageObj.enterEmailID(creds[1][0])
    loginPageObj.clickOnSubmit()
    loginPageObj.enterPassword(os.getenv("pw"))
    loginPageObj.clickOnSubmit()
    homePageObj.validateTheVisibilityOfSearchBox()
    

@pytest.mark.login
def test_email_negitiveLogin(page,launchAmazon,homePageObj,loginPageObj):
    homePageObj.clickOnAccountsNdList()
    loginPageObj.enterEmailID("trainingplaywright")
    loginPageObj.clickOnSubmit()
    loginPageObj.validateEmailError()
