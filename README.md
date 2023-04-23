# SpaceXPy

> A wrapper that supports asynchronous.

This package is Asynchronous wrapping of the [informal SpaceX REST API](https://github.com/r-spacex/SpaceX-API).

## Install

```sh
pip install spacexpy
```

## Quick Example

### Sync

```py
import spacexpy

spacex = spacexpy.SpaceX()
cl = spacex.company()

print(cl.headquarters)
print(cl.headquarters.address)

```

### Async

```py
import asyncio
import spacexpy

async def main():
    spacex = spacexpy.SpaceX()
    cl = await spacex.company()
    print(cl.headquarters)
    print(cl.headquarters.address)

asyncio.run(main())
```

Print:

```txt
{"address": "Rocket Road", "city": "Hawthorne", "state": "California"}
Rocket Road
```

## Get all list

### Sync

```py
import spacexpy


spacex = spacexpy.SpaceX()
cl = spacex.capsules()

print(cl)
```

### Async

```py
import asyncio
import spacexpy

async def main():
    spacex = spacexpy.SpaceX()
    cl = await spacex.capsules()
    print(cl)

asyncio.run(main())
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

### 2.0.2

* PR [#10](https://github.com/SaidBySolo/SpaceXPy/pull/10)

### 2.0.1

* PR [#9](https://github.com/SaidBySolo/SpaceXPy/pull/9)

### 2.0.0

* Now support Sync
* Change model
* PR [#3](https://github.com/SaidBySolo/SpaceX-Async-Wrapper/pull/3)

### 1.0.1

* Grammer fix 1.0.1: PR [#1](https://github.com/SaidBySolo/SpaceX-Async-Wrapper/pull/1)

### 1.0.0

* Released 1.0.0: All endpoints cover

## Contributing

You can [Open an issue](https://github.com/SaidBySolo/SpaceX-SimpleWrapper/issues) or submit PRs.
