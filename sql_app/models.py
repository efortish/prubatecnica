


from sqlalchemy import  Column, ForeignKey, Integer, String, Date



from .database import Base



class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    phone_number = Column(String)
    password = Column(String)
    profile = Column(String)
    medical_services = Column(String)
    date_of_birth = Column(String)












