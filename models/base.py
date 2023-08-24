from sqlalchemy.ext.declarative import declarative_base

# Create a base class for your models
Base = declarative_base()

# You can also add any common functionality or attributes here that you want to be present in all models.
# For example, you can define common columns like 'created_at' and 'updated_at'.
# Keep in mind that this is just a sample and you can modify it according to your requirements.
# Example:
# from sqlalchemy import Column, DateTime
# from sqlalchemy.sql import func
#
# class Base(Base):
#     __abstract__ = True
#     created_at = Column(DateTime, default=func.now())
#     updated_at = Column(DateTime, onupdate=func.now())
