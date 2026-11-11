-- The Book form's wallet (assets/fo-wallet-cards.js) is a snapshot of this query on Supabase cuzuzzbezswvejnoskum.
-- Read-only. Re-run when cards_reference changes, then regenerate the file (same ordering rules as its header).
select json_agg(json_build_array(issuer,
         case when card_class = 'business' then 'b' else 'p' end,
         card_name,
         case when coalesce(cobrand_partner, '') = '' then 0 else 1 end,
         coalesce(annual_fee, 0))
       order by issuer, card_class, card_name) as rows
from public.cards_reference
where card_type not in ('personal_debit', 'secured')
  and not coalesce(discontinued, false);
