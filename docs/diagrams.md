# Architecture Diagrams

This page provides visual representations of the internal architecture and execution flow of **mini-scanner**.

---

# High-Level Architecture

```mermaid
flowchart TD

A[CLI] --> B[Argument Parser]
B --> C[Configuration]
C --> D[Scanner Engine]
D --> E[Thread Pool]
E --> F[TCP Connections]
F --> G[Result Aggregator]
G --> H[Formatter]
H --> I[Console Output]
H --> J[JSON Output]
```

---

# Scan Lifecycle

```mermaid
sequenceDiagram

participant User
participant CLI
participant Scanner
participant Socket

User->>CLI: Start scan
CLI->>Scanner: Validate arguments
Scanner->>Scanner: Parse ports
Scanner->>Scanner: Resolve hostname

loop For each port
Scanner->>Socket: connect()
Socket-->>Scanner: Open / Closed
Scanner->>Socket: Read banner (optional)
Socket-->>Scanner: Banner
end

Scanner->>CLI: Results
CLI->>User: Display output
```

---

# Thread Pool Workflow

```mermaid
flowchart LR

Queue[Port Queue]

Worker1 --> Queue
Worker2 --> Queue
Worker3 --> Queue
Worker4 --> Queue

Queue --> Socket
Socket --> Results
Results --> Formatter
```

---

# Configuration Priority

```mermaid
flowchart TD

CLI[CLI Arguments]

ENV[Environment Variables]

DEFAULTS[Default Values]

CLI --> CONFIG
ENV --> CONFIG
DEFAULTS --> CONFIG

CONFIG --> Scanner
```

---

# Port Processing

```mermaid
flowchart TD

Start --> Parse
Parse --> Validate
Validate --> DuplicateCheck
DuplicateCheck --> Sort
Sort --> Scan
```

---

# Socket Lifecycle

```mermaid
stateDiagram-v2

[*] --> Created

Created --> Connected
Created --> Failed

Connected --> Banner

Banner --> Closed

Failed --> Closed

Closed --> [*]
```

---

# Result Pipeline

```mermaid
flowchart LR

TCP --> Result
Banner --> Result

Result --> Formatter

Formatter --> Text
Formatter --> JSON
```

---

# Error Handling

```mermaid
flowchart TD

Start --> ResolveHost

ResolveHost -->|Failure| DNSError

ResolveHost -->|Success| Scan

Scan --> Socket

Socket -->|Timeout| Timeout

Socket -->|Refused| Closed

Socket -->|Connected| Open
```

---

# Future Architecture

```mermaid
flowchart TD

CLI --> Core

Core --> TCP

Core --> UDP

Core --> IPv6

Core --> Plugins

Core --> Async

Core --> Formatter

Formatter --> JSON

Formatter --> YAML

Formatter --> CSV

Formatter --> XML
```

---

# Design Principles

```mermaid
mindmap
  root((mini-scanner))
    Simple
    Modular
    Testable
    Secure
    Extensible
    Cross Platform
    Well Documented
```