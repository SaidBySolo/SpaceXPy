from spacexerror import *
from spacexhttp import Http

http = Http()

class SpaceX():

    async def capsules(self, capsule_id:str= None, query:Any=None):
        if capsule_id is None and query is None:
            return await http.requests('get', '/capsules')
        elif capsule_id is not None:
            return await http.requests('get', f'/capsules/{capsule_id}')
        elif query is not None:
            return await http.requests('post', '/capsules/query', query)
        else:
            raise UnexpectedArguments()