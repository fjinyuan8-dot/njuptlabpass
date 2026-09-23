"""Typed domain models used by the client and runner."""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


@dataclass(frozen=True)
class Course:
    id: str
    name: str
    finished: bool = False
    type_name: str | None = None


@dataclass(frozen=True)
class Question:
    submission_id: str
    course_id: str
    answer: str | list[str]
    source_question_id: str | None = None
    kind: str | None = None


class CourseStatus(str, Enum):
    SUCCESS = "success"
    FAILED = "failed"


@dataclass(frozen=True)
class CourseResult:
    course: Course
    status: CourseStatus
    question_count: int = 0
    answered_count: int = 0
    error: str | None = None
    uncertain: bool = False

    @property
    def succeeded(self) -> bool:
        return self.status is CourseStatus.SUCCESS


@dataclass(frozen=True)
class RunSummary:
    discovered: int
    already_finished: int
    results: tuple[CourseResult, ...] = field(default_factory=tuple)
    elapsed_seconds: float = 0.0

    @property
    def succeeded(self) -> int:
        return sum(result.succeeded for result in self.results)

    @property
    def failed(self) -> int:
        return len(self.results) - self.succeeded
