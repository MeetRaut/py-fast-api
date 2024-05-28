from fastapi import APIRouter

from models.user import User
from config.db import conn
from schemas.user import userEntity, usersEntity
from bson import objectid
user = APIRouter()

@user.get('/')
async def find_all_user():
    return usersEntity(conn.local.user.find())

@user.get('/{id}')
async def find_one_user(id):
    return usersEntity(conn.local.user.find_one({"_id":objectid(id)}))

@user.post('/')
async def create_user(user:User):
    conn.local.user.insert_one(dict(user))

    return usersEntity(conn.local.user.find())

@user.put('/{id}')
async def update_user(id, user:User):
    conn.local.user.find_one_and_update({"_id":objectid(id)}, {
        "$set":dict(user)
    })

    return usersEntity(conn.local.user.find_one({"_id":objectid(id)}))

@user.delete('/{id}')
async def delete_user(user:User):
    return conn.local.user.find_one_and_delete({"_id":objectid(id)})