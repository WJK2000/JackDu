
import asyncio, json, pathlib
from agents.breakout import BreakoutAgent
from core.dashboard import Dash
from core.db import init, load
cfg=json.loads(pathlib.Path('config/settings.json').read_text())
async def main():
    init(); agent=BreakoutAgent(cfg)
    saved=load(); 
    if agent.name in saved:
        agent.cash,agent.pos_qty,agent.pnl=saved[agent.name]
    dash=Dash(agent)
    await asyncio.gather(agent.run(), dash.run())
if __name__=='__main__':
    asyncio.run(main())
