from typing import List
from fastapi import FastAPI, HTTPException, Request, status
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from random import randrange

import config

OAUTH_CLIENT_ID = "macwiitl"
app = FastAPI(title="mac-wiitl", description="MAC Addr based extension of Wiitl")
templates = Jinja2Templates(directory="templates")
lablist: List[str] = []


def verify_push_key(req: Request):
    aktest = req.headers.get("Push-Key")
    if aktest != config.get("PUSH_KEY"):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Invalid push key")


def gen_tab_id():
    return "".join([chr(randrange(65, 91)) for _ in range(0, 11)])


@app.get("/")
async def home(req: Request):
    return templates.TemplateResponse(
        "login.html.j2",
        {
            "request": req,
            "oauth_client_id": OAUTH_CLIENT_ID,
        },
    )


@app.get("/oauth2-callback")
async def oauth2_callback(req: Request):
    return


@app.get("/login")
async def login(req: Request):
    return templates.TemplateResponse(
        "login.html.j2",
        {
            "request": req,
            "oauth_client_id": OAUTH_CLIENT_ID,
            "oauth_tab_id": gen_tab_id(),
        },
    )


@app.get("/wiitl")
async def wiitl():
    return JSONResponse(lablist)


@app.get("/remove/{mac_address}")
async def remove_mac_address(mac_address: str, req: Request):
    return


@app.post("/push")
async def push_mac_addresses(addresses_list: str, req: Request):
    """
    Push MAC addresses from DHCP lease list to this endpoint.
    """
    verify_push_key(req)
    addresses_list.strip().split(" ")
