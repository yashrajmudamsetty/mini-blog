from pydantic import BaseModel, ConfigDict, Field
# config dict is the modern pydantic version to configure models, basemodel is the base class from which pydantic models inherit from

class PostBase(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    content: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=50)

class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    model_config = ConfigDict(from_attributes=True)
    # it tells pydantic to read data from objects not just dictionaries

    id: int
    date_posted: str