import re
from typing import List
from app.note.models import Note


async def add(data: str, title: str=None) -> Note:
    new_note = await Note.create(data=data, title=title)
    return new_note


async def get(id: int) -> Note:
    note = await Note.get_or_none(id=id)
    return note


async def get_all() -> List[Note]:
    notes = await Note.all()
    return notes


async def filter_by(text: str) -> List[Note]:
    notes = await Note.filter(data__icontains=text)
    return notes


async def update(note_to_update: Note, note_data: dict):
    for field_name in note_data:
        setattr(note_to_update, field_name, note_data.get(field_name))
    await note_to_update.save()
    return note_to_update
