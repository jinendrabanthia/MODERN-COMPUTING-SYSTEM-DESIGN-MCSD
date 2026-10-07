1. Parallel in Parallel out register(PIPO)
this is a synchronous circuit in which data bits provided on inputs D0-D3
are loaded into the flip flops on rising edge of clock signal.

the data bits appear immediately at the Q0-Q3 outputs and retain their state untill new data values are loaded on a subsequent rising clock edge.

RING COUNTER
the ring counter has 4 positions the circuit contains 4 ring counter states
the counter is initialized by setting the RST input high and then low this sets the q output of the first flip flop to 1 and the remaining q outputs to 0.
the CLK input is connected to a clock source 