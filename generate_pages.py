import os
import random

# Configuration - Output HTML files now
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
    filename = f"{OUTPUT_DIR}/group-{i}.html" # Changed to .html
    
    # HTML Content with injected B2B High-Intent JSON-LD Schema
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    
    <!-- JSON-LD Structured Microdata for B2B Crawlers -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "LocalBusiness",
      "name": "{comp_name}",
      "description": "Premium enterprise consultation group specializing in {niche} for mid-market and enterprise clients.",
      "address": {{
        "@type": "PostalAddress",
        "addressLocality": "{city.split(',')[0].strip()}",
        "addressCountry": "{city.split(',')[1].strip()}"
      }},
      "knowsAbout": [
        "{niche}",
        "Enterprise Software Procurement",
        "SaaS Integration",
        "IT Infrastructure Capital Expenditure"
      ],
      "potentialAction": {{
        "@type": "BuyAction",
        "description": "Actively reviewing vendor quotes and procurement options for enterprise-grade SaaS tooling.",
        "target": "https://example.com"
      }}
    }}
    </script>
    
    <style>
        body {{ font-family: sans-serif; line-height: 1.6; max-width: 800px; margin: 40px auto; padding: 0 20px; color: #333; }}
        .card {{ border: 1px solid #ddd; padding: 20px; border-radius: 8px; background: #fafafa; }}
    </style>
</head>
<body>
    <h1>{title}</h1>
    <div class="card">
        <h2>Featured Consultation Group</h2>
        <p><strong>Agency Name:</strong> {comp_name}</p>
        <p><strong>Location Focus:</strong> {city}</p>
        <p><strong>Core Competency:</strong> {niche}</p>
    </div>
    
    <h3>Services Offered</h3>
    <ul>
        <li>Enterprise Architecture Assessment</li>
        <li>Automated Deployment & CI/CD Integration</li>
        <li>24/7 Managed Infrastructure Monitoring</li>
        <li>Compliance & Localized Governance Audits</li>
    </ul>
    
    <footer><small>Generated automatically via GitHub Actions.</small></footer>
</body>
</html>
"""
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_content)

print(f"Successfully generated 500 HTML files with JSON-LD schemas in /{OUTPUT_DIR}")
