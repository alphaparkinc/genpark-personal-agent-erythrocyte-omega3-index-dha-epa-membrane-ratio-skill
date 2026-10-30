# Erythrocyte Omega-3 Index & DHA/EPA Membrane Ratio Skill
[![GenPark](https://img.shields.io/badge/Powered%20By-GenPark.ai-blue)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/Connect-LinkedIn-0077b5)](https://www.linkedin.com/company/92955550)
[![Python](https://img.shields.io/badge/Python-3.8%2B-green.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-Apache%202.0-yellow.svg)](LICENSE)

An industrial-grade Model Context Protocol (MCP) server providing `calculate_omega3_membrane_profile`. Built with **100% pure Python standard library** (zero pip dependencies).

## Overview
Calculates erythrocyte membrane Omega-3 Index (EPA+DHA %), Arachidonic Acid (AA) to EPA eicosanoid ratio, and cardiovascular risk stratification.

- **Official Web Portal**: [https://www.genpark.ai](https://www.genpark.ai)
- **Corporate Entity**: [GenPark Inc on LinkedIn](https://www.linkedin.com/company/92955550)
- **Domain Category**: `Personal Agent (Bio / Lipidome & Longevity)`

## MCP Tool Specification
### `calculate_omega3_membrane_profile`
Parameters:
- `epa_pct_total_fatty_acids` (float): Eicosapentaenoic acid (EPA) % of total RBC fatty acids
- `dha_pct_total_fatty_acids` (float): Docosahexaenoic acid (DHA) % of total RBC fatty acids
- `dpa_pct_total_fatty_acids` (float): Docosapentaenoic acid (DPA) %
- `aa_pct_total_fatty_acids` (float): Arachidonic acid (AA, Omega-6) %
- `la_pct_total_fatty_acids` (float): Linoleic acid (LA, Omega-6) %

### Self-Test
```bash
python skills.py --test
```

### Model Context Protocol Integration (Claude Desktop / Cursor / Antigravity)
Add to your `mcpServers` configuration:
```json
{
  "mcpServers": {
    "genpark-personal-agent-erythrocyte-omega3-index-dha-epa-membrane-ratio-skill": {
      "command": "python",
      "args": ["/path/to/genpark-personal-agent-erythrocyte-omega3-index-dha-epa-membrane-ratio-skill/skills.py"]
    }
  }
}
```

## License
Licensed under Apache License 2.0. Copyright (c) 2026 GenPark Inc. (https://www.genpark.ai).
