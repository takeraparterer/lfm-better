#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import time

BASE_URL = "http://localhost:8000"

def print_response(title, response):
    print(f"\n{'='*70}")
    print(f"{title}")
    print('='*70)
    try:
        data = response.json()
        print(json.dumps(data, indent=2))
    except:
        print(response.text)
    return response.status_code

print("\n" + "="*70)
print("LFM RAG API - ENDPOINT TESTS")
print("="*70)

# Test 1: Health check
print("\n[TEST 1] Health Check")
r = requests.get(f"{BASE_URL}/health")
status = print_response("GET /health", r)
print(f"Status Code: {status}")

# Test 2: Query - Pressure Scaling
print("\n[TEST 2] Query - Pressure Scaling Law")
payload = {"question": "What is the pressure scaling law?", "top_k": 2}
r = requests.post(f"{BASE_URL}/query", json=payload)
status = print_response("POST /query (pressure)", r)
print(f"Status Code: {status}")

# Test 3: Query - Arrow of Time
print("\n[TEST 3] Query - Arrow of Time")
payload = {"question": "Explain the arrow of time", "top_k": 2}
r = requests.post(f"{BASE_URL}/query", json=payload)
status = print_response("POST /query (time arrow)", r)
print(f"Status Code: {status}")

# Test 4: Get Specific Axiom
print("\n[TEST 4] Get Axiom A2.1")
r = requests.get(f"{BASE_URL}/axiom/A2.1")
status = print_response("GET /axiom/A2.1", r)
print(f"Status Code: {status}")

# Test 5: List Group II
print("\n[TEST 5] Get Group II Axioms")
r = requests.get(f"{BASE_URL}/group/II")
status = print_response("GET /group/II", r)
print(f"Status Code: {status}")

# Test 6: List All Axioms
print("\n[TEST 6] List All Axioms")
r = requests.get(f"{BASE_URL}/axioms")
status = print_response("GET /axioms", r)
print(f"Status Code: {status}")

# Test 7: Statistics
print("\n[TEST 7] System Statistics")
r = requests.get(f"{BASE_URL}/stats")
status = print_response("GET /stats", r)
print(f"Status Code: {status}")

print("\n" + "="*70)
print("ALL API TESTS COMPLETED")
print("="*70)
print("\nAPI Endpoints:")
print("  - Health: GET /health")
print("  - Query: POST /query")
print("  - Get Axiom: GET /axiom/{axiom_id}")
print("  - Get Group: GET /group/{group}")
print("  - List All: GET /axioms")
print("  - Stats: GET /stats")
print("\nInteractive Docs: http://localhost:8000/docs")
print("ReDoc: http://localhost:8000/redoc")
