#!/usr/bin/env bash
# Push this folder as ONE commit to the GitHub repository (state only, no history).
# Unpack the zip into a fresh folder and run the script there — not over an old clone, whose stale files would be committed too.
#   ./push.sh                      -> pushes to https://github.com/frnkptrln/peer-pressure-without-peers
#   ./push.sh owner/other-name     -> pushes to another repository
#   FORCE=1 ./push.sh              -> when the repository already has commits (an earlier push, or GitHub's initial README/LICENSE): its history is replaced by this commit
# Needs git with working GitHub credentials (credential helper or SSH); gh is not required.
set -euo pipefail
REPO="${1:-frnkptrln/peer-pressure-without-peers}"
URL="https://github.com/$REPO.git"
if [ ! -d .git ]; then git init -q; fi
git add -A
git commit -q -m "Peer pressure without peers — harness, run records and papers (AI Incident Response Sprint, 11–13 September 2026)" || echo "nothing new to commit"
git branch -M main
git remote remove origin 2>/dev/null || true
git remote add origin "$URL"
if git push -u origin main; then
  echo "pushed to https://github.com/$REPO"
elif [ "${FORCE:-0}" = "1" ]; then
  git push -u origin main --force && echo "pushed (replaced the repository's earlier commits) to https://github.com/$REPO"
else
  echo "push rejected: the repository already has commits (an earlier push, or GitHub-generated README/LICENSE). Re-run with FORCE=1 ./push.sh to replace its history with this state." >&2
  exit 1
fi
