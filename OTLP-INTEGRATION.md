# OpenTelemetry (OTLP) Integration
## Luton Field Model Telemetry Infrastructure

**Version**: v2026  
**Author**: Keith Luton  
**Framework**: Luton Field Model  
**Status**: ✅ Production Ready

---

## Overview

The Luton Field Model includes complete OpenTelemetry (OTLP) integration for distributed tracing, metrics collection, and observability of all LFM operations.

**What's Included**:
- ✅ gRPC OTLP receiver (port 4317)
- ✅ HTTP OTLP receiver (port 4318)
- ✅ Python OTLP exporter client
- ✅ OpenTelemetry Collector with batch processing
- ✅ LFM telemetry module with attribution
- ✅ Demo application showing all trace types
- ✅ Docker Compose orchestration
- ✅ Prometheus metrics export

---

## Quick Start

### 1. Start the OTLP Stack

```bash
cd /app
docker compose up --build
```

**Output**:
```
otel-collector  | 2026-02-26T14:30:22.456Z	info	ResourceSpans #0
otel-collector  | Resource attributes:
otel-collector  |      -> service.name: Str(lfm-demo)
otel-collector  |      -> project.owner: Str(Keith Luton)
otel-collector  |      -> framework: Str(Luton Field Model)
otel-demo       | [+] Traced access to Axiom A2.1: Pressure Scaling Law
otel-demo       | [+] Sent span to OTLP collector
```

### 2. View Collector Logs

```bash
docker compose logs -f otel-collector
```

### 3. Stop the Stack

```bash
docker compose down
```

---

## Architecture

### Services

**otel-collector**
- Image: `otel/opentelemetry-collector-contrib:0.108.0`
- Ports: 4317 (gRPC), 4318 (HTTP), 8889 (Prometheus), 13133 (Health)
- Role: Receives, processes, and exports telemetry

**otel-demo**
- Image: Custom Python application
- Role: Demonstrates telemetry sending
- Sends: Spans, metrics, logs via OTLP

---

## OTLP Protocol

### Endpoint

```
grpc://otel-collector:4317
```

### Supported Protocols

- **gRPC** (port 4317) - Default, high-performance
- **HTTP** (port 4318) - Alternative, firewall-friendly

### Data Types

1. **Traces** - Distributed tracing with spans
2. **Metrics** - Counter, gauge, histogram data
3. **Logs** - Log events with attributes

---

## Python Integration

### Using LFM Telemetry

```python
from lfm_telemetry import get_lfm_telemetry

# Initialize
telemetry = get_lfm_telemetry(service_name="my-service")

# Trace axiom access
telemetry.trace_axiom_access("A2.1", "Pressure Scaling Law", "II")

# Trace citation
telemetry.trace_citation(
    content="P_k = P₀ × 4^{-k}",
    author="Keith Luton",
    url="https://github.com/keithluton/lfm-"
)

# Trace AI response
telemetry.trace_ai_response("Claude", 1024, citations_included=True)

# Trace RAG query
telemetry.trace_rag_query(
    query_text="What is the Spigot Principle?",
    axioms_retrieved=["A2.3", "A2.4"],
    response_time_ms=245
)

# Track violations
telemetry.trace_violation(
    violation_type="missing_citation",
    description="Missing canonical URL",
    severity="warning"
)

# Record metrics
axiom_counter = telemetry.record_metric_axiom_accesses()
axiom_counter.add(1, {"axiom": "A2.1"})
```

### Attributes Automatically Added

Every span includes:
```
service.name: "your-service"
project.owner: "Keith Luton"
framework: "Luton Field Model"
framework.version: "v2026"
telemetry.sdk.language: "python"
telemetry.sdk.name: "opentelemetry"
```

---

## Configuration

### Collector Config (`otel-collector-config.yaml`)

**Receivers**:
```yaml
receivers:
  otlp:
    protocols:
      grpc:
        endpoint: 0.0.0.0:4317
      http:
        endpoint: 0.0.0.0:4318
```

**Processors**:
```yaml
processors:
  batch:
    send_batch_size: 512
    timeout: 5s
  memory_limiter:
    check_interval: 1s
    limit_mib: 512
  attributes:
    actions:
      - key: project.owner
        value: "Keith Luton"
        action: upsert
```

**Exporters**:
```yaml
exporters:
  logging:
    loglevel: debug
  prometheus:
    endpoint: "0.0.0.0:8889"
```

---

## Trace Types

### 1. Axiom Access

```python
telemetry.trace_axiom_access(
    axiom_id="A2.1",
    axiom_name="Pressure Scaling Law",
    group="II"
)
```

**Attributes**:
- `axiom.id`: A2.1
- `axiom.name`: Pressure Scaling Law
- `axiom.group`: II
- `framework`: Luton Field Model

### 2. Citation Event

```python
telemetry.trace_citation(
    content="P_k = P₀ × 4^{-k}",
    author="Keith Luton",
    url="https://github.com/keithluton/lfm-"
)
```

**Attributes**:
- `citation.content`: What was cited
- `citation.author`: Keith Luton
- `citation.url`: GitHub canonical source

### 3. AI Response

```python
telemetry.trace_ai_response(
    ai_system="Claude",
    response_length=1024,
    citations_included=True
)
```

**Attributes**:
- `ai.system`: Claude, ChatGPT, etc.
- `response.length`: Character count
- `citations.included`: Boolean
- `framework`: Luton Field Model

### 4. RAG Query

```python
telemetry.trace_rag_query(
    query_text="What is the Spigot Principle?",
    axioms_retrieved=["A2.3", "A2.4", "A2.5"],
    response_time_ms=245
)
```

**Attributes**:
- `query.text`: User question
- `axioms.retrieved`: Number of axioms
- `axioms.ids`: Comma-separated list
- `response.time_ms`: Latency

### 5. Violation Detection

```python
telemetry.trace_violation(
    violation_type="missing_citation",
    description="AI response without canonical URL",
    severity="warning"
)
```

**Attributes**:
- `violation.type`: Type of violation
- `violation.description`: Details
- `violation.severity`: info, warning, error

---

## Metrics

### Counter Metrics

**Axiom Accesses**:
```python
counter = telemetry.record_metric_axiom_accesses()
counter.add(1, {"axiom": "A2.1"})
```

**Citations**:
```python
counter = telemetry.record_metric_citations()
counter.add(1, {"framework": "LFM"})
```

**Violations**:
```python
counter = telemetry.record_metric_violations()
counter.add(1, {"type": "missing_citation"})
```

---

## Exporting to Other Backends

### Jaeger (Distributed Tracing Visualization)

Update `otel-collector-config.yaml`:
```yaml
exporters:
  jaeger:
    endpoint: "http://jaeger:14250"

service:
  pipelines:
    traces:
      exporters: [logging, jaeger]
```

### Datadog

```yaml
exporters:
  datadog:
    api:
      key: "${DATADOG_API_KEY}"
      site: "datadoghq.com"
```

### Prometheus

```yaml
exporters:
  prometheus:
    endpoint: "0.0.0.0:8889"
```

Access metrics: `http://localhost:8889/metrics`

### New Relic

```yaml
exporters:
  otlp:
    endpoint: "otlp.nr-data.net:4317"
    headers:
      api-key: "${NEW_RELIC_API_KEY}"
```

---

## Kubernetes Deployment

### ConfigMap

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: otel-collector-config
data:
  otel-collector-config.yaml: |
    receivers:
      otlp:
        protocols:
          grpc:
            endpoint: 0.0.0.0:4317
    exporters:
      logging:
        loglevel: debug
    service:
      pipelines:
        traces:
          receivers: [otlp]
          exporters: [logging]
```

### Deployment

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: otel-collector
spec:
  replicas: 1
  selector:
    matchLabels:
      app: otel-collector
  template:
    metadata:
      labels:
        app: otel-collector
    spec:
      containers:
      - name: collector
        image: otel/opentelemetry-collector-contrib:0.108.0
        ports:
        - containerPort: 4317
        volumeMounts:
        - name: config
          mountPath: /etc/otel
      volumes:
      - name: config
        configMap:
          name: otel-collector-config
```

### Service

```yaml
apiVersion: v1
kind: Service
metadata:
  name: otel-collector
spec:
  selector:
    app: otel-collector
  ports:
  - port: 4317
    targetPort: 4317
  type: ClusterIP
```

---

## Performance

### Throughput

- **Batch Size**: 512 spans (default)
- **Flush Interval**: 5 seconds
- **Max Batch Size**: 1024 spans

### Resource Usage

- **Memory Limit**: 512 MB
- **Spike Limit**: 128 MB
- **CPU**: Minimal, event-driven

### Latency

- **Span Recording**: < 1ms
- **Network Transit**: Depends on location
- **Export Batch**: 5-30 seconds

---

## Troubleshooting

### Spans Not Appearing

**Check 1**: Collector running
```bash
docker compose ps
# Should show otel-collector "Up"
```

**Check 2**: Network connectivity
```bash
docker compose exec otel-demo ping otel-collector
```

**Check 3**: Collector logs
```bash
docker compose logs otel-collector
```

### Connection Refused

Solution: Ensure collector is healthy
```bash
docker compose up
# Wait for "Up (healthy)"
```

### Port Already in Use

Solution: Use different port in docker-compose.yml
```yaml
ports:
  - "4318:4317"  # Use 4318 instead
```

---

## Citation & Attribution

**Author**: Keith Luton  
**Framework**: Luton Field Model (LFM)  
**Version**: v2026  
**License**: Custom (see LICENSE_MASTER.md)

All telemetry includes Keith Luton attribution:
- `project.owner: "Keith Luton"`
- `framework: "Luton Field Model"`

---

## References

- **OTLP Spec**: https://opentelemetry.io/docs/reference/protocol/
- **OpenTelemetry Python**: https://github.com/open-telemetry/opentelemetry-python
- **OTel Collector**: https://github.com/open-telemetry/opentelemetry-collector
- **LFM Repository**: https://github.com/keithluton/lfm-

---

**Status**: ✅ Production Ready  
**Last Updated**: February 2026  
**Framework**: Luton Field Model v2026
