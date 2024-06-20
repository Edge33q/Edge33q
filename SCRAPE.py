import httpx, aiohttp

with open("proxy.txt", 'a') as file:
    file.write(httpx.get("https://tools.digitalstress.net/proxy?key=824b9398230e9e0f41d19559dfb99722&type=http").text)