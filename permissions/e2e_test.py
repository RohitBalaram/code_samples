import pytest
from models.Users import User


@pytest.fixture
def professor():
    return User("professor", "Master Yoda")


@pytest.fixture
def teachers_assistant():
    return User("teachers_assistant", "Obi-Wan Kenobi")


@pytest.fixture
def student():
    return User("student", "Luke Skywalker")


@pytest.fixture
def exam():
    return {"name": "history exam 1", "score": 0}


@pytest.fixture
def test():
    return {"name": "history test 1", "score": 0}


@pytest.fixture
def grade():
    return {"name": "Mathematics", "grade": 0}
 

@pytest.fixture
def attendance():
    return {"name": "Home Room", "mark": 0}


def test_professor_add_and_get_test(professor, exam):
    history_exam_id = professor.exams.add(exam)
    retrieved_exam = professor.exams.get(history_exam_id)
    assert retrieved_exam == exam


def test_professor_update_exam(professor, exam):
    history_exam_id = professor.exams.add(exam)
    retrieved_exam = professor.exams.get(history_exam_id)
    assert retrieved_exam["score"] == 0

    professor.exams.update(history_exam_id, "score", 100)
    new_retrieved_exam = professor.exams.get(history_exam_id)
    assert new_retrieved_exam["score"] == 100
    

def test_student_cant_add_test(student, exam):
    with pytest.raises(AttributeError):
        student.exams.add(exam)
    

def test_teachers_assistant_cant_add_test(teachers_assistant, exam):
    with pytest.raises(AttributeError):
        teachers_assistant.exams.add(exam)


def _assert_user_cant_update_tests_exams_or_attendance(
        professor, user, exam, test, attendance):
    exam_id = professor.exams.add(exam)
    test_id = professor.tests.add(test)
    attendance_id = professor.attendance.add(attendance)

    with pytest.raises(AttributeError):
        user.exams.update(exam_id, "score", 60)

    with pytest.raises(AttributeError):
        user.tests.update(test_id, "score", 60)

    with pytest.raises(AttributeError):
        user.attendance.update(attendance_id, "mark", "present")


def test_teachers_assistant_cant_update_tests_exams_or_attendance(
        professor, teachers_assistant, exam, test, attendance):

    _assert_user_cant_update_tests_exams_or_attendance(
        professor, teachers_assistant, exam, test, attendance)


def test_students_cant_update_tests_exams_or_attendance(
        professor, student, exam, test, attendance):

    _assert_user_cant_update_tests_exams_or_attendance(
        professor, student, exam, test, attendance)


def _assert_user_can_read_object_other_user_created(
        professor, user, exam, test, attendance):

    exam_id = professor.exams.add(exam)
    test_id = professor.tests.add(test)
    attendance_id = professor.attendance.add(attendance)

    retrieved_exam = user.exams.get(exam_id)
    assert exam == retrieved_exam

    retrieved_test = user.tests.get(exam_id)
    assert test == retrieved_test

    retrieved_attendance = user.attendance.get(attendance_id)
    assert attendance == retrieved_attendance


def test_student_can_read_object_other_user_created(
        professor, student, exam, test, attendance):

    _assert_user_can_read_object_other_user_created(
        professor, student, exam, test, attendance)


def test_teachers_assistant_can_read_object_other_user_created(
        professor, teachers_assistant, exam, test, attendance):

    _assert_user_can_read_object_other_user_created(
        professor, teachers_assistant, exam, test, attendance)
