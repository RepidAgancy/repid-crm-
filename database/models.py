import datetime
import enum
import os

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Enum, String, ForeignKey, INTEGER, Boolean
from sqlalchemy.orm import DeclarativeBase, relationship


class Base(DeclarativeBase):
    pass

class UserType(str, enum.Enum):
    super_admin = 'Super admin'
    admin = 'Admin'
    custom = 'Custom'

class StatusProject(str, enum.Enum):
    in_progres = 'in_progres'
    done = 'done'
    cancel = 'cancel'

class StatusOperator(str, enum.Enum):
    in_progres = 'in_progres'
    done = 'done'
    cancel = 'cancel'

class StatusTask(str, enum.Enum):
    to_do = 'to_do'
    in_progres = 'in_progres'
    done = 'done'
    success = 'success'

class StatusExpectedVAlue(str, enum.Enum):
    income = 'income'
    expense = 'expense'

class ProjectProgrammer(Base):
    __tablename__ = 'project_programmer'

    id: Mapped[int] = mapped_column(primary_key=True)
    project_id:Mapped[int] = mapped_column(ForeignKey('projects.id'))
    programmer_id: Mapped[int] = mapped_column(ForeignKey('employees.id'))


class TaskProgrammer(Base):
    __tablename__ = 'task_programmer'

    id: Mapped[int] = mapped_column(primary_key=True)
    task_id:Mapped[int] = mapped_column(ForeignKey('tasks.id'))
    programmer_id: Mapped[int] = mapped_column(ForeignKey('employees.id'))


class Employees(Base):
    __tablename__ = 'employees'



    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(100))
    username: Mapped[str] = mapped_column(String(100))
    last_name: Mapped[str] = mapped_column(String(100))
    phone_number: Mapped[str] = mapped_column(String(50))
    date_of_birth: Mapped[datetime.datetime | None]
    date_of_jobstarted: Mapped[datetime.datetime | None]
    position_id: Mapped[int] = mapped_column(ForeignKey('positions.id',onupdate='CASCADE'))
    image: Mapped[str | None] = mapped_column(String,index=True)
    salary: Mapped[int | None]
    user_type: Mapped[UserType] = mapped_column(Enum(UserType), default=UserType.custom)
    password: Mapped[str] = mapped_column(String)
    is_active: Mapped[bool] = mapped_column(default=True)

    projects = relationship(
        "Project",
        secondary="project_programmer",
        back_populates="programmers"
    )

    tasks = relationship(
        "Task",
        secondary="task_programmer",
        back_populates="programmers"
    )


    position: Mapped['Position'] = relationship(back_populates='user')

    def __repr__(self) -> str:
        return f"Employees(id={self.id!r}, last_name={self.last_name!r})"


class Position(Base):
    __tablename__ = 'positions'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))

    user: Mapped['Employees'] = relationship(back_populates='position')

    def __repr__(self) -> str:
        return f"Positions(id={self.id!r}, name={self.name!r})"


class Project(Base):
    __tablename__ = 'projects'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    start_date: Mapped[datetime.datetime | None]
    end_date: Mapped[datetime.datetime | None]
    status: Mapped[StatusProject] = mapped_column(Enum(StatusProject), default=StatusProject.in_progres)
    image: Mapped[str] = mapped_column(String,index=True)
    price: Mapped[str] = mapped_column(String, nullable=True)
    is_deleted:Mapped[bool|None] = mapped_column(Boolean, nullable=True ,default=False)

    programmers = relationship(
        "Employees",
        secondary="project_programmer",
        back_populates="projects"
    )


class Operator(Base):
    __tablename__='operators'

    id: Mapped[int] = mapped_column(primary_key=True)
    full_name: Mapped[str] = mapped_column(String(100))
    phone_number: Mapped[str] = mapped_column(String(100))
    description: Mapped[str]
    status:Mapped[StatusOperator] = mapped_column(Enum(StatusOperator), default=StatusOperator.in_progres)
    operator_type_id: Mapped[int] = mapped_column(ForeignKey('operator_type.id', onupdate='CASCADE'))

    operator_type: Mapped['OperatorType'] = relationship(back_populates='operator')


class OperatorType(Base):
    __tablename__='operator_type'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))

    operator: Mapped[Operator] = relationship(back_populates='operator_type')


class ExcpectedValue(Base):
    __tablename__ = 'expected_value'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[int] = mapped_column(String(100))
    date: Mapped[datetime.datetime]
    description: Mapped[str]
    type: Mapped[StatusExpectedVAlue] = mapped_column(Enum(StatusExpectedVAlue))


class Task(Base):
    __tablename__ ='tasks'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[int] = mapped_column(String(100))
    start_date: Mapped[datetime.datetime]
    end_date: Mapped[datetime.datetime]
    status: Mapped[StatusTask] = mapped_column(Enum(StatusTask), default=StatusTask.to_do)
    is_deleted:Mapped[bool|None] = mapped_column(Boolean, nullable=True ,default=False)
    description: Mapped[str]

    programmers = relationship(
        "Employees",
        secondary="task_programmer",
        back_populates="tasks"
    )



