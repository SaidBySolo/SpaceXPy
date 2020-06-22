from .spacexclient import SpaceXClient
from .spacexmodel import SpaseXResponse

spacex = SpaceXClient()

class SpaceX():
        
    async def capsules(self, capsule_id:str= None, query=None, rawdata=False):
        return SpaseXResponse(await spacex.capsules(capsule_id,query), rawdata)
    
    async def company(self):
        return SpaseXResponse(await spacex.company())

    async def cores(self, core_id:str= None, query=None, rawdata=False):
        return SpaseXResponse(await spacex.cores(core_id, query), rawdata)
    
    async def crew(self, crew_id:str=None, query=None, rawdata=False):
        return SpaseXResponse(await spacex.crew(crew_id,query), rawdata)

    async def dragons(self, dragon_id:str= None, query=None, rawdata=False):
        return SpaseXResponse(await spacex.dragons(dragon_id, query), rawdata)

    async def landpads(self, landpad_id:str= None, query=None, rawdata=False):
        return SpaseXResponse(await spacex.landpads(landpad_id, query), rawdata)

    async def launches(self, schedule:str = None, launche_id:str= None, query=None, rawdata=False):
        return SpaseXResponse(await spacex.launches(schedule, launche_id, query), rawdata)

    async def launchpads(self, launchpad_id:str= None, query=None, rawdata=False):
        return SpaseXResponse(await spacex.launchpads(launchpad_id, query), rawdata)

    async def payloads(self, payload_id:str= None, query=None, rawdata=False):
        return SpaseXResponse(await spacex.payloads(payload_id, query), rawdata)

    async def roadster(self):
        return SpaseXResponse(await spacex.roadster())

    async def rockets(self, rocket_id:str= None, query=None, rawdata=False):
        return SpaseXResponse(await spacex.rockets(rocket_id, query), rawdata)

    async def ships(self, ship_id:str= None, query=None, rawdata=False):
        return SpaseXResponse(await spacex.ships(ship_id,query), rawdata)

    async def starlink(self, starlink_id:str= None, query=None, rawdata=False):
        return SpaseXResponse(await spacex.ships(starlink_id,query), rawdata)
