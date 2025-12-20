
from datetime import datetime

from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, JSON, String, Text

from app.db.base import Base


class Component(Base):
    __tablename__ = "components"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False, unique=True)
    formula = Column(String(64), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)


class PropertyCorrelation(Base):
    __tablename__ = "property_correlations"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    data = Column(JSON, nullable=False, default=dict)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)


class SteamTable(Base):
    __tablename__ = "steam_tables"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    data = Column(JSON, nullable=False, default=dict)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)


class EquipmentTemplate(Base):
    __tablename__ = "equipment_templates"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    data = Column(JSON, nullable=False, default=dict)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)


class Flowsheet(Base):
    __tablename__ = "flowsheets"

    id = Column(String(64), primary_key=True)
    name = Column(String(256), nullable=True)
    data = Column(JSON, nullable=False, default=dict)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)


class Stream(Base):
    __tablename__ = "streams"

    id = Column(String(64), primary_key=True)
    flowsheet_id = Column(String(64), ForeignKey("flowsheets.id"), nullable=False)
    data = Column(JSON, nullable=False, default=dict)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)


class Unit(Base):
    __tablename__ = "units"

    id = Column(String(64), primary_key=True)
    flowsheet_id = Column(String(64), ForeignKey("flowsheets.id"), nullable=False)
    type = Column(String(32), nullable=False)
    params = Column(JSON, nullable=False, default=dict)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)


class Calculation(Base):
    __tablename__ = "calculations"

    id = Column(Integer, primary_key=True)
    flowsheet_id = Column(String(64), ForeignKey("flowsheets.id"), nullable=False)
    status = Column(String(32), nullable=False, default="created")
    data = Column(JSON, nullable=False, default=dict)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)


class Result(Base):
    __tablename__ = "results"

    id = Column(Integer, primary_key=True)
    flowsheet_id = Column(String(64), ForeignKey("flowsheets.id"), nullable=False)
    data = Column(JSON, nullable=False, default=dict)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)


class ValidationLog(Base):
    __tablename__ = "validation_logs"

    id = Column(Integer, primary_key=True)
    flowsheet_id = Column(String(64), ForeignKey("flowsheets.id"), nullable=False)
    level = Column(String(16), nullable=False)
    code = Column(String(64), nullable=False)
    message = Column(Text, nullable=False)
    suggestion = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
