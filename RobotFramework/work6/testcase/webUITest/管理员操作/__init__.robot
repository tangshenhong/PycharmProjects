*** Settings ***
Library  pylib.Resource.WebOpAdmin
Variables  cfg.py
Suite Setup  loginWebSite   ${username}  ${passwd}
