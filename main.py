from time import sleep

from rich.console import Console
from rich.layout import Layout
from rich.live import Live
from rich.panel import Panel
from rich.table import Table

console = Console()

def make_layout():
    """ Define the layout of the application""" 
    layout = Layout(name="root")

    layout.split(
        Layout(name="main", ratio=7),
        Layout(name="footer", ratio=1)
    )

    layout["main"].split_row(
        Layout(name="side"),
        Layout(name="body", ratio=3, minimum_size=60)
    )

    return layout

class MetricPanel:
    """Display accuracy in metrics"""
    _metrics = {}

    def __rich__(self) -> Panel:
        grid = Table.grid(expand=True)
        grid.add_column(justify="left")
        grid.add_column(justify="right", ratio=3)
        for key, val in self._metrics.items():
            grid.add_row(
                f"[b]{key}[b]", str(val)
            )
        return Panel(grid, title="Metrics")

    def log_metrics(self, metrics: dict):
        for k, v in metrics.items():
            self._metrics[k] = v

    


if __name__ == "__main__":
    import random


    layout = make_layout()

    ct = 0

    mp = MetricPanel()

    metrics = {
        "count": ct,
        "train_accuracy": random.randint(0, 100),
        "val_accuracy": random.randint(0, 100),
    }

    mp.log_metrics(metrics)

    layout["side"].update(mp)

    with Live(layout, refresh_per_second=10, screen=True):
        while True:
            ct += 1
            sleep(.5)

            metrics = {
                "count": ct,
                "train_accuracy": random.randint(0, 100),
                "val_accuracy": random.randint(0, 100),
            }
            
            mp.log_metrics(metrics=metrics)

            layout["side"].update(mp)