from typing import Dict, Optional

from ..ml.model.content_filter import filter_text

from fastapi import APIRouter, status


router = APIRouter()


@router.post("/app/v1/text/filter", status_code=status.HTTP_200_OK)
async def filter_content(content_to_filter: str) -> Dict[str, Optional[int]]:

    filter_result_num = filter_text(content_to_filter)

    response = {
        0: "Text is safe",
        1: "Text is sensitive",
        2: "Text is unsafe"
        }.get(filter_result_num)

    return {"Result": response}
