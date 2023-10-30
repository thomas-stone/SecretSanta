from fastapi import APIRouter
import boto3

from backend.models.user_model import User
from backend.models.group_model import Group
from backend.schemas.group_schema import GroupCreate, GroupOut, GroupUpdate

group_router = APIRouter()

table = boto3.resource("dynamodb").Table("groups")

@group_router.get("/{group_id}", response_model=GroupOut)
async def get_group(group_id: str):
    response = table.get_item(Key={"group_id": group_id})
    return response["Item"]

@group_router.post("/", response_model=GroupOut)
async def create_group(group: Group):
    group_id = str(group.model_dump()["group_id"])
    group = group.model_dump() | {"group_id": group_id}
    table.put_item(Item=group)
    return group

@group_router.put("/{group_id}", response_model=GroupOut)
async def update_group(group_id: str, group: GroupUpdate):
    group = group.model_dump()

    update_expression = "SET "
    expression_attribute_values = {}

    for key, value in group.items():
        if value is not None and value != "":
            update_expression += f"{key} = :{key}, "
            expression_attribute_values[f":{key}"] = value

    update_expression = update_expression.rstrip(', ')

    table.update_item(
        Key={"group_id": group_id},
        UpdateExpression=update_expression,
        ExpressionAttributeValues=expression_attribute_values
    )

    group["group_id"] = group_id
    return group

@group_router.delete("/{group_id}")
async def delete_group(group_id: str):
    table.delete_item(Key={"group_id": group_id})
    return {"message": "Group successfully deleted"}