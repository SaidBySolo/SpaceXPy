from .spacexerror import *
from .spacexhttp import Http

http = Http()


class SpaceXClient:
    async def capsules(self, capsule_id: str = None, query=None):
        if len(list(filter(None.__ne__, [capsule_id, query]))) >= 2:
            raise UnexpectedArguments(
                "Only one argument is required but received more than one")
        elif capsule_id is not None:
            return await http.get("get", f"/capsules/{capsule_id}")
        elif query is not None:
            return await http.get("post", "/capsules/query", query)
        else:
            return await http.get("get", "/capsules")

    async def company(self):
        return await http.get("get", "/company")

    async def cores(self, core_id: str = None, query=None):
        if len(list(filter(None.__ne__, [core_id, query]))) >= 2:
            raise UnexpectedArguments(
                "Only one argument is required but received more than one")
        elif core_id is not None:
            return await http.get('get', f'/cores/{core_id}')
        elif query is not None:
            return await http.get('post', '/cores/query', query)
        else:
            return await http.get('get', '/cores')

    async def crew(self, crew_id: str = None, query=None):
        if len(list(filter(None.__ne__, [crew_id, query]))) >= 2:
            raise UnexpectedArguments(
                "Only one argument is required but received more than one")
        elif crew_id is not None:
            return await http.get('get', f'/crew/{crew_id}')
        elif query is not None:
            return await http.get('post', '/crew/query', query)
        else:
            return await http.get('get', '/crew')

    async def dragons(self, dragon_id: str = None, query=None):
        if len(list(filter(None.__ne__, [dragon_id, query]))) >= 2:
            raise UnexpectedArguments(
                "Only one argument is required but received more than one")
        elif dragon_id is not None:
            return await http.get('get', f'/dragons/{dragon_id}')
        elif query is not None:
            return await http.get('post', '/dragons/query', query)
        else:
            return await http.get('get', '/dragons')

    async def landpads(self, landpad_id: str = None, query=None):
        if len(list(filter(None.__ne__, [landpad_id, query]))) >= 2:
            raise UnexpectedArguments(
                "Only one argument is required but received more than one")
        elif landpad_id is not None:
            return await http.get('get', f'/landpads/{landpad_id}')
        elif query is not None:
            return await http.get('post', '/landpads/query', query)
        else:
            return await http.get('get', '/landpads')

    async def launches(self,
                       schedule: str = None,
                       launche_id: str = None,
                       query=None):
        if len(list(filter(None.__ne__, [schedule, launche_id, query]))) >= 2:
            raise UnexpectedArguments(
                "Only one argument is required but received more than one")
        elif schedule is not None:
            schedule_list = ["past", "upcomming", "latest", "next"]
            if schedule in schedule_list:
                return await http.get('get', f'/launches/{schedule}')
            else:
                raise UnexpectedArguments("invalid endpoint.")
        elif launche_id is not None:
            return await http.get('get', f'/launches/{launche_id}')
        elif query is not None:
            return await http.get('post', '/launches/query', query)
        else:
            return await http.get('get', '/launches')

    async def launchpads(self, launchpad_id: str = None, query=None):
        if len(list(filter(None.__ne__, [launchpad_id, query]))) >= 2:
            raise UnexpectedArguments("Two or more arguments cannot come.")
        elif launchpad_id is not None:
            return await http.get('get', f'/launchpads/{launchpad_id}')
        elif query is not None:
            return await http.get('post', '/launchpads/query', query)
        else:
            return await http.get('get', '/launchpads')

    async def payloads(self, payload_id: str = None, query=None):
        if len(list(filter(None.__ne__, [payload_id, query]))) >= 2:
            raise UnexpectedArguments("Two or more arguments cannot come.")
        elif payload_id is not None:
            return await http.get('get', f'/payloads/{payload_id}')
        elif query is not None:
            return await http.get('post', '/payloads/query', query)
        else:
            return await http.get('get', '/payloads')

    async def roadster(self):
        return await http.get('get', '/roadster')

    async def rockets(self, rocket_id: str = None, query=None):
        if len(list(filter(None.__ne__, [rocket_id, query]))) >= 2:
            raise UnexpectedArguments("Two or more arguments cannot come.")
        elif rocket_id is not None:
            return await http.get('get', f'/rockets/{rocket_id}')
        elif query is not None:
            return await http.get('post', '/rockets/query', query)
        else:
            return await http.get('get', '/rockets')

    async def ships(self, ship_id: str = None, query=None):
        if len(list(filter(None.__ne__, [ship_id, query]))) >= 2:
            raise UnexpectedArguments("Two or more arguments cannot come.")
        elif ship_id is not None:
            return await http.get('get', f'/ships/{ship_id}')
        elif query is not None:
            return await http.get('post', '/ships/query', query)
        else:
            return await http.get('get', '/ships')

    async def starlink(self, starlink_id: str = None, query=None):
        if len(list(filter(None.__ne__, [starlink_id, query]))) >= 2:
            raise UnexpectedArguments("Two or more arguments cannot come.")
        elif starlink_id is not None:
            return await http.get('get', f'/starlink/{starlink_id}')
        elif query is not None:
            return await http.get('post', '/starlink/query', query)
        else:
            return await http.get('get', '/starlink')
