set -e; cd /workspace/fo-rebuild-mockups; rm -f _build/fixlog.json
python3 _build/build_generic.py >/dev/null; python3 _build/build_home.py >/dev/null; python3 _build/build_bespoke.py >/dev/null; python3 _build/build_upns.py >/dev/null; python3 _build/build_flows.py >/dev/null
echo built $(ls *.html | wc -l)
