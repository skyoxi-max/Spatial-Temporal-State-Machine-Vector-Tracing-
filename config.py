"""
Primary execution script for evaluating the Edge-to-Cloud Co-Design Framework.
"""
import random
from image_processing import CoordinateFilter, calculate_illumination_aware_gain
from state_machine import TrafficStateMachine
from telemetry import compute_telemetry_packet_success


def execute_empirical_run():
    print("=" * 80)
    print("STARTING TRAFFIC ENFORCEMENT EDGE CO-DESIGN FRAMEWORK EXECUTION PROFILE")
    print("=" * 80)

    # Mock evaluation data covering diverse operational deployment scenarios
    scenarios = [
        {"id": "VEH_001", "name": "Bhilai Rural Junction (Low Light)", "lux": 20.0, "snr_db": -1.5,
         "path_x": [150, 250, 350, 500, 650]},
        {"id": "VEH_002", "name": "Suburban Mumbai Interchange (Rainy)", "lux": 85.0, "snr_db": 12.0,
         "path_x": [50, 120, 200, 310, 110]},
        {"id": "VEH_003", "name": "Old Delhi Market Corridor (Daytime)", "lux": 450.0, "snr_db": 25.0,
         "path_x": [110, 260, 380, 520, 710]}
    ]

    for item in scenarios:
        print(f"\n[CORRIDOR RUN] Deployment Arena: {item['name']}")
        print(f"[-] Ambient Illumination: {item['lux']} Lux | Communication SNR: {item['snr_db']} dB")

        # 1. Evaluate Illumination-Aware Preprocessing Layer
        snr_gain = calculate_illumination_aware_gain(item['lux'])
        print(f"[-] Illumination Correction Layer Engaged: +{snr_gain} dB Optical SNR Gain")

        # 2. Track Trajectories and Apply Smoothing Filter
        filter_engine = CoordinateFilter()
        state_machine = TrafficStateMachine(vehicle_id=item['id'])

        print("[-] Mapping target path tracking vectors...")
        for frame_index, raw_coordinate in enumerate(item['path_x']):
            # Add synthetic noise to simulate physical coordinate jitter
            jittered_coord = raw_coordinate + random.uniform(-8.2, 8.2)
            smoothed_x, _ = filter_engine.process_centroid(jittered_coord, 0)

            # Feed smoothed data into the state machine
            state_machine.update_state(smoothed_x)

        # 3. Assess State Machine Violation Determinations
        is_violator, complete_trace = state_machine.get_violation_status()
        print(f"[-] State Machine Trace Trajectory: [{complete_trace}]")

        if is_violator:
            print(" [ALERT Raised] Moving Traffic Violation Confirmed (Wrong-Way Vector detected).")
        else:
            print(" [LOG Saved] Movement identified as a valid maneuver or boundary noise.")

        # 4. Check Telemetry Ingestion Output
        ingestion_success = compute_telemetry_packet_success(item['snr_db'])
        print(f"[-] Packet Ingestion Transmission Success Rate: {ingestion_success}%")
        print("-" * 50)


if __name__ == "__main__":
    execute_empirical_run()