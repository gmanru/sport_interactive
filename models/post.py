from . import Base, User
from sqlalchemy import Column, String,Integer,ForeignKey,Text
from sqlalchemy.orm import relationship

class Post(Base):
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    post_title = Column(String(64), nullable=False)
    post_text = Column(Text, nullable=False)

    user = relationship("User", back_populates="post")