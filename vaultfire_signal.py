from datetime import datetime
import os

def log_vaultfire_status():
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    status = "Vaultfire status: ACTIVE | Identity: Ghostkey-316 | Wallet: bpow20.cb.id"
    log_entry = f"[{timestamp}] {status}\n"

    os.makedirs("logs", exist_ok=True)

    with open("logs/vaultfire_log.txt", "a") as log_file:
        log_file.write(log_entry)

    print(log_entry.strip())

if __name__ == "__main__":
    log_vaultfire_status()
