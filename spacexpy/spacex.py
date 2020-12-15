import asyncio
import functools
from typing import Any
from .spacexrequester import SpaceXRequester
from .spacexmodel import AttributeDict


class _SpaceX(SpaceXRequester):
    async def capsules(self, capsule_id: str = None, query=None):
        return AttributeDict(
            await self.request_capsules(capsule_id, query),
        )

    async def company(self):
        return AttributeDict(await self.request_company())

    async def cores(self, core_id: str = None, query=None):
        return AttributeDict(await self.request_cores(core_id, query))

    async def crew(self, crew_id: str = None, query=None):
        return AttributeDict(await self.request_crew(crew_id, query))

    async def dragons(self, dragon_id: str = None, query=None):
        return AttributeDict(await self.request_dragons(dragon_id, query))

    async def landpads(self, landpad_id: str = None, query=None):
        return AttributeDict(await self.request_landpads(landpad_id, query))

    async def launches(self, schedule: str = None, launche_id: str = None, query=None):
        return AttributeDict(await self.request_launches(schedule, launche_id, query))

    async def launchpads(self, launchpad_id: str = None, query=None):
        return AttributeDict(await self.request_launchpads(launchpad_id, query))

    async def payloads(self, payload_id: str = None, query=None):
        return AttributeDict(await self.request_payloads(payload_id, query))

    async def roadster(self):
        return AttributeDict(await self.request_roadster())

    async def rockets(self, rocket_id: str = None, query=None):
        return AttributeDict(await self.request_rockets(rocket_id, query))

    async def ships(self, ship_id: str = None, query=None):
        return AttributeDict(await self.request_ships(ship_id, query))

    async def starlink(self, starlink_id: str = None, query=None):
        return AttributeDict(await self.request_ships(starlink_id, query))


class SpaceX(_SpaceX):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.loop = asyncio.get_event_loop()

    def __run_coroutine(self, coroutine, *args, **kwargs):
        if self.loop.is_running():
            return coroutine(*args, **kwargs)

        return self.loop.run_until_complete(coroutine(*args, **kwargs))

    def __getattribute__(self, name: str) -> Any:
        attribute = getattr(super(), name, None)

        if not attribute:
            return object.__getattribute__(self, name)

        if asyncio.iscoroutinefunction(attribute):
            return functools.partial(self.__run_coroutine, attribute)

        return attribute
