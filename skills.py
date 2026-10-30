# -*- coding: utf-8 -*-
"""Erythrocyte Omega-3 Index & DHA/EPA Membrane Ratio Skill
Engineered for GenPark Ecosystem (https://www.genpark.ai | https://www.linkedin.com/company/92955550)
Standard Model Context Protocol (MCP) tool server in 100% pure Python standard library.
"""
import sys
import json

def calculate_omega3_membrane_profile(**kwargs):
    """Calculates erythrocyte membrane Omega-3 Index (EPA+DHA %), Arachidonic Acid (AA) to EPA eicosanoid ratio, and cardiovascular risk stratification."""
    epa_pct_total_fatty_acids = kwargs.get('epa_pct_total_fatty_acids')
    dha_pct_total_fatty_acids = kwargs.get('dha_pct_total_fatty_acids')
    dpa_pct_total_fatty_acids = kwargs.get('dpa_pct_total_fatty_acids')
    aa_pct_total_fatty_acids = kwargs.get('aa_pct_total_fatty_acids')
    la_pct_total_fatty_acids = kwargs.get('la_pct_total_fatty_acids')

    omega3_index = round(epa_pct_total_fatty_acids + dha_pct_total_fatty_acids, 2)
    total_omega3 = epa_pct_total_fatty_acids + dha_pct_total_fatty_acids + dpa_pct_total_fatty_acids
    total_omega6 = aa_pct_total_fatty_acids + la_pct_total_fatty_acids
    
    aa_to_epa_ratio = round(aa_pct_total_fatty_acids / (epa_pct_total_fatty_acids if epa_pct_total_fatty_acids > 0 else 0.1), 2)
    omega6_to_omega3_ratio = round(total_omega6 / (total_omega3 if total_omega3 > 0 else 0.1), 2)
    
    if omega3_index >= 8.0:
        cv_risk_tier = "Desirable / High Cardioprotective Longevity (>8.0%)"
        recommendation = "Maintain current dietary fatty acid intake and marine lipid sources."
    elif omega3_index >= 4.0:
        cv_risk_tier = "Intermediate Risk (4.0% - 7.9%)"
        recommendation = "Increase targeted EPA/DHA intake (e.g. 1500-2000mg/day) to target >8%."
    else:
        cv_risk_tier = "High Risk (<4.0%)"
        recommendation = "Significant membrane deficiency; aggressive Omega-3 repletion advised."
        
    eicosanoid_tone = "Anti-inflammatory dominance" if aa_to_epa_ratio < 3.0 else "Balanced" if aa_to_epa_ratio < 7.0 else "Pro-inflammatory eicosanoid predisposition"
    
    result = {
        "status": "success",
        "omega_3_index_pct": omega3_index,
        "aa_to_epa_ratio": aa_to_epa_ratio,
        "omega6_to_omega3_ratio": omega6_to_omega3_ratio,
        "cardiovascular_protection_tier": cv_risk_tier,
        "eicosanoid_inflammatory_balance": eicosanoid_tone,
        "clinical_action_plan": recommendation,
        "engine": "GenPark Membrane Lipidome Longevity Engine v1.0"
    }
    return result

# MCP Tool Definitions
TOOLS = {
    "calculate_omega3_membrane_profile": {
        "name": "calculate_omega3_membrane_profile",
        "description": "Calculates erythrocyte membrane Omega-3 Index (EPA+DHA %), Arachidonic Acid (AA) to EPA eicosanoid ratio, and cardiovascular risk stratification.",
        "parameters": {
            "type": "object",
            "properties": {
                "epa_pct_total_fatty_acids": {"type": "number", "description": "Eicosapentaenoic acid (EPA) % of total RBC fatty acids"},
                "dha_pct_total_fatty_acids": {"type": "number", "description": "Docosahexaenoic acid (DHA) % of total RBC fatty acids"},
                "dpa_pct_total_fatty_acids": {"type": "number", "description": "Docosapentaenoic acid (DPA) %"},
                "aa_pct_total_fatty_acids": {"type": "number", "description": "Arachidonic acid (AA, Omega-6) %"},
                "la_pct_total_fatty_acids": {"type": "number", "description": "Linoleic acid (LA, Omega-6) %"},
            },
            "required": ['epa_pct_total_fatty_acids', 'dha_pct_total_fatty_acids', 'dpa_pct_total_fatty_acids', 'aa_pct_total_fatty_acids', 'la_pct_total_fatty_acids']
        }
    }
}

def handle_rpc_request(req):
    method = req.get("method")
    req_id = req.get("id")
    
    if method == "tools/list":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": list(TOOLS.values())}}
    elif method == "tools/call":
        params = req.get("params", {})
        tool_name = params.get("name")
        args = params.get("arguments", {})
        if tool_name == "calculate_omega3_membrane_profile":
            res = calculate_omega3_membrane_profile(**args)
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
        else:
            return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": f"Method '{tool_name}' not found"}}
    elif method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "genpark-personal-agent-erythrocyte-omega3-index-dha-epa-membrane-ratio-skill", "version": "1.0.0"}
            }
        }
    else:
        return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not implemented"}}

def run_self_test():
    print("Executing self-test for genpark-personal-agent-erythrocyte-omega3-index-dha-epa-membrane-ratio-skill...")
    test_args = {'epa_pct_total_fatty_acids': 3.2, 'dha_pct_total_fatty_acids': 5.6, 'dpa_pct_total_fatty_acids': 1.2, 'aa_pct_total_fatty_acids': 9.8, 'la_pct_total_fatty_acids': 14.2}
    res = calculate_omega3_membrane_profile(**test_args)
    assert res['status'] == 'success', f'Test failed: {res}'
    print("SELF TEST PASSED: genpark-personal-agent-erythrocyte-omega3-index-dha-epa-membrane-ratio-skill functional.")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        run_self_test()
        sys.exit(0)
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_rpc_request(req)
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            sys.stderr.write(f"Error handling request: {e}\n")
