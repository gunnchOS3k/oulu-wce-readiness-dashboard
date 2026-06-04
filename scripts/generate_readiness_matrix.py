from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
R=ROOT/'results'; R.mkdir(exist_ok=True)
(R/'oulu_wce_readiness_matrix.md').write_text('# Readiness matrix\nSee parent oulu-wce-portfolio-alignment/OULU_WCE_SKILL_MATRIX.md\n')
(R/'oulu_wce_skill_badges.json').write_text(json.dumps({'dsp':'partial','mimo':'partial'}, indent=2))
(R/'repo_to_skill_map.md').write_text('# Repo map\n- oulu-stochastic-dsp-lab -> DSP\n')
(R/'missing_evidence_todos.md').write_text('- [ ] DeepMIMO benchmark\n- [ ] Field measurements\n')
