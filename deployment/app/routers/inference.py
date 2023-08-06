from fastapi import APIRouter
from models.serializers import CorrectorRequest, CorrectedResult
from routers.utils import inference

router = APIRouter()


@router.post("/correct_sentences")
async def correct_sentences(request: CorrectorRequest):
    corrected = inference(request)

    return corrected
