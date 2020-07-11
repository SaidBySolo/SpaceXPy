from .spacexerror import *
from .spacexhttp import Http

http = Http()

class SpaceXClient():

    async def capsules(self, capsule_id:str= None, query=None):
        if len(list(filter(None.__ne__, [capsule_id, query]))) >= 2:
            raise UnexpectedArguments('Only one argument is required but received more than one')     
        elif capsule_id is not None:
            return await http.capsules('get', f'/capsules/{capsule_id}')
        elif query is not None:
            return await http.capsules('post', '/capsules/query', query)
        else:
            return await http.capsules('get', '/capsules')
    
    async def company(self):
        return await http.company('get', '/company')

    async def cores(self, core_id:str= None, query=None):
        if len(list(filter(None.__ne__, [core_id, query]))) >= 2:
            raise UnexpectedArguments('Only one argument is required but received more than one')
        elif core_id is not None:
            return await http.cores('get', f'/cores/{core_id}')
        elif query is not None:
            return await http.cores('post', '/cores/query', query)
        else:
            return await http.cores('get', '/cores')
    
    async def crew(self, crew_id:str=None, query=None):
        if len(list(filter(None.__ne__, [crew_id, query]))) >= 2:
            raise UnexpectedArguments('Only one argument is required but received more than one')
        elif crew_id is not None:
            return await http.crew('get', f'/crew/{crew_id}')
        elif query is not None:
            return await http.crew('post', '/crew/query', query)
        else:
            return await http.crew('get', '/crew')

    async def dragons(self, dragon_id:str= None, query=None):
        if len(list(filter(None.__ne__, [dragon_id, query]))) >= 2:
            raise UnexpectedArguments('Only one argument is required but received more than one')
        elif dragon_id is not None:
            return await http.dragons('get', f'/dragons/{dragon_id}')
        elif query is not None:
            return await http.dragons('post', '/dragons/query', query)
        else:
            return await http.dragons('get', '/dragons')

    async def landpads(self, landpad_id:str= None, query=None):
        if len(list(filter(None.__ne__, [landpad_id, query]))) >= 2:
            raise UnexpectedArguments('Only one argument is required but received more than one')
        elif landpad_id is not None:
            return await http.landpads('get', f'/landpads/{landpad_id}')
        elif query is not None:
            return await http.landpads('post', '/landpads/query', query)
        else:
            return await http.landpads('get', '/landpads')

    async def launches(self, schedule:str = None, launche_id:str= None, query=None):
        if len(list(filter(None.__ne__, [schedule, launche_id, query]))) >= 2:
            raise UnexpectedArguments('Only one argument is required but received more than one')
        elif schedule is not None:
            schedule_list = ['past', 'upcomming', 'latest', 'next']
            if schedule in schedule_list:
                return await http.launches('get', f'/launches/{schedule}')
            else:
                raise UnexpectedArguments('invalid endpoint.')
        elif launche_id is not None:
            return await http.launches('get', f'/launches/{launche_id}')
        elif query is not None:
            return await http.launches('post', '/launches/query', query)
        else:
            return await http.launches('get', '/launches')

    async def launchpads(self, launchpad_id:str= None, query=None):
        if len(list(filter(None.__ne__, [launchpad_id, query]))) >= 2:
            raise UnexpectedArguments('Two or more arguments cannot come.')
        elif launchpad_id is not None:
            return await http.launchpads('get', f'/launchpads/{launchpad_id}')
        elif query is not None:
            return await http.launchpads('post', '/launchpads/query', query)
        else:
            return await http.launchpads('get', '/launchpads')

    async def payloads(self, payload_id:str= None, query=None):
        if len(list(filter(None.__ne__, [payload_id, query]))) >= 2:
            raise UnexpectedArguments('Two or more arguments cannot come.')
        elif payload_id is not None:
            return await http.payloads('get', f'/payloads/{payload_id}')
        elif query is not None:
            return await http.payloads('post', '/payloads/query', query)
        else:
            return await http.payloads('get', '/payloads')

    async def roadster(self):
        return await http.roadster('get', '/roadster')

    async def rockets(self, rocket_id:str= None, query=None):
        if len(list(filter(None.__ne__, [rocket_id, query]))) >= 2:
            raise UnexpectedArguments('Two or more arguments cannot come.')
        elif rocket_id is not None:
            return await http.rockets('get', f'/rockets/{rocket_id}')
        elif query is not None:
            return await http.rockets('post', '/rockets/query', query)
        else:
            return await http.rockets('get', '/rockets')

    async def ships(self, ship_id:str= None, query=None):
        if len(list(filter(None.__ne__, [ship_id, query]))) >= 2:
            raise UnexpectedArguments('Two or more arguments cannot come.')
        elif ship_id is not None:
            return await http.ships('get', f'/ships/{ship_id}')
        elif query is not None:
            return await http.ships('post', '/ships/query', query)
        else:
            return await http.ships('get', '/ships')

    async def starlink(self, starlink_id:str= None, query=None):
        if len(list(filter(None.__ne__, [starlink_id, query]))) >= 2:
            raise UnexpectedArguments('Two or more arguments cannot come.')
        elif starlink_id is not None:
            return await http.starlink('get', f'/starlink/{starlink_id}')
        elif query is not None:
            return await http.starlink('post', '/starlink/query', query)
        else:
            return await http.starlink('get', '/starlink')
