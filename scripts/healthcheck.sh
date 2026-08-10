#!/bin/bash

echo "Checking RiskMonitor..."

# 1. Check process
if pgrep -f "python3 main.py" > /dev/null; then
    echo "[OK] Process is running"
else
    echo "[ERROR] Process is not running"
    exit 1
fi

# 2. Check port
if ss -ltn | grep -q ":8080"; then
    echo "[OK] Port 8080 is listening"
else
    echo "[ERROR] Port 8080 is not listening"
    exit 1
fi

# 3. Check HTTP endpoint
if curl -s -f http://localhost:8080/health > /dev/null; then
    echo "[OK] HTTP healthcheck passed"
else
    echo "[ERROR] HTTP healthcheck failed"
    exit 1
fi

echo "RiskMonitor is healthy"
exit 0