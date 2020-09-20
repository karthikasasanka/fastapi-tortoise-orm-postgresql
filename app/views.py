from fastapi.exceptions import HTTPException
from typing import List

from fastapi import APIRouter

from app.crud import add, filter_by, get, get_all, update
from app.schemas import Note

note_views = APIRouter()

@note_views.get("", response_model=List[Note])
async def get_notes():
    return await get_all()


@note_views.post("", response_model=Note)
async def new_note(note_in: Note):
    return await add(data= note_in.data, title=note_in.title)

@note_views.get("/{text}", response_model=List[Note])
async def filter_notes_by_text(text: str):
    return await filter_by(text=text)

@note_views.put("/{id}", response_model=Note)
async def update_note(id: int, note_in: Note):
    note_to_update = await get(id=id)

    if not note_to_update:
        raise HTTPException(400,detail="Invalid Note")

    # return await update(note_id=id, note_data=note_in.dict(exclude_unset=True))
    return await update(note_to_update=note_to_update, note_data=note_in.dict(exclude_unset=True))
