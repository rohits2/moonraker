import sys
import os
import time
from uuid import UUID

# Mock system path to find moonraker
sys.path.append("/home/printer/moonraker")

try:
    from moonraker.components.job_queue import QueuedJob
    print("Imported QueuedJob")
    
    job = QueuedJob("test.gcode", None)
    print(f"Created Job ID: {job.job_id}")
    
    # Verify UUID
    try:
        val = UUID(job.job_id, version=4)
        print("UUID Valid")
    except ValueError:
        print("UUID INVALID")
        sys.exit(1)
        
    if len(job.job_id) != 36:
        print("UUID Length INVALID")
        sys.exit(1)
        
    print("Verification Successful")

except ImportError as e:
    print(f"Import Error: {e}")
    sys.exit(1)
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
