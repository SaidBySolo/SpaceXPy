import aiohttp

class Http():
    
    async def requests(self, method:str, endpoint:str, json=None):
        BaseURL = 'https://api.spacexdata.com/v4'
        url = BaseURL + endpoint
        async with aiohttp.ClientSession() as cs:
            async with aiohttp.request(method, url, json=json) as r:
                return await r.json()

    async def capsules(self, method:str, endpoint:str, json=None):
        return await self.requests(method, endpoint, json)

    async def company(self, method:str, endpoint:str, json=None):
        return await self.requests(method, endpoint, json)