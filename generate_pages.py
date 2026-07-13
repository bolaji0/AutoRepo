import os
import random

# Configuration
OUTPUT_DIR = "consultation-groups"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Data Pools
TECH_NICHES = [
    "Cloudflare Zero Trust Architecture Implementation Partners",
    "Kubernetes Multi-Cluster Orchestration Specialists",
    "Datadog APM & Observability Integrators",
    "HashiCorp Vault Secrets Management Consultants",
    "Apache Kafka Real-Time Data Pipeline Architects"
]

CITIES = [
    "Graz, Austria", "Ghent, Belgium", "Turku, Finland", 
    "Nantes, France", "Brno, Czech Republic", "Utrecht, Netherlands",
    "Oulu, Finland", "Coimbra, Portugal", "Basel, Switzerland"
]

COMPANY_PREFIXES = ["Apex", "Vertex", "Quantum", "Stratum", "Nexus", "Core"]
COMPANY_SUFFIXES = ["Systems", "Consulting", "Solutions", "Integrators", "Labs"]

# Generation Logic
for i in range(1, 501):
    niche = random.choice(TECH_NICHES)
    city = random.choice(CITIES)
    comp_name = f"{random.choice(COMPANY_PREFIXES)} {random.choice(COMPANY_SUFFIXES)}"
    
    title = f"{niche} in {city}"
    filename = f"{OUTPUT_DIR}/group-{i}.md"
    
    markdown_content = f"""# {title}

Welcome to the official directory for **{title}**.

## Featured Consultation Group
* **Agency Name:** {comp_name}
* **Location Focus:** {city}
* **Core Core competency:** {niche}

## Services Offered
1. Enterprise Architecture Assessment
2. Automated Deployment & CI/CD Integration
3. 24/7 Managed Infrastructure Monitoring
4. Compliance & Localized Governance Audits

*Generated automatically via GitHub Actions.*
"""
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(markdown_content)

print(f"Successfully generated 500 files in /{OUTPUT_DIR}")
