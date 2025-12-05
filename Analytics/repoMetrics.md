flowchart TD
style TD fill:#0B3D91,stroke:#000,color:#fff
A[Tanjiro - Commits: 42/week] --> B[Zenitsu - PRs merged: 8/week]
B --> C[Nezuko - Test pass rate: 96%]
C --> D[MugenTrain - Deployments: 3/mo \n Success 99%]
B --> E[Inosuke - Code churn (20% files changed/mo)]
E --> F[Hashira - Security alerts: 1 open]
D --> G[Observability - Errors: 0.2% || Latency 120ms]
classDef theme fill:#111827,stroke:#f97316,color:#fff;
class A,B,C,D,E,F,G theme


click A "#commits" "View commits"
click B "#prs" "View PRs"
click C "#tests" "View tests"
click F "#security" "View security"

graph LR
subgraph PRs
PR1[Mon] -->|2 merged| PR2[Tue]
PR2 -->|1 merged| PR3[Wed]
PR3 -->|3 merged| PR4[Thu]
PR4 -->|2 merged| PR5[Fri]
end

pie
title Test Coverage (Nezuko)
"Covered: 85%" : 85
"Missing: 15%" : 15

gantt
title Release Cadence — MugenTrain
dateFormat YYYY-MM-DD
section Releases
Alpha: done, a1, 2025-09-01, 7d
Beta: active, a2, 2025-10-01, 14d
Prod: planned, a3, 2025-11-15, 3d
section Hotfixes
CriticalPatch: after a2, 2d


flowchart TB
S0[Hashira Guard] --> S1[Dependabot PRs: 2 open]
S0 --> S2[SAST: last run OK]
S0 --> S3[Secrets scan: no leaks]
S1 --> S4[Auto-merge? No - manual review]


