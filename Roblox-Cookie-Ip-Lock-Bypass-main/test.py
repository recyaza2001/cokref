import requests

def fetch_session_csrf_token(roblosecurity_cookie):
    try:
        response = requests.post("https://auth.roblox.com/v2/logout", headers={
            'Cookie': f'.ROBLOSECURITY={roblosecurity_cookie}'
        })
        return None
    except requests.exceptions.RequestException as error:
        return error.response.headers.get("x-csrf-token", None)

def generate_auth_ticket(roblosecurity_cookie):
    try:
        csrf_token = fetch_session_csrf_token(roblosecurity_cookie)
        response = requests.post("https://auth.roblox.com/v1/authentication-ticket", headers={
            "x-csrf-token": csrf_token,
            "referer": "https://www.roblox.com/madebySynaptrixBitch",
            'Content-Type': 'application/json',
            'Cookie': f'.ROBLOSECURITY={roblosecurity_cookie}'
        })
        return response.headers.get('rbx-authentication-ticket', "Failed to fetch auth ticket")
    except requests.exceptions.RequestException:
        return "Failed to fetch auth ticket"

def redeem_auth_ticket(auth_ticket):
    try:
        response = requests.post("https://auth.roblox.com/v1/authentication-ticket/redeem", json={
            "authenticationTicket": auth_ticket
        }, headers={
            'RBXAuthenticationNegotiation': '1'
        })
        refreshed_cookie_data = response.headers.get('set-cookie', "")

        return {
            'success': True,
            'refreshedCookie': refreshed_cookie_data
        }
    except requests.exceptions.RequestException as error:
        return {
            'success': False,
            'robloxDebugResponse': error.response.json()
        }

def write_to_file(content, filename):
    with open(filename, 'w') as file:
        file.write(content)

# Example usage:
roblosecurity_cookie = "your_roblosecurity_cookie_here_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_1DDE93C78CF6E6D16CC00CA38C25B1F85E0FA2C99CEF2D430F9E13A51FE00D603352CFAFF1524E1288A126D245AEEAE3FE6D5550BE9660B61FC1D5143C8545E051F4E946FE51714A2DAE0ED62116C69A168FD3EA39F7DA11FB0EA21B5171CBBBFAB710B35AA1878CD757AEE37766C0EC668BDC64F2CFEFE25C0FFC6589221CF5E83AA33943B51B2EAA271B4550713EC294C0FDC8260CB624FD92DC82F8F94E74720FEC99A4197C7A4AC276107CBDD5012E105ABEFA1ED30327907BA385E4CB11D525CD6E340EDDA508C1229D42E9D45AA505D6E809122ECDAC5D637F456662A001DE8F448B66DBF556DAA8A5E33B469F3D4B0FFB5241CAE095956D2CEE45C7188C53608C25052B385FAC565D96BD9B54B1EB76C52CED23D3FFB8A86146A30C7FFA693987C320B6F3E96FC606158BC989A1BDA5EE36DD6D0C9CF2C2C325BBBA7551BE8AD6F163CE5BC37FC7D078990173ADB09D7D4C2AAF747E4392D9FAF919329CE298A94838083D2D8DF719A23CC48D1567E0669C20C6658C764B3F0E31B694DD135389FC6704B27B1AF4D166CA3294EFC2A12E2300F3DCC65110E51AC7BEB1014AD1206689CA6E504806800ED2343564E2C1FD613F8F32B6920DFF7BF23635A63E804EB68C7243A3E46B124A28C4A8565A899D71922835AC24955A9916E9D2B590A04B3704EF68E8C46DD4E94DFDAAB5EB321C5317DFB11648CD176DE7DDBE03B67197CC27CC451A7B35E06988588A27ED0BB886A070F5C607E7695DE696DB15EC89AA6653BF5C27F70C0942AE9456702B29C3C13EAEB9C0ADD27CCF8C117B4B4835202731E247C279AED8EFE00FF601061FCAE646FB2290BC11EEB954B23FF76AC065E079E334471A88621CF10A4D43322451E9CEDDD5D90AE9770971C2F4AC02A8942E4D7D21A1304593A1C66A51863B3C1AAC2C44319A4566ECAD99457EE911D3B3192198F98D57FB3599532B2E764C446C38280B00648B47755E6C66054D8BA1572D4B879DBC8CFC8777DB98AB33FD5CD7E826B1A45CD92BCD6AD3398B9DD2B433C6308CD07E34855FE22BBFB15782C515DD1B9DE4FCB438E802BCC470D60B9A0FAC86B4D6AF4584927E789B5E73413AAD"
auth_ticket = generate_auth_ticket(roblosecurity_cookie)
result = redeem_auth_ticket(auth_ticket)

# Write the result to a new text file
write_to_file(str(result), 'result.txt')

print(f"Result written to result.txt: {result}")