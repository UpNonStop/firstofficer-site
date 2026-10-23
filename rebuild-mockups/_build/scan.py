import re,glob,sys
from bs4 import BeautifulSoup
RULES=[r'\bseats?\b',r'\bavailability\b',r'\bheld\b',r'\bholding\b',r'just opened',r'\bVisa\b',r'MDSM',r'\bAmex\b',r'American Express',r'\bChase\b',r'Capital One',r'Citi\b',r'Bank of America',r'Wells Fargo',r'\bInk\b',r'Sapphire',r'Membership Rewards',r'Ultimate Rewards',r'our customers',r'our clients',r'\bBen\b',r'Remco',r'SOC ?2',r'\bISO\b',r'bank-level',r'\bAI\b',r'\bSMS\b',r'\$25K',r'\$35K',r'\$15K',r'\b50 programs',r'629',r'\b13 banks',r'McKinsey',r'Mastercard',r'licensed',r'Gold Card',r'Platinum',r'Venture',r'\bAmEx\b',r'Delta|United|American Airlines|SkyMiles|AAdvantage|MileagePlus|Marriott|Hilton|Hyatt|Bonvoy',r'Inter\b']
files=sys.argv[1:] or sorted(glob.glob('/workspace/fo-rebuild-mockups/*.html'))
for f in files:
    t=BeautifulSoup(open(f).read(),'lxml')
    for x in t(['script','style']): x.decompose()
    txt=re.sub(r'\s+',' ',t.get_text(' '))
    for r in RULES:
        for m in re.finditer(r,txt,re.I if r not in (r'\bAI\b',r'\bISO\b',r'\bBen\b',r'\bInk\b',r'Inter\b',r'Citi\b') else 0):
            print(f.split('/')[-1],'|',r,'|',txt[max(0,m.start()-60):m.end()+50])
