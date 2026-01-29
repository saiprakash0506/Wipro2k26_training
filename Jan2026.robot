*** Settings ***
Library           SeleniumLibrary

*** Keywords ***
Open Application
    Open Browser    https://example.com    edge
    Maximize Browser Window

*** Test Cases ***
test1.robot
    Open Browser    https://www.google.com    edge
    Title Should Be    Google
    Close Browser
