#!/bin/bash

echo "Starting RiskMonitor..."

cd "$(dirname "$0")/../app"

nohup python3 main.py > ../logs/application.log 2>&1 &

echo $! > ../riskmonitor.pid

echo "RiskMonitor started with PID $(cat ../riskmonitor.pid)"