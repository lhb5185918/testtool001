import requests
import time

header = {
    "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX25hbWUiOiJsaGIiLCJjcmVhdGVkIjoxNzE2Nzk0MDA2ODg0LCJjb21wYW55TmFtZSI6IumdkuWym-eZvua0i-WMu-iNr-iCoeS7veaciemZkOWFrOWPuCIsImNvbXBhbnlTaG9ydE5hbWUiOiLpnZLlspvnmb7mtIvljLvoja_ogqHku73mnInpmZDlhazlj7giLCJ1c2VySWQiOjE3MDk1OTkwNzA4Njc5NjgsInN1cHBlciI6dHJ1ZSwid2FyZWhvdXNlTmFtZSI6IumdkuWym-S7kyIsImNsaWVudF9pZCI6Imlvd3RiIiwid2FyZWhvdXNlQ29kZSI6IlFEQyIsInVzZXJMYW5ndWFnZSI6InpoLUNOIiwidXNlcl9ubyI6ImxoYiIsImN1cnJlbnRfdXNlcl9uYW1lIjoi5p2O6bi_5a6-IiwiYXVkIjpbInpocWMiXSwiY29tcGFueUlkIjo4MTc5MjY5Mzg0NjQ3NjgsImxvZ2luVGltZSI6MTcxNjc5NDAwNjI2MCwibW9kaWZ5VGltZSI6MTcxMzc3NjI2OTAwMCwid2FyZWhvdXNlSWQiOiI4MTc5Mjk5NDAzNDEyNDgiLCJzY29wZSI6WyJhbGwiXSwiY29tcGFueV9jb2RlIjoiUURCWVlZR0YiLCJleHAiOjE3NTI3OTQwMDYsInBsYXRGb3JtIjoiV2ViIiwianRpIjoiNTk4NjEzOTAtMWEwZi00OWIxLTlkNGItYTJlNzY4ZmU3MTVmIiwiZGF0YVBlcm1pc3Npb24iOiJ7fSJ9.fMCVcwhG2ZoLqrC0XJCZTT-i83bBs4lAmZtnmwHt0WG3xdU15dJXgVF7umtlywNhlo02n5B_WHnVTbx2jeSejEyEaa7299eQZ9Ba43PibazG-Fo6bz411ESyp_vgNxZHs2YvFMV6mwouh8S8IwFDLQrZH8-Mi4rac6DSqMDIf9IWiwslnC15BLCqRNz07YDEHIEGKjtcdOlzyD-pXUCmI6eLaTUzd-sk8TEkqxnte8LCNSr66viAupEQeN6mestAQXEhELr_2rbLt9B2TKloKjaJxebewLlIcTwjxEVcOEPdqoB5XowFbpXaurgI9qE8ja2dFIsW37sLVqOKbWJbfw"}

for i in range(100, 217):
    data = {"isEnable": 1, "workStatus": 10, "equipmentCode": "8012010{}".format(i), "rfid": "8012010{}".format(i),
            "equipmentName": "冰排",
            "iceRowCategoryId": "1758998406582784", "coldStorageDuration": 1, "releaseColdDuration": 1,
            "releaseColdDurationMax": None, "weight": None, "innerLength": None, "innerWidth": None,
            "innerHeight": None,
            "innerVolume": None, "externalLength": None, "externalWidth": None, "externalHeight": None,
            "externalVolume": None, "factoryModel": None, "phaseTransitionTemperature": None, "imageList": []}
    res = requests.post(url="http://bswms-uat-01.baheal.com:7777/bp/base/iceRowInfo/add", json=data, headers=header)
    print(res.json())
