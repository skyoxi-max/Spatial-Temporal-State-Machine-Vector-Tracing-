"""
Network modeling pipeline evaluating ingestion rates under varying channel conditions.
"""
import numpy as np
from config import CRITICAL_SNR_THRESHOLD_DB

def compute_telemetry_packet_success(channel_snr_db):
    """
    Models data link performance, automatically engaging the ESP-NOW fallback
    when the signal drops into the critical failure domain.
    """
    if channel_snr_db <= CRITICAL_SNR_THRESHOLD_DB:
        # Physical Fallback Layer maintains an ~81% to 85% success rate
        # by avoiding TCP/IP overhead and transmitting via direct MAC addressing.
        base_success_rate = np.random.uniform(81.0, 85.5)
    else:
        # Standard sigmoidal optimization curve for stable networks
        logistic_curve = 40 + (60 / (1 + np.exp(-0.4 * (channel_snr_db - 1.0))))
        base_success_rate = np.clip(logistic_curve, 85.0, 99.8)

    return round(base_success_rate, 2)