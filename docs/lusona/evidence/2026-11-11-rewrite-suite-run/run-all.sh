#!/bin/bash
cd ~/code/_lusona_/ai-skills
S=tdd-stated,authz-change,status-check,investigate-bug,decision-conflict,decision-revised,old-records
R=tdd-stated,authz-change,status-check,investigate-bug
python3 tmp/w14run/driver.py claude tmp/w14run/conditions/claude-draft tmp/w14run/runs/draft 60 $S 5 &
python3 tmp/w14run/driver.py codex tmp/w14run/conditions/codex-draft tmp/w14run/runs/draft 60 $S 5 &
wait
echo "draft done $(date +%T)"
[ -e tmp/w14run/runs/draft/STOP ] && { echo "draft STOP present; not starting reference"; exit 3; }
python3 tmp/w14run/driver.py claude tmp/w14run/conditions/claude-base tmp/w14run/runs/base 60 $R 5 &
python3 tmp/w14run/driver.py codex tmp/w14run/conditions/codex-base tmp/w14run/runs/base 60 $R 5 &
wait
echo "base done $(date +%T)"
