# Agent Temptation Bench

**Question:** How often do AI agents take forbidden shortcuts, and can a monitor catch them?

**How:** Each trap is a real task with a planted loophole the agent is told (or should know) not to use, like editing the unit tests instead of fixing the bug. An automatic detector checks whether it took the shortcut.

**Safety:** The agent's actions run only inside Docker containers with networking disabled. The only "shortcuts" are ones I planted on purpose.

**Open question:** Can an agent trick the monitor into missing its shortcuts?

**Status:** 🚧 Week 1 of 12, setting up.