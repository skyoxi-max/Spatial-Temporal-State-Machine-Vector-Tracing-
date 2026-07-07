"""
Configuration module defining system-wide constants, geometric regions of interest,
and physical hardware performance simulation limits.
"""

# Optical Optimization and Threshold Limits
LOW_LIGHT_THRESHOLD_LUX = 20.0
TARGET_SNR_GAIN_DB = 16.0

# Spatial Coordinate Trajectory Boundaries (Enforcement Fields)
# Coordinates represented as bounding polygons or regional lines
ROI_1_ENTRY_X_BOUNDS = (100, 400)    # Active Monitoring Entry Zone (S1)
ROI_2_VIOLATION_X_BOUNDS = (450, 800)  # Active Moving Violation Checked Field (S2)

# Vector Smoothing Window Length
SMOOTHING_WINDOW_SIZE = 5

# Wireless Network Performance Profiles
CRITICAL_SNR_THRESHOLD_DB = 2.0
MIN_RELIABILITY_TARGET_PCT = 90.0