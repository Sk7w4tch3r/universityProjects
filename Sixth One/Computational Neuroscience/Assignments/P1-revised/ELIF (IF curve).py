from brian2 import *
from neurodynex.tools import input_factory, plot_tools

defaultclock.dt = 0.05 * ms
tau = 12.0 * ms
R = 20.0 * Mohm
v_rest = -65.0 * mV
v_reset = -60.0 * mV
v_rheobase = -55.0 * mV
delta_T = 2.0 * mV
v_spike = -30. * mV
simulation_time=300 * ms

# generating input for 100 neurons ranging input current between (2, 2.5)namp 
amplitude = 2
t_end = 120
t_start = 20
tmp_size = 1 + t_end 
tmp = np.zeros((tmp_size, 100)) * amp
for j in range(100):
    tmp[t_start: t_end + 1, j] = (amplitude + j*0.005)*namp
input_current = TimedArray(tmp, dt=1. * ms)

eqs = """
dv/dt = (-(v-v_rest) +delta_T*exp((v-v_rheobase)/delta_T)+ R * input_current(t,i))/(tau) : volt
"""
neuron = NeuronGroup(100, model=eqs, reset="v=v_reset", threshold="v>v_spike", method="euler")
neuron.v = v_rest
state_monitor = StateMonitor(neuron, ["v"], record=True)
spike_monitor = SpikeMonitor(neuron)

net = Network(neuron, state_monitor, spike_monitor)
net.run(simulation_time)

# plotting I-F curve
plot(linspace(amplitude, amplitude+0.5, 100), spike_monitor.count / simulation_time)
show()

