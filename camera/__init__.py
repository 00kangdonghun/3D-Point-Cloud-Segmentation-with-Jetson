from pathlib import Path

from dataset import Dataset
from .realsense_camera import RealsenseCamera
from .mock_camera import MockRealsenseCamera
from .base_camera import Camera

import pyrealsense2.pyrealsense2 as rs

def auto_connect_camera() -> Camera:
    context = rs.context()

    for device in context.query_devices():
        name = device.get_info(rs.camera_info.name)
        serial = device.get_info(rs.camera_info.serial_number)
        product_line = device.get_info(rs.camera_info.product_line)

        # D455 = D400 product line
        if product_line == "D400":
            print(f"Detected D455 camera: {name} (serial: {serial})")
            return RealsenseCamera(name, serial)

    # No D455 found → fallback to mock
    print("No D455 found. Using mock camera.")
    return MockRealsenseCamera("mock", Dataset(
        Path(__file__).parent / "data" / "mock", only_annotated=False
    ))

__all__ = [
    "Camera",
    "auto_connect_camera"
]
