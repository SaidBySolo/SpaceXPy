from spacexpy.spacexhttp import Http
from .spacexerror import *


class SpaceXRequester(Http):
    def check_argument(self, args: list):
        if len(list(filter(None.__ne__, args))) >= 2:
            raise UnexpectedArguments(
                "Only one argument is required but received more than one"
            )

    async def request_capsules(self, capsule_id: str = None, query=None):
        self.check_argument([capsule_id, query])
        if capsule_id is not None:
            return await self.get("get", f"/capsules/{capsule_id}")
        elif query is not None:
            return await self.get("post", "/capsules/query", query)
        else:
            return await self.get("get", "/capsules")

    async def request_company(self):
        return await self.get("get", "/company")

    async def request_cores(self, core_id: str = None, query=None):
        self.check_argument([core_id, query])
        if core_id is not None:
            return await self.get("get", f"/cores/{core_id}")
        elif query is not None:
            return await self.get("post", "/cores/query", query)
        else:
            return await self.get("get", "/cores")

    async def request_crew(self, crew_id: str = None, query=None):
        self.check_argument([crew_id, query])
        if crew_id is not None:
            return await self.get("get", f"/crew/{crew_id}")
        elif query is not None:
            return await self.get("post", "/crew/query", query)
        else:
            return await self.get("get", "/crew")

    async def request_dragons(self, dragon_id: str = None, query=None):
        self.check_argument([dragon_id, query])
        if dragon_id is not None:
            return await self.get("get", f"/dragons/{dragon_id}")
        elif query is not None:
            return await self.get("post", "/dragons/query", query)
        else:
            return await self.get("get", "/dragons")

    async def request_landpads(self, landpad_id: str = None, query=None):
        self.check_argument([landpad_id, query])
        if landpad_id is not None:
            return await self.get("get", f"/landpads/{landpad_id}")
        elif query is not None:
            return await self.get("post", "/landpads/query", query)
        else:
            return await self.get("get", "/landpads")

    async def request_launches(
        self, schedule: str = None, launche_id: str = None, query=None
    ):
        self.check_argument([schedule, launche_id, query])
        if schedule is not None:
            schedule_list = ["past", "upcomming", "latest", "next"]
            if schedule in schedule_list:
                return await self.get("get", f"/launches/{schedule}")
            else:
                raise UnexpectedArguments("Invalid endpoint.")
        elif launche_id is not None:
            return await self.get("get", f"/launches/{launche_id}")
        elif query is not None:
            return await self.get("post", "/launches/query", query)
        else:
            return await self.get("get", "/launches")

    async def request_launchpads(self, launchpad_id: str = None, query=None):
        self.check_argument([launchpad_id, query])
        if launchpad_id is not None:
            return await self.get("get", f"/launchpads/{launchpad_id}")
        elif query is not None:
            return await self.get("post", "/launchpads/query", query)
        else:
            return await self.get("get", "/launchpads")

    async def request_payloads(self, payload_id: str = None, query=None):
        self.check_argument([payload_id, query])
        if payload_id is not None:
            return await self.get("get", f"/payloads/{payload_id}")
        elif query is not None:
            return await self.get("post", "/payloads/query", query)
        else:
            return await self.get("get", "/payloads")

    async def request_roadster(self):
        return await self.get("get", "/roadster")

    async def request_rockets(self, rocket_id: str = None, query=None):
        self.check_argument([rocket_id, query])
        if rocket_id is not None:
            return await self.get("get", f"/rockets/{rocket_id}")
        elif query is not None:
            return await self.get("post", "/rockets/query", query)
        else:
            return await self.get("get", "/rockets")

    async def request_ships(self, ship_id: str = None, query=None):
        self.check_argument([ship_id, query])
        if ship_id is not None:
            return await self.get("get", f"/ships/{ship_id}")
        elif query is not None:
            return await self.get("post", "/ships/query", query)
        else:
            return await self.get("get", "/ships")

    async def request_starlink(self, starlink_id: str = None, query=None):
        self.check_argument([starlink_id, query])
        if starlink_id is not None:
            return await self.get("get", f"/starlink/{starlink_id}")
        elif query is not None:
            return await self.get("post", "/starlink/query", query)
        else:
            return await self.get("get", "/starlink")
