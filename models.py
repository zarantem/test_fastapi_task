from pydantic import BaseModel, Field
from datetime import date, datetime

class shift_task(BaseModel):
    close_status: bool = Field(alias='СтатусЗакрытия')
    shift_task_submission: str = Field(alias='ПредставлениеЗаданияНаСмену')
    work_center: str = Field(alias='Рабочий центр')
    shift: str = Field(alias='Смена')
    brigade: str = Field(alias='Бригада')
    partion_naumber: int = Field(alias='НомерПартии')
    partion_date: date = Field(alias='ДатаПартии')
    nomenclature: str = Field(alias='Номенклатура')
    ekn_code: str = Field(alias='КодЕКН')
    rc_id: str = Field(alias='ИдентификаторРЦ')
    shift_starts_at: datetime = Field(alias='ДатаВремяНачалаСмены')
    shift_ends_at: datetime = Field(alias='ДатаВремяОкончанияСмены')
    closed_at: datetime = Field(alias='время закрытия')


class product(BaseModel):
    unique_product_code: str = Field(alias='УникальныйКодПродукта')
    partion_naumber: int = Field(alias='НомерПартии')
    partion_date: date = Field(alias='ДатаПартии')