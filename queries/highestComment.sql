select text from (select cid, text, upvotes, rank() over (partition by classID) order by upvotes DESC) 
as rank from (cid join taken)) as renamed where rank=1;
