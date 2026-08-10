#!/bin/bash

PID_FILE="riskmonitor.pid"

if [ -f "$PID_FILE" ]; then

    PID=$(cat "$PID_FILE")

    echo "Stopping RiskMonitor (PID: $PID)..."

    kill "$PID"

    rm "$PID_FILE"

    echo "RiskMonitor stopped."

else

    echo "RiskMonitor is not running."

fi