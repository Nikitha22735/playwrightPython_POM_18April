import json

from playwright.sync_api import sync_playwright,expect
import pytest
from pages.homePage import homePage
from pages.loginPage import loginPage
from utils.jsonhandling import jsonhandling

filePathJson = "testData/credentials.json"


@pytest.mark.login
def test_positiveLogin(page,launchAmazon,homePageObj,loginPageObj):
    creds = jsonhandling(filePathJson)
    homePageObj.clickOnAccountsNdList()
    loginPageObj.enterEmailID(creds["email"])
    loginPageObj.clickOnSubmit()
    loginPageObj.enterPassword(creds["password"])
    loginPageObj.clickOnSubmit()
    homePageObj.validateTheVisibilityOfSearchBox()
    

@pytest.mark.login
def test_email_negitiveLogin(page,launchAmazon,homePageObj,loginPageObj):
    homePageObj.clickOnAccountsNdList()
    loginPageObj.enterEmailID("trainingplaywright")
    loginPageObj.clickOnSubmit()
    loginPageObj.validateEmailError()
