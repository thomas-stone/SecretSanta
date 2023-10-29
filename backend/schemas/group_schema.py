from pydantic import BaseModel, Field

class GroupCreate(BaseModel):
    group_name: str
    group_description: str
    group_members: list[str] | None = None
    group_admin: str

class GroupUpdate(BaseModel):
    group_name: str | None
    group_description: str | None
    group_members: list[str] | None
    group_admin: str | None
    random_ordered_list: list[str] | None

class GroupOut(BaseModel):
    group_id: str
    group_name: str
    group_description: str
    group_members: list[str] | None = None
    group_admin: str
    random_ordered_list: list[str] | None = None