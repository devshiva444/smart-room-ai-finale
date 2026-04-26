"""Minimal models.py to satisfy OpenEnv environment validation.

This file provides a lightweight load_model() helper that returns the
path to the trained PyTorch artifact. OpenEnv only requires the file
to exist during validation; real loading happens in `core/multi_agent.py`.
"""
from pathlib import Path


def load_model_path():
    """Return the path to the trained model file if present, else None."""
    p = Path(__file__).parent / "smart_room_ai_final.pth"
    return str(p) if p.exists() else None


def model_info():
    """Return basic model metadata for validation/display."""
    path = load_model_path()
    return {
        "name": "DQN-SmartRoom",
        "file": path,
        "status": "present" if path else "missing",
    }
