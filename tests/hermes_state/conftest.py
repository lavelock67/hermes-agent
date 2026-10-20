"""Private SQLite fixture shared by state CRUD and maintenance policy tests."""

from pathlib import Path

import pytest


@pytest.fixture
def db(tmp_path):
    from hermes_state import SessionDB

    session_db = SessionDB(db_path=tmp_path / "test_state.db")
    yield session_db
    session_db.close()


@pytest.fixture
def private_db_no_foreign_holders(tmp_path, monkeypatch):
    """Explicit premise for private-DB policy tests, never real foreign-holder tests.

    In-process holders remain real. Scanning unrelated host processes would add
    an uncontrolled input and can hit the suite's real-home I/O tripwire.
    """
    import hermes_state_holders

    def scan_owned_db(path):
        assert Path(path).resolve().parent == tmp_path.resolve()
        return []

    monkeypatch.setattr(hermes_state_holders, "foreign_state_db_holders", scan_owned_db)
