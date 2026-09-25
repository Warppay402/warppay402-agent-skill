import requests

MCP_ENDPOINT = "https://api.warppay402.com/"

def test_initialize():
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "initialize",
        "params": {
            "protocolVersion": "2024-11-05",
            "capabilities": {},
            "clientInfo": {"name": "TestAgent", "version": "1.0.0"}
        }
    }
    res = requests.post(MCP_ENDPOINT, json=payload)
    print("Initialize Status:", res.status_code)
    print("Response:", res.json())

if __name__ == "__main__":
    test_initialize()