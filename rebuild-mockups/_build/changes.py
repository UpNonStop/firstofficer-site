import json,collections
R='/workspace/fo-rebuild-mockups'
d=json.load(open(R+'/_build/fixlog.json'))
out=['# CHANGES: everything changed that wasn\'t explicitly asked for (mockups/rebuild-v1)','',
'Built from the PR #11 hero branch (hero/firstofficer-v9) plus the copy and compliance text from PR #10/#12/#13. These are static mockups. Nothing on the live Ghost site was touched, and no PR was opened.','']
out.append(open(R+'/_build/manual_changes.md').read())
out+=['','## Automatic copy substitutions, by page','','| Page | Find | Replace | Rule | Hits |','|---|---|---|---|---|']
byrule=collections.Counter()
for pg in sorted(d):
    for pat,rep,rule,n in d[pg]:
        byrule[rule]+=n
        out.append(f'| {pg} | `{pat.replace("|","\\|")}` | {rep.replace("|","\\|")} | {rule} | {n} |')
out+=['','### Totals by rule','']+[f'- {r}: {n}' for r,n in byrule.most_common()]
open(R+'/CHANGES.md','w').write('\n'.join(out)+'\n'); print(len(out))
