import time
import json
import random
import hashlib
from datetime import datetime

class IoTSensorArray:
    """Simulates or reads physical IoT nodes deployed around tailings site."""
    def __init__(self, node_id):
        self.node_id = node_id

    def read_telemetry(self):
        # In production, replace with actual serial/LoRaWAN/MQTT sensor reads
        return {
            "node_id": self.node_id,
            "timestamp": datetime.utcnow().isoformat(),
            "pm2_5": round(random.uniform(5.0, 150.0), 2),  150 µg/m³ = high alert
            "pm10": round(random.uniform(10.0, 300.0), 2),
            "wind_speed_kmh": round(random.uniform(0.0, 65.0), 1),
            "ph_level": round(random.uniform(2.5, 8.5), 2),  < 4.0 = Acid Rock Drainage
            "groundwater_ec": round(random.uniform(200, 2500), 1)  # µS/cm
        }

class EcoMiningAIEngine:
    """Core AI Inference engine for environmental safety & dosing control."""
    def __init__(self, pm_threshold=75.0, wind_threshold=35.0):
        self.pm_threshold = pm_threshold
        self.wind_threshold = wind_threshold
        self.suppression_active = False

    def evaluate_risk(self, telemetry):
        """Predictive risk evaluation logic for dust suppression and chemical dosing."""
        pm2_5 = telemetry["pm2_5"]
        wind_speed = telemetry["wind_speed_kmh"]
        ph = telemetry["ph_level"]

        actions = []
        risk_score = 0.0

        # Dust Dispersion Risk Assessment
        if pm2_5 > self.pm_threshold or wind_speed > self.wind_threshold:
            risk_score += 0.6
            actions.append("ACTIVATE_MIST_CANNONS")
            self.suppression_active = True
        else:
            self.suppression_active = False

        # Acid Rock Drainage Risk Assessment
        if ph < 4.0:
            risk_score += 0.4
            actions.append("INCREASE_ALKALINE_NEUTRALIZER_DOSING")

        status = "CRITICAL" if risk_score >= 0.6 else "NOMINAL"

        return {
            "status": status,
            "risk_score": round(risk_score, 2),
            "recommended_actions": actions,
            "suppression_system": "ON" if self.suppression_active else "OFF"
        }

class ProofOfDecontaminationOracle:
    """Generates immutable hashes for Web3 / $ECO9 smart contract state updates."""
    @staticmethod
    def generate_pod_payload(telemetry, evaluation, processed_tonnes):
        payload = {
            "telemetry": telemetry,
            "evaluation": evaluation,
            "processed_tonnes_cumulated": processed_tonnes,
            "nonce": random.randint(100000, 999999)
        }
        serialized = json.dumps(payload, sort_keys=True).encode('utf-8')
        pod_hash = hashlib.sha256(serialized).hexdigest()
        
        return {
            "payload": payload,
            "pod_hash": f"0x{pod_hash}",
            "oracle_status": "READY_FOR_ONCHAIN_SUBMISSION"
        }

# Main Execution Loop (Pilot Test Simulation)
if __name__ == "__main__":
    print("=== EcoMining AI: Open-Source Engine Initialized ===")
    sensor_node = IoTSensorArray(node_id="NODE-MOLDOVA-NOUA-001")
    ai_engine = EcoMiningAIEngine(pm_threshold=75.0, wind_threshold=35.0)
    
    simulated_processed_tonnes = 1250.50

    try:
        for cycle in range(1, 4):
            print(f"\n--- Execution Cycle #{cycle} ---")
            data = sensor_node.read_telemetry()
            analysis = ai_engine.evaluate_risk(data)
            simulated_processed_tonnes += 15.25
            
            oracle_packet = ProofOfDecontaminationOracle.generate_pod_payload(
                data, analysis, round(simulated_processed_tonnes, 2)
            )

            print(f"[IoT Raw Feeds]  PM2.5: {data['pm2_5']} µg/m³ | Wind: {data['wind_speed_kmh']} km/h | pH: {data['ph_level']}")
            print(f"[AI Decision]   Status: {analysis['status']} | Actions: {analysis['recommended_actions']}")
            print(f"[Proof-of-Decontamination Hash] {oracle_packet['pod_hash']}")
            
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nShutdown signal received. Engine stopped safely.")
