# create a group model that will be used to create a group table in the database
# the group table will be used to store the group information like group name, group members, etc
# the group model will be used to create a group table in the database

from pydantic import BaseModel, Field
from typing import Optional, List
from uuid import uuid4

class Group(BaseModel):
    group_id: str = Field(default_factory=uuid4)
    group_name: str
    group_description: str
    group_members: List[str] | None = None
    group_admin: str
    random_ordered_list: List[str] | None = None