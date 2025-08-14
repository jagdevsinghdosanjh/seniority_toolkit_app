def compare_entries(seniority_text, objection_text):
    results = []

    seniority_lines = seniority_text.splitlines()
    objection_lines = objection_text.splitlines()

    for line in seniority_lines:
        matched = any(objection in line for objection in objection_lines)
        results.append({
            "entry": line,
            "matched": matched
        })

    return results
