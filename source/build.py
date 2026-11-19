import json
months=[
 dict(label="Mar 2026*",total=189.00,card=None,cash=None,partial=True),
 dict(label="Apr 2026",total=1130.00,card=None,cash=None),
 dict(label="May 2026",total=1280.00,card=None,cash=None),
 dict(label="Jun 2026",total=1113.00,card=None,cash=None),
 dict(label="Jul 2026",total=1251.50,card=238.75,cash=1012.75),
 dict(label="Aug 2026",total=1195.25,card=166.75,cash=1028.50),
 dict(label="Sep 2026",total=681.75,card=213.75,cash=468.00),
 dict(label="Oct 2026",total=540.25,card=119.25,cash=421.00),
]
for m in months: m.setdefault("partial",False)
total=sum(m["total"] for m in months)
s1=sum(m["total"] for m in months[:4]); s2=sum(m["total"] for m in months[4:])
c1=round(s1*0.10,2); c2=round(s2*0.10,2)
comm=[dict(period="March 25 – June 30, 2026",sales=s1,comm=c1,status="Paid · July 3, 2026"),
      dict(period="July 1 – October 31, 2026",sales=s2,comm=c2,status="Paid · November 18, 2026"),
      dict(period="November 2026 onward",sales=0,comm=0,status="Next payment after January 31, 2027")]
full=[m["total"] for m in months[1:]]
avg=sum(full)/len(full)*0.10
visits=[("Mar",2),("Apr",9),("May",9),("Jun",8),("Jul",4),("Aug",5),("Sep",4),("Oct",5),("Nov",2)]
HPV=7.5
nv=sum(n for _,n in visits); hrs=nv*HPV
work=[
 dict(k="Service visits since install",v=f"≈{nv}",p="Up to twice a week from March to June while we stabilised the machine and its product mix, then about once a week."),
 dict(k="Hours per visit",v=f"{HPV:g} h",p="2 h driving (about one hour each way from our Cambridge warehouse), 1.5 h on site, and 4 h buying stock, planning the refill and checking sales."),
 dict(k="Our time so far",v=f"≈{hrs:,.0f} h",p="All of it paid by Buenavyda, plus fuel on every trip. None of it is deducted from your 10%."),
 dict(k="Machine, delivered and installed",v="+$10,000",p="Combo vending machine, Nayax card reader, coin mechanism, bill acceptor, $269 of coins for change, delivery to Delhi and 13% HST. All amounts in CAD."),
 dict(k="Requests answered",v="3",p="Gum instead of juice, Dr Pepper back, and Fanta options, each changed at the next visit."),
]
labour=hrs*25*(1+0.0595+0.02282+0.04)*1.05
km=nv*200; drive=5000*0.73+(km-5000)*0.67
inv=[dict(item="Vending machine, card reader, coin and bill units, delivery, HST",amt=9731.00,how="Supplier invoices"),
 dict(item="Coins loaded for change",amt=269.00,how="Supplier invoices"),
 dict(item="First full load of products",amt=255,how="≈208 items at our cost (about half the selling price)"),
 dict(item=f"Our time: ≈{hrs:,.0f} hours",amt=round(labour),how="$25/h plus employer CPP 5.95%, EI 2.28%, 4% vacation pay and ≈5% payroll and accounting"),
 dict(item=f"Driving: ≈{km:,} km",amt=round(drive),how=f"{nv} round trips of ≈200 km at the 2026 CRA rate (73¢ first 5,000 km, 67¢ after)")]
invT=round(sum(r["amt"] for r in inv)+0.01)
VIDEO=""
PRODUCTS=[{"name": "Large gummies (Maynards)", "qty": 23, "amt": 0}, {"name": "Coca-Cola can", "qty": 22, "amt": 0}, {"name": "Coke Zero bottle", "qty": 22, "amt": 0}, {"name": "Coca-Cola bottle", "qty": 21, "amt": 0}, {"name": "Small gummies", "qty": 20, "amt": 0}, {"name": "Coke Zero can", "qty": 19, "amt": 0}, {"name": "Aero", "qty": 19, "amt": 0}, {"name": "Dr Pepper", "qty": 18, "amt": 0}, {"name": "Reese's", "qty": 18.0, "amt": 0}, {"name": "Oh Henry!", "qty": 18, "amt": 0}, {"name": "Pepsi bottle", "qty": 15, "amt": 0}, {"name": "Snickers", "qty": 13, "amt": 0}, {"name": "Twix", "qty": 13.0, "amt": 0}, {"name": "Pepsi can", "qty": 11, "amt": 0}, {"name": "Diet Coke", "qty": 10, "amt": 0}, {"name": "Takis", "qty": 9, "amt": 0}, {"name": "Fanta Orange", "qty": 7, "amt": 0}, {"name": "Kit Kat", "qty": 7, "amt": 0}, {"name": "Ruffles All Dressed", "qty": 7, "amt": 0}, {"name": "Fanta Strawberry", "qty": 6, "amt": 0}, {"name": "Gatorade Fruit Punch", "qty": 5, "amt": 0}, {"name": "Lay's", "qty": 5, "amt": 0}, {"name": "Fanta Ghost Face Punch", "qty": 3, "amt": 0}, {"name": "Fanta Pineapple", "qty": 2, "amt": 0}, {"name": "Canada Dry Zero", "qty": 2, "amt": 0}, {"name": "Cheetos", "qty": 2, "amt": 0}, {"name": "Diet Pepsi", "qty": 1, "amt": 0}, {"name": "Canada Dry Ginger Ale", "qty": 1, "amt": 0}]
CATS=[{"name": "Cans & drinks", "qty": 107, "amt": 0}, {"name": "Chocolate", "qty": 88.0, "amt": 0}, {"name": "Bottles", "qty": 58, "amt": 0}, {"name": "Gummies & gum", "qty": 43, "amt": 0}, {"name": "Chips & Takis", "qty": 23, "amt": 0}]
HEAT={"hours": ["8 am", "9 am", "10 am", "11 am", "12 pm", "1 pm", "2 pm", "3 pm", "4 pm", "5 pm", "6 pm", "7 pm", "8 pm", "9 pm", "10 pm", "11 pm"], "z": [0, 0, 0, 2, 1, 5, 1, 3, 3, 4, 1, 2, 4, 7, 7, 2], "days": []}
D=dict(video=VIDEO,inv=inv,invTotal=invT,earned=c1+c2,months=months,comm=comm,work=work,avgMonthlyComm=avg,visits=[dict(month=m,n=n) for m,n in visits],hpv=HPV,
       heat=HEAT,products=PRODUCTS,cats=CATS)
html=open("template.html").read()
rep={"__ASOF__":"November 18, 2026","__START__":"March 25, 2026",
 "__TOTAL__":"$"+f"{total:,.0f}","__TX__":"thousands of","__MONTHS__":"7",
 "__COMM__":"$"+f"{c1+c2:,.2f}","__PAID__":"$"+f"{c1:,.2f}","__DUE__":"$"+f"{c2:,.2f}","__INVK__":f"${invT:,.0f}","__INVNOTE__":"Machine figures are from the supplier invoices. Time and driving are what the same work would cost a business that hired someone to do it. Restocking after the first load is paid from sales, so it is not counted twice.","__F3__":f"<b>Buenavyda has put in about ${invT:,.0f}</b> in equipment, stock, time and driving. Metamorphosis has put in $0 and has earned ${c1+c2:,.2f}: 10% of every sale with 0% of the cost or the risk.","__VIDCAP__":"A walk-through of the proposed essentials corner at Metamorphosis Delhi.","__VISITS__":f"≈{nv}","__HOURS__":f"≈{hrs:,.0f}",
 "__MONTHNOTE__":"*March counts from installation on March 25. Card and cash split shown from July. Source: Nayax; March–June from Buenavyda's monthly records.",
 "__F1__":f"<b>${total:,.0f} sold in just over seven months</b>, with the best month in May (${max(full):,.0f}). Most customers pay cash, so the machine accepts both and we collect and count the cash on every visit.",
 "__F2__":"<b>Most purchases happen in the evening, between 8 and 11 pm</b>, with a smaller peak around lunch. We keep the machine full before evenings and weekends.","__HEATNOTE__":"Sample: November 13 to 17, 2026 (43 purchases). Times are Toronto time.","__PERIOD__":"October 11 to November 17: 319 units",
 "__WEEKS__":"5","__WORKNOTE__":f"Estimated from our visit records: twice a week from March to June, about weekly since July. Each visit counts {HPV:g} hours of Buenavyda time.",
 "__DATA__":json.dumps(D)}
for k,v in rep.items(): html=html.replace(k,v)
import re
if not D['products']:
    html=re.sub(r'<section id="when".*?</section>\s*<section id="what".*?</section>','',html,flags=re.S)
    html=html.replace('<a href="#when">When people buy</a><a href="#what">What they buy</a>','')
html=html.replace('<button data-v="cnt">Purchases</button>','')
html=html.replace('thousands of purchases · 7 full months','March 25 to October 31 · 7 full months')
html=html.replace('<div class="panel"><div id="cHeat" class="chart tall"></div><p class="note">Darker = more purchases. Times are Toronto time.</p></div>','<div class="panel"><p class="note" style="padding:30px 10px">Pending: the day-and-hour chart is being built from the machine\'s transaction records.</p><div id="cHeat"></div></div>')

cnt=[0]
def rn(m):
    cnt[0]+=1; return f'<p class="sec-tag">{cnt[0]:02d} ·'
html=re.sub(r'<p class="sec-tag">\d\d ·',rn,html)
open("index.html","w").write(html)
print(total,c1,c2,c1+c2,avg)
