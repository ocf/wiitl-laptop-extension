from typing import List
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, load_only

db_engine = create_engine()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)
db_session = SessionLocal()


class Base(DeclarativeBase):
    pass


class MacMap(Base):
    __tablename__ = "mac_map"
    mac_address = Column(String, nullable=False, primary_key=True)
    device_label = Column(String, nullable=False)
    ocf_username = Column(String, nullable=False)


Base.metadata.create_all(bind=db_engine)


def mac_list_to_users(maclist: List[str]) -> List[str]:
    res: List[MacMap] = (
        db_session.query(MacMap)
        .filter(MacMap.mac_address.in_(tuple(maclist)))
        .options(load_only(MacMap.ocf_username))
        .all()
    )
    return [r.ocf_username for r in res]
