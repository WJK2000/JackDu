
import sqlite3, pathlib, datetime, json
DB = pathlib.Path('logs/state.db')
def init():
    con = sqlite3.connect(DB)
    con.execute("""create table if not exists state(
        name text primary key,
        cash real,
        pos_qty real,
        pnl real,
        updated text)""")
    con.commit(); con.close()
def save(agent):
    con = sqlite3.connect(DB)
    con.execute("""insert into state(name,cash,pos_qty,pnl,updated)
    values(?,?,?,?,?) on conflict(name) do update set
    cash=excluded.cash,pos_qty=excluded.pos_qty,pnl=excluded.pnl,updated=excluded.updated""",
    (agent.name, agent.cash, agent.pos_qty, agent.pnl, datetime.datetime.utcnow().isoformat()))
    con.commit(); con.close()
def load():
    con = sqlite3.connect(DB)
    cur=con.execute("select name,cash,pos_qty,pnl from state")
    rows={n:(c,q,p) for n,c,q,p in cur.fetchall()}
    con.close(); return rows
