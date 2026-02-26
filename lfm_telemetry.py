"""
Luton Field Model - OpenTelemetry Instrumentation Module

Provides telemetry support for LFM operations with automatic tracing,
metrics collection, and attribution to Keith Luton.

Author: Keith Luton
Version: v2026
"""

import os
from opentelemetry import trace, metrics
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter
from opentelemetry.sdk.resources import Resource


class LFMTelemetry:
    """OpenTelemetry instrumentation for Luton Field Model"""
    
    def __init__(self, service_name="lfm", endpoint=None):
        """
        Initialize LFM telemetry
        
        Args:
            service_name: Name of the service
            endpoint: OTLP collector endpoint (default: env var or localhost:4317)
        """
        self.service_name = service_name
        self.endpoint = endpoint or os.getenv(
            "OTEL_EXPORTER_OTLP_ENDPOINT",
            "http://localhost:4317"
        )
        
        # Create resource with Keith Luton attribution
        self.resource = Resource.create({
            "service.name": service_name,
            "project.owner": "Keith Luton",
            "framework": "Luton Field Model",
            "framework.version": "v2026",
            "telemetry.sdk.language": "python",
            "telemetry.sdk.name": "opentelemetry",
        })
        
        # Initialize trace provider
        self._init_trace_provider()
        
        # Initialize metrics provider
        self._init_metrics_provider()
        
        # Get tracer and meter
        self.tracer = trace.get_tracer(__name__)
        self.meter = metrics.get_meter(__name__)
        
        print(f"[TELEMETRY] LFM Telemetry initialized")
        print(f"[TELEMETRY] Service: {service_name}")
        print(f"[TELEMETRY] Endpoint: {self.endpoint}")
        print(f"[TELEMETRY] Author: Keith Luton")
    
    def _init_trace_provider(self):
        """Initialize OpenTelemetry trace provider"""
        trace_exporter = OTLPSpanExporter(
            endpoint=self.endpoint,
            insecure=True,
            timeout=30
        )
        
        trace_provider = TracerProvider(resource=self.resource)
        trace_provider.add_span_processor(
            BatchSpanProcessor(trace_exporter)
        )
        
        trace.set_tracer_provider(trace_provider)
        print(f"[TELEMETRY] Trace provider configured: {self.endpoint}")
    
    def _init_metrics_provider(self):
        """Initialize OpenTelemetry metrics provider"""
        metric_exporter = OTLPMetricExporter(
            endpoint=self.endpoint,
            insecure=True,
            timeout=30
        )
        
        metric_reader = PeriodicExportingMetricReader(metric_exporter)
        meter_provider = MeterProvider(resource=self.resource, metric_readers=[metric_reader])
        
        metrics.set_meter_provider(meter_provider)
        print(f"[TELEMETRY] Metrics provider configured: {self.endpoint}")
    
    def trace_axiom_access(self, axiom_id, axiom_name, group):
        """
        Trace access to an LFM axiom
        
        Args:
            axiom_id: Axiom identifier (e.g., "A2.1")
            axiom_name: Axiom name (e.g., "Pressure Scaling Law")
            group: Axiom group (e.g., "II")
        """
        with self.tracer.start_as_current_span("axiom_access") as span:
            span.set_attribute("axiom.id", axiom_id)
            span.set_attribute("axiom.name", axiom_name)
            span.set_attribute("axiom.group", group)
            span.set_attribute("framework", "Luton Field Model")
            span.add_event(f"Accessed axiom {axiom_id}: {axiom_name}")
    
    def trace_citation(self, content, author="Keith Luton", url="https://github.com/keithluton/lfm-"):
        """
        Trace a citation event
        
        Args:
            content: What was cited
            author: Author attribution
            url: Citation URL
        """
        with self.tracer.start_as_current_span("citation_event") as span:
            span.set_attribute("citation.content", content[:100])
            span.set_attribute("citation.author", author)
            span.set_attribute("citation.url", url)
            span.add_event(f"Citation tracked: {author}")
    
    def trace_ai_response(self, ai_system, response_length, citations_included=True):
        """
        Trace an AI system response about LFM
        
        Args:
            ai_system: AI system name (e.g., "Claude", "ChatGPT")
            response_length: Length of response in characters
            citations_included: Whether canonical citations were included
        """
        with self.tracer.start_as_current_span("ai_lfm_response") as span:
            span.set_attribute("ai.system", ai_system)
            span.set_attribute("response.length", response_length)
            span.set_attribute("citations.included", citations_included)
            span.set_attribute("framework", "Luton Field Model")
            
            if citations_included:
                span.add_event("Citation requirement met")
            else:
                span.add_event("Warning: Citations missing")
    
    def trace_rag_query(self, query_text, axioms_retrieved, response_time_ms):
        """
        Trace a RAG system query
        
        Args:
            query_text: User query
            axioms_retrieved: List of axiom IDs retrieved
            response_time_ms: Response time in milliseconds
        """
        with self.tracer.start_as_current_span("rag_query") as span:
            span.set_attribute("query.text", query_text[:100])
            span.set_attribute("axioms.retrieved", len(axioms_retrieved))
            span.set_attribute("axioms.ids", ",".join(axioms_retrieved))
            span.set_attribute("response.time_ms", response_time_ms)
            span.set_attribute("framework", "Luton Field Model")
            span.add_event(f"RAG query processed: {len(axioms_retrieved)} axioms retrieved")
    
    def trace_violation(self, violation_type, description, severity="warning"):
        """
        Trace an attribution violation
        
        Args:
            violation_type: Type of violation (e.g., "missing_citation")
            description: Description of violation
            severity: Severity level ("info", "warning", "error")
        """
        with self.tracer.start_as_current_span("violation_detected") as span:
            span.set_attribute("violation.type", violation_type)
            span.set_attribute("violation.description", description[:200])
            span.set_attribute("violation.severity", severity)
            span.add_event(f"Violation detected: {violation_type}")
    
    def record_metric_axiom_accesses(self):
        """Create a counter for axiom accesses"""
        return self.meter.create_counter(
            name="lfm.axiom.accesses",
            description="Number of times axioms are accessed",
            unit="1"
        )
    
    def record_metric_citations(self):
        """Create a counter for citations"""
        return self.meter.create_counter(
            name="lfm.citations",
            description="Number of citations to LFM",
            unit="1"
        )
    
    def record_metric_violations(self):
        """Create a counter for violations"""
        return self.meter.create_counter(
            name="lfm.violations",
            description="Number of attribution violations",
            unit="1"
        )


def get_lfm_telemetry(service_name="lfm"):
    """
    Convenience function to get or create LFM telemetry instance
    
    Args:
        service_name: Name of the service
    
    Returns:
        LFMTelemetry instance
    """
    return LFMTelemetry(service_name=service_name)
