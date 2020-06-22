import aiohttp

class Http():
    
    async def request(self, method:str, endpoint:str, json=None):
        BaseURL = 'https://api.spacexdata.com/v4'
        url = BaseURL + endpoint
        async with aiohttp.ClientSession() as cs:
            async with aiohttp.request(method, url, json=json) as r:
                return await r.json()

    async def capsules(self, method:str, endpoint:str, json=None):
        return await self.request(method, endpoint, json)

    async def company(self, method:str, endpoint:str):
        return await self.request(method, endpoint)

    async def capsules(self, method:str, endpoint:str, json=None):
        return await self.request(method, endpoint, json)

    async def cores(self, method:str, endpoint:str, json=None):
        return await self.request(method, endpoint, json)

    async def crew(self, method:str, endpoint:str, json=None):
        return await self.request(method, endpoint, json)

    async def dragons(self, method:str, endpoint:str, json=None):
        return await self.request(method, endpoint, json)

    async def launches(self, method:str, endpoint:str, json=None):
        return await self.request(method, endpoint, json)

    async def launchpads(self, method:str, endpoint:str, json=None):
        return await self.request(method, endpoint, json)

    async def roadster(self, method:str, endpoint:str, json=None):
        return await self.request(method, endpoint, json)

    async def rockets(self, method:str, endpoint:str, json=None):
        return await self.request(method, endpoint, json)

    async def ships(self, method:str, endpoint:str, json=None):
        return await self.request(method, endpoint, json)

    async def starlink(self, method:str, endpoint:str, json=None):
        return await self.request(method, endpoint, json)