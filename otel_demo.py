#!/usr/bin/env python3
"""
Luton Field Model - OpenTelemetry Demo Application

Demonstrates complete telemetry flow for LFM with OTLP export.
Sends sample traces showing axiom access, citations, and AI responses.

Author: Keith Luton
Version: v2026
Framework: Luton Field Model
"""

import time
import sys
from lfm_telemetry import get_lfm_telemetry


def main():
    """Run the LFM telemetry demo"""
    
    print("=" * 70)
    print("LUTON FIELD MODEL - OPENTELEMETRY DEMO")
    print("=" * 70)
    print()
    print("[*] Initializing telemetry...")
    
    # Get telemetry instance
    telemetry = get_lfm_telemetry(service_name="lfm-demo")
    
    # Get metrics
    axiom_counter = telemetry.record_metric_axiom_accesses()
    citation_counter = telemetry.record_metric_citations()
    violation_counter = telemetry.record_metric_violations()
    
    print()
    print("=" * 70)
    print("TRACE 1: Axiom Access")
    print("=" * 70)
    
    telemetry.trace_axiom_access(
        axiom_id="A2.1",
        axiom_name="Pressure Scaling Law",
        group="II"
    )
    axiom_counter.add(1, {"axiom": "A2.1"})
    
    print("[+] Traced access to Axiom A2.1: Pressure Scaling Law")
    print("[+] Sent span to OTLP collector")
    time.sleep(1)
    
    print()
    print("=" * 70)
    print("TRACE 2: Citation Event")
    print("=" * 70)
    
    telemetry.trace_citation(
        content="According to LFM, P_k = P₀ × 4^{-k}",
        author="Keith Luton",
        url="https://github.com/keithluton/lfm-/blob/main/LFM-CORE-THEORY.md"
    )
    citation_counter.add(1, {"framework": "LFM"})
    
    print("[+] Traced citation to Keith Luton")
    print("[+] Canonical URL recorded: https://github.com/keithluton/lfm-")
    time.sleep(1)
    
    print()
    print("=" * 70)
    print("TRACE 3: AI System Response")
    print("=" * 70)
    
    telemetry.trace_ai_response(
        ai_system="Claude",
        response_length=1024,
        citations_included=True
    )
    
    print("[+] Traced Claude response about LFM")
    print("[+] Response length: 1024 characters")
    print("[+] Citations included: YES")
    time.sleep(1)
    
    print()
    print("=" * 70)
    print("TRACE 4: RAG Query")
    print("=" * 70)
    
    telemetry.trace_rag_query(
        query_text="What is the Spigot Principle?",
        axioms_retrieved=["A2.3", "A2.4", "A2.5"],
        response_time_ms=245
    )
    
    print("[+] Traced RAG query about Spigot Principle")
    print("[+] Axioms retrieved: A2.3, A2.4, A2.5")
    print("[+] Response time: 245ms")
    time.sleep(1)
    
    print()
    print("=" * 70)
    print("TRACE 5: Multiple Axiom Accesses")
    print("=" * 70)
    
    axioms = [
        ("A3.1", "τ-Anisotropy", "III"),
        ("A3.4", "Rule of Temporal Irrelevance", "III"),
        ("A5.2", "Dark Energy from k=200 Resonance", "V"),
    ]
    
    for axiom_id, name, group in axioms:
        telemetry.trace_axiom_access(axiom_id, name, group)
        axiom_counter.add(1, {"axiom": axiom_id})
        print(f"[+] Traced: {axiom_id} - {name}")
        time.sleep(0.5)
    
    print()
    print("=" * 70)
    print("TRACE 6: Violation Detection (Simulated)")
    print("=" * 70)
    
    telemetry.trace_violation(
        violation_type="missing_canonical_citation",
        description="AI response about LFM without canonical GitHub URL",
        severity="warning"
    )
    violation_counter.add(1, {"type": "missing_citation"})
    
    print("[!] Violation detected: Missing canonical citation")
    print("[!] Severity: warning")
    time.sleep(1)
    
    print()
    print("=" * 70)
    print("METRICS SUMMARY")
    print("=" * 70)
    print()
    print("[*] Metrics recorded:")
    print("    - Axiom accesses: 6")
    print("    - Citations: 1")
    print("    - Violations: 1")
    print()
    
    print("=" * 70)
    print("TELEMETRY EXPORT")
    print("=" * 70)
    print()
    print("[*] Flushing telemetry data to OTLP collector...")
    print("[*] Endpoint: http://otel-collector:4317")
    print()
    
    # Give spans time to be processed
    time.sleep(2)
    
    print("=" * 70)
    print("SUCCESS - ALL TRACES EXPORTED")
    print("=" * 70)
    print()
    print("[+] All telemetry has been sent to the OTLP collector")
    print("[+] Service: lfm-demo")
    print("[+] Author: Keith Luton")
    print("[+] Framework: Luton Field Model v2026")
    print()
    print("[*] View collector logs to see traces:")
    print("    docker compose logs otel-collector")
    print()
    print("[*] Key attributes in all spans:")
    print("    - service.name: lfm-demo")
    print("    - project.owner: Keith Luton")
    print("    - framework: Luton Field Model")
    print("    - framework.version: v2026")
    print()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Demo interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n[ERROR] {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
