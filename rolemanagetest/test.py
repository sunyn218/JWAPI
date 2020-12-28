import requests

url = "http://122.144.131.129:5190/api/cloud/Permisssion/newRole"

payload = 'role_name=4546&role_area=021002'
headers = {
    'X-Token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL3VzZXJkYXRhIjoie1wiSWRcIjoxLFwiVXNlck5hbWVcIjpcImFkbWluXCIsXCJOYW1lXCI6XCLnrqHnkIblkZhcIixcIlBob25lTnVtYmVyXCI6bnVsbCxcIkVtYWlsXCI6bnVsbCxcIkFyZWFJZFwiOlwiLTFcIixcIklzQWN0aXZlZFwiOjEsXCJDcmVhdGlvblRpbWVcIjpcIjIwMjAtMTEtMjMgMTg6Mzg6MDBcIixcIkRlc2NyaXB0aW9uXCI6bnVsbH0iLCJuYmYiOjE2MDc1MTA4NDcsImV4cCI6MTYwNzUxNjI0NywiaXNzIjoiaHR0cDovL3d3dy5qd2FpLXRlY2guY29tLyIsImF1ZCI6Imh0dHA6Ly93d3cuandhaS10ZWNoLmNvbS8ifQ.AhMumxXgIDv6b9Xu0ML3xCeCo0LF44Lnh1CHahL30kI',
    'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
