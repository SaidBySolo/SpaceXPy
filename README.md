# SpaceX-Async-Wrapper

> A wrapper that supports asynchronous.

This package is Asynchronous wrapping of the [informal SpaceX REST API](https://github.com/r-spacex/SpaceX-API).

## Install

```sh
pip install spacexpy
```

## Quick Example

```py
import asyncio
import spacexpy

async def main():
    spacex = spacexpy.SpaceX()
    cl = await spacex.company()
    print(cl.name)
    print(cl.summary)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```
Print:
```
SpaceX
SpaceX designs, manufactures and launches advanced rockets and spacecraft. The company was founded in 2002 to revolutionize space technology, with the ultimate goal of enabling people to live on other planets.
```

## Get all list
```py
import asyncio
import spacexpy

async def main():
    spacex = spacexpy.SpaceX()
    cl = await spacex.capsules(rawdata=True)
    print(cl.data)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```
Print:
```json
[
    {
        "reuse_count": 1,
        "water_landings": 1,
        "land_landings": 0,
        "last_update": "Reentered after three weeks in orbit",
        "launches": [
            "5eb87cdeffd86e000604b330"
        ],
        "serial": "C101",
        "status": "retired",
        "id": "5e9e2c5bf35918ed873b2664"
    },
    ...
]
```
## Attribute

Check this [docs](https://github.com/r-spacex/SpaceX-API/blob/master/docs/v4/README.md)

## Patch note

### 1.0.0

* Released 1.0.0: All endpoints cover


## Contributing

You can [Open an issue](https://github.com/SaidBySolo/SpaceX-SimpleWrapper/issues) or submit PRs.
