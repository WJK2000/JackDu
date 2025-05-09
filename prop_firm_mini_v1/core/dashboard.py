
from rich.live import Live
from rich.table import Table
import asyncio
class Dash:
    def __init__(self, agent): self.agent=agent
    def table(self):
        t=Table();t.add_column('Cash');t.add_column('Pos');t.add_column('PnL')
        t.add_row(f'{self.agent.cash:.0f}',f'{self.agent.pos_qty:.6f}',f'{self.agent.pnl:.0f}');return t
    async def run(self):
        with Live(self.table(), refresh_per_second=1) as live:
            while True:
                live.update(self.table()); await asyncio.sleep(1)
