from sqlmodel import SQLModel, Field, create_engine

class Fact(SQLModel, table=True):
    id: int | None = Field(
        default=None,
        primary_key=True,
        description="Numeric Wikidata ID"
    )
    label_en: str = Field(index=True, description="English Wikidata label")
    label_mk: str | None = Field(default=None, description="Macedonian Wikidata label")
    description: str | None = None
    year_start: int | None = Field(default=None, description="Start year")
    year_end: int | None = Field(default=None, description="End year")
    wikidata_url: str | None = None


DATABASE_URL = "postgresql+psycopg://histo:histo@localhost:5432/histofakt"
engine = create_engine(DATABASE_URL, echo=False)