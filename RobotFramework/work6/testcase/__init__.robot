*** Settings ***
Library  pylib.Resource.WebOpAdmin
Variables  cfg.py
Suite Setup  setupWebTest   ${url}
Suite Teardown  tearDownWebTest