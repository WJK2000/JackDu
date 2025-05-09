
import asyncio, random
from ingest.feed import price
from core.logger import logger
from core.db import save
class BreakoutAgent:
    def __init__(self, cfg):
        self.cfg=cfg; self.name='Breakout'
        self.cash=cfg['total_capital']; self.pos_qty=0.0; self.pnl=0.0
    async def run(self):
        while True:
            await asyncio.sleep(10)
            p=price(self.cfg['symbol'])
            if p is None: continue
            if random.random()<0.5 and self.cash>5000:
                amt=self.cash*0.1; qty=amt/p; self.cash-=amt; self.pos_qty+=qty
                logger.info(f'BUY {qty:.6f} @ {p}')
            elif self.pos_qty>0:
                proceeds=self.pos_qty*p; self.cash+=proceeds; self.pos_qty=0
                logger.info(f'SELL all @ {p}')
            self.pnl=self.cash+self.pos_qty*p-self.cfg['total_capital']
            save(self)
