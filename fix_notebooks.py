import json
from pathlib import Path

WIDGET_VIEW_MIME = "application/vnd.jupyter.widget-view+json"


for path in Path(".").rglob("*.ipynb"):
    try:
        with open(path, "r", encoding="utf-8") as f:
            nb = json.load(f)

        changed = False
        metadata = nb.get("metadata", {})

        # GitHub Preview can fail on notebooks that carry broken widget state.
        if "widgets" in metadata:
            del metadata["widgets"]
            changed = True

        for cell in nb.get("cells", []):
            cell_metadata = cell.get("metadata", {})
            if "widgets" in cell_metadata:
                del cell_metadata["widgets"]
                changed = True

            outputs = cell.get("outputs", [])
            if not isinstance(outputs, list):
                continue

            filtered_outputs = []
            for output in outputs:
                data = output.get("data", {}) if isinstance(output, dict) else {}
                if WIDGET_VIEW_MIME in data:
                    changed = True
                    continue
                filtered_outputs.append(output)

            if len(filtered_outputs) != len(outputs):
                cell["outputs"] = filtered_outputs

        if changed:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(nb, f, ensure_ascii=False, indent=1)
                f.write("\n")
            print(f"fixed: {path}")

    except Exception as e:
        print(f"skip: {path} -> {e}")
