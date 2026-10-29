/* FO_REDEMPTION_BASIS: what a point is worth, by how it is redeemed. US cents per point, est.
   Built on the floor · mid · ceiling approach (valuation/methodology.md):
     floor   = what the issuer pays on a plain cash-out, no skill needed
     mid     = what a well-run booking of that type typically gets
     ceiling = a level a well-planned booking can reach again and again, not a one-off
   Every figure is an ESTIMATE. None of these come from logged desk bookings.
   To drop in verified desk figures later, fill `desk` per type: {median:1.7, n:24, asOf:'2027-01-31'}.
   The page shows a desk figure only when n >= 10, always with its n. Mockup only. */
window.FO_REDEMPTION_BASIS={
  version:'est-2026-10',
  util:.85,          /* share of earned points counted in any value */
  fee:6600,          /* $550 a month */
  gate:25000,        /* ~$25K a month on cards */
  types:[
    {id:'mix',  name:'A mix of trips and cash out', short:'Mixed',    floor:1.0, mid:1.3,  ceil:1.6, note:'The default. Some trips, some cash.'},
    {id:'cash', name:'Cash out or statement credit', short:'Cash out', floor:1.0, mid:1.0,  ceil:1.0, note:'The guaranteed floor.'},
    {id:'econ', name:'Economy flights',              short:'Economy',  floor:1.0, mid:1.2,  ceil:1.4, note:'Domestic and short-haul.'},
    {id:'hotel',name:'Top hotel nights',             short:'Hotels',   floor:1.2, mid:1.6,  ceil:2.0, note:'Transferred to the right hotel program.'},
    {id:'biz',  name:'Business class',               short:'Business', floor:1.5, mid:1.75, ceil:2.0, note:'Long-haul, through airline partners.'}
  ],
  desk:{}            /* verified desk redemption medians go here, per type id. Empty: none shown. */
};
