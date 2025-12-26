import pytest
from unittest.mock import MagicMock
from uuid import UUID
from moonraker.components.job_queue import QueuedJob
from moonraker.components.history import History, PrinterJob

def test_queued_job_uuid():
    job = QueuedJob("test.gcode", None)
    # Verify job_id is a valid UUID
    try:
        val = UUID(job.job_id, version=4)
        assert str(val).upper() == job.job_id.upper()
    except ValueError:
        pytest.fail(f"job_id {job.job_id} is not a valid UUID")

@pytest.mark.asyncio
async def test_history_job_creation():
    # Mock config and server
    config = MagicMock()
    server = MagicMock()
    config.get_server.return_value = server
    server.lookup_component.return_value = MagicMock() # file_manager
    
    # We can't easily instantiate History full component without full server mock,
    # but we can test PrinterJob and static methods if any.
    
    # Test PrinterJob create_time
    job = PrinterJob({})
    assert hasattr(job, 'create_time')
    assert job.create_time > 0

    # Test QueuedJob again just to be sure
    qjob = QueuedJob("test.gcode")
    assert len(qjob.job_id) == 36
