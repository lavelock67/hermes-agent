"""Private SQLite fixture shared by state CRUD and maintenance policy tests."""

import pytest


@pytest.fixture
def db(tmp_path):
    from hermes_state import SessionDB

    session_db = SessionDB(db_path=tmp_path / "test_state.db")
    yield session_db
    session_db.close()
