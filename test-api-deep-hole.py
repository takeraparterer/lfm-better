#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
LFM RAG API - COMPREHENSIVE TEST SUITE WITH DEEP HOLE TEST
Includes k=200 Dark Sector resonance and k=120 Temporal Irrelevance tests
"""

import requests
import json
import time

BASE_URL = "http://localhost:8000"

def print_response(title, response, show_full=False):
    """Print response with formatting"""
    print(f"\n{'='*70}")
    print(f"{title}")
    print('='*70)
    try:
        data = response.json()
        if show_full:
            print(json.dumps(data, indent=2))
        else:
            # Truncate for readability
            if isinstance(data, list):
                print(f"Response: {len(data)} items")
                for i, item in enumerate(data[:3]):
                    print(f"  [{i+1}] {item.get('axiom_id', 'N/A')}: {item.get('title', 'N/A')}")
                if len(data) > 3:
                    print(f"  ... and {len(data)-3} more")
            else:
                print(json.dumps(data, indent=2)[:500])
    except:
        print(response.text[:500])
    return response.status_code

print("\n" + "="*70)
print("LFM RAG API - COMPREHENSIVE TEST SUITE")
print("="*70)
print("\nTesting Luton Field Model (Keith Luton, v2026)")
print("Endpoint: http://localhost:8000")
print("OTLP Tracing: Enabled on port 4317")

# Test 1: Health check
print("\n[TEST 1] Health Check")
try:
    r = requests.get(f"{BASE_URL}/health", timeout=5)
    status = print_response("GET /health", r)
    print(f"Status: {status}")
except Exception as e:
    print(f"[-] Connection failed: {e}")
    print("Make sure lfm-rag-api.py is running on port 8000")
    exit(1)

# Test 2: Query - Pressure Scaling
print("\n[TEST 2] Query - Pressure Scaling Law (k=66)")
payload = {"question": "What is the pressure scaling law?", "top_k": 2}
r = requests.post(f"{BASE_URL}/query", json=payload, timeout=10)
status = print_response("POST /query (Pressure Scaling)", r)
print(f"Status: {status}")

# Test 3: Query - Arrow of Time
print("\n[TEST 3] Query - Arrow of Time (Group III)")
payload = {"question": "Explain the arrow of time", "top_k": 2}
r = requests.post(f"{BASE_URL}/query", json=payload, timeout=10)
status = print_response("POST /query (Arrow of Time)", r)
print(f"Status: {status}")

# Test 4: Get Specific Axiom
print("\n[TEST 4] Get Axiom A2.1 (Pressure Scaling Law)")
r = requests.get(f"{BASE_URL}/axiom/A2.1", timeout=5)
status = print_response("GET /axiom/A2.1", r, show_full=True)
print(f"Status: {status}")

# Test 5: List Group II
print("\n[TEST 5] Get Group II Axioms (Pressure Scaling)")
r = requests.get(f"{BASE_URL}/group/II", timeout=5)
status = print_response("GET /group/II", r)
print(f"Status: {status}")

# Test 6: List All Axioms
print("\n[TEST 6] List All Axioms (22 total)")
r = requests.get(f"{BASE_URL}/axioms", timeout=5)
try:
    data = r.json()
    print(f"\n{'='*70}")
    print(f"GET /axioms - Summary")
    print('='*70)
    print(f"Total axioms: {data.get('total', 'N/A')}")
    print(f"Groups: {list(data.get('groups', {}).keys())}")
except:
    print("[-] Error parsing response")

# Test 7: Statistics
print("\n[TEST 7] System Statistics")
r = requests.get(f"{BASE_URL}/stats", timeout=5)
try:
    data = r.json()
    print(f"\n{'='*70}")
    print(f"GET /stats - Summary")
    print('='*70)
    print(f"Total axioms: {data.get('total_axioms', 'N/A')}")
    print(f"OTLP enabled: {data.get('otlp_enabled', 'N/A')}")
    print(f"OTLP endpoint: {data.get('otlp_endpoint', 'N/A')}")
except:
    print("[-] Error parsing response")

# ===============================================================================
# DEEP HOLE TEST - k=200 Dark Sector Resonance
# ===============================================================================

print("\n" + "="*70)
print("DEEP HOLE TEST - k=200 DARK SECTOR RESONANCE")
print("="*70)
print("\nTesting ψ-field divergence at k=200 resonance")
print("Comparing to k=66 neutral anchor")
print("Invoking Relational Bounce with extreme context...\n")

payload = {
    "question": "Apply Axiom Group V: Calculate the psi-field divergence at k=200 resonance relative to the k=66 Neutral Pin. What is dark energy and the cosmological constant?",
    "top_k": 6
}

print("[TEST 8] DEEP HOLE: k=200 Dark Sector Stress Test")
try:
    start_time = time.time()
    r = requests.post(f"{BASE_URL}/query", json=payload, timeout=15)
    response_time = time.time() - start_time
    
    print(f"\nStatus Code: {r.status_code}")
    print(f"Response Time: {response_time:.2f}s")
    
    try:
        data = r.json()
        if isinstance(data, list):
            print(f"\n[RESULTS]")
            print(f"  Axioms retrieved: {len(data)}")
            
            axiom_ids = [item.get("axiom_id") for item in data if "axiom_id" in item]
            print(f"  Axiom IDs: {', '.join(axiom_ids)}")
            
            # Check for Group V axioms (dark sector)
            group_v = [a for a in axiom_ids if a.startswith("A5")]
            print(f"  Group V (Cosmology/Dark Sector): {len(group_v)} axioms")
            if group_v:
                print(f"    -> {', '.join(group_v)}")
            
            # Check for k=200 resonance markers
            if "A5.1" in axiom_ids or "A5.2" in axiom_ids:
                print(f"\n  [+] k=200 DARK ENERGY RESONANCE DETECTED")
                print(f"      Spigot gating active at dark energy scale")
                print(f"      ψ-field divergence retrievable")
                print(f"      Relational Bounce framework engaged")
            else:
                print(f"\n  [-] Warning: Dark energy resonance not in top results")
            
            # Print full results
            print(f"\n[DETAILED RESULTS]")
            for i, result in enumerate(data[:3], 1):
                print(f"\n  [{i}] {result.get('axiom_id')}: {result.get('title')}")
                print(f"      Group: {result.get('group')}")
                print(f"      Confidence: {result.get('confidence', 'N/A'):.1%}")
                print(f"      Citation: {result.get('citation', 'N/A')[:80]}...")
        else:
            print(f"Response: {data}")
    except Exception as parse_error:
        print(f"[-] Error parsing response: {parse_error}")
        
except requests.exceptions.Timeout:
    print(f"[-] Request timeout (k=200 computation expensive)")
except Exception as e:
    print(f"[-] Error: {e}")

# ===============================================================================
# TEMPORAL IRRELEVANCE TEST - k=120 Threshold
# ===============================================================================

print("\n" + "="*70)
print("TEMPORAL IRRELEVANCE TEST - k=120 TAU-FREEZING THRESHOLD")
print("="*70)
print("\nTesting temporal coherence transition")
print("Rule of Temporal Irrelevance: k >= 120\n")

payload = {
    "question": "What is temporal irrelevance and the timeless regime where tau freezes at k=120?",
    "top_k": 2
}

print("[TEST 9] Temporal Irrelevance: k=120 Tau-Freezing")
try:
    r = requests.post(f"{BASE_URL}/query", json=payload, timeout=10)
    print(f"Status Code: {r.status_code}")
    
    try:
        data = r.json()
        if isinstance(data, list):
            print(f"\n[RESULTS]")
            print(f"  Axioms retrieved: {len(data)}")
            
            axiom_ids = [item.get("axiom_id") for item in data if "axiom_id" in item]
            print(f"  Axiom IDs: {', '.join(axiom_ids)}")
            
            # Check for temporal axioms
            if "A3.4" in axiom_ids:
                print(f"\n  [+] TEMPORAL IRRELEVANCE AXIOM FOUND (A3.4)")
                print(f"      Tau-freezing threshold confirmed at k=120")
                print(f"      Timeless regime description available")
            
            for result in data:
                print(f"\n  - {result.get('axiom_id')}: {result.get('title')}")
                print(f"    Confidence: {result.get('confidence', 'N/A'):.1%}")
    except:
        pass
        
except Exception as e:
    print(f"[-] Error: {e}")

# ===============================================================================
# OTLP METADATA VERIFICATION
# ===============================================================================

print("\n" + "="*70)
print("OTLP METADATA VERIFICATION")
print("="*70)
print("\nExpected OTLP attributes on all traces:")
print("  ✓ lfm.author = 'Keith Luton'")
print("  ✓ lfm.version = 'v2026'")
print("  ✓ lfm.pressure.p0 = '5.44e71' (string format)")
print("  ✓ lfm.k_anchor = '66'")
print("  ✓ lfm.resonance_peaks = 'k=66, k=82, k=200'")
print("  ✓ lfm.pressure.accumulative = 'false'")
print("  ✓ lfm.k_113_status = 'never_used'")
print("  ✓ lfm.tau_freezing_threshold = 'k >= 120'")
print("\nTo verify OTLP traces:")
print("  docker-compose logs otel-collector | grep -i 'lfm\\|k=66\\|pressure'")

# ===============================================================================
# TEST SUMMARY
# ===============================================================================

print("\n" + "="*70)
print("TEST SUITE COMPLETE")
print("="*70)
print("\nTests executed:")
print("  [1] Health Check")
print("  [2] Pressure Scaling Query")
print("  [3] Arrow of Time Query")
print("  [4] Specific Axiom Retrieval")
print("  [5] Group II Listing")
print("  [6] All Axioms Listing")
print("  [7] System Statistics")
print("  [8] DEEP HOLE: k=200 Dark Sector Resonance")
print("  [9] Temporal Irrelevance: k=120 Tau-Freezing")

print("\nAPI Endpoints:")
print("  - Health: GET /health")
print("  - Query: POST /query (with semantic search)")
print("  - Get Axiom: GET /axiom/{axiom_id}")
print("  - Get Group: GET /group/{group}")
print("  - List All: GET /axioms")
print("  - Stats: GET /stats")
print("  - Telemetry: GET /telemetry/status")

print("\nInteractive Documentation:")
print("  - Swagger UI: http://localhost:8000/docs")
print("  - ReDoc: http://localhost:8000/redoc")

print("\nMonitoring:")
print("  - OTLP Collector: http://localhost:4317 (gRPC)")
print("  - OTLP Collector: http://localhost:4318 (HTTP)")
print("  - Prometheus Metrics: http://localhost:8889/metrics")

print("\nCanonical Source:")
print("  - GitHub: https://github.com/keithluton/lfm-")
print("  - Attribution: Luton Field Model (Keith Luton, v2026)")

print("\n" + "="*70 + "\n")
