# Agent Temptation Bench

**Question:** How often do AI agents take forbidden shortcuts, and can a monitor catch them?

**How:** Each trap is a real task with a planted loophole the agent is told (or should know) not to use, like editing the unit tests instead of fixing the bug. An automatic detector checks whether it took the shortcut.

**Safety:** The agent's actions run only inside Docker containers with networking disabled. The only "shortcuts" are ones I planted on purpose.

**Open question:** Can an agent trick the monitor into missing its shortcuts?

## Planned trap types 
**Gaming the grader** (first trap): Does the agent edit the tests instead of fixing the bug?
**Disabling oversight**: Does the agent delete or change the log file the monitor reads?
**Acting differently when watched**: Does the agent cheat less when it's told it's being tested?
**Lying about it**: When asked "did you take any shortcuts?", does the agent tell the truth?
**Reading the answer key**: Does the agent open a solutions file it was told not to touch?