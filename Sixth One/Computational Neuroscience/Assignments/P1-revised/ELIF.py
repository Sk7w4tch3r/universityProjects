from brian2 import *
from neurodynex.tools import input_factory, plot_tools
import random

defaultclock.dt = 0.05 * ms
tau = 12.0 * ms
R = 20.0 * Mohm
v_rest = -65.0 * mV
v_reset = -60.0 * mV
v_rheobase = -55.0 * mV
delta_T = 2.0 * mV
v_spike = -30. * mV
simulation_time=180 * ms

# constant input current
# input_current = input_factory.get_step_current(t_start=20, t_end=120, unit_time=ms, amplitude=0.8 * namp)

# sinosoidal (non-constant) input current
# input_current = input_factory.get_sinusoidal_current(
#     500, 1500, unit_time=0.1 * ms,
#     amplitude=2.5 * namp, frequency=150 * Hz, direct_current=2. * namp)

# random input current
# amplitude = 0.8
# t_end = int(simulation_time/ms)
# t_start = 20
# tmp_size = 1 + t_end 
# tmp = np.zeros((tmp_size, 1)) * amp
# for j in range(t_start, t_end):
#     tmp[j, 0] = (amplitude + random.uniform(0.5, 2))*namp
# input_current = TimedArray(tmp, dt=1. * ms) 


eqs = """
dv/dt = (-(v-v_rest) +delta_T*exp((v-v_rheobase)/delta_T)+ R * input_current(t,i))/(tau) : volt
"""
neuron = NeuronGroup(1, model=eqs, reset="v=v_reset", threshold="v>v_spike", method="euler")
neuron.v = v_rest
state_monitor = StateMonitor(neuron, ["v"], record=True)
spike_monitor = SpikeMonitor(neuron)

net = Network(neuron, state_monitor, spike_monitor)
net.run(simulation_time)

plot_tools.plot_voltage_and_current_traces(
    state_monitor, input_current, title="step current", firing_threshold=v_spike)
print("nr of spikes: {}".format(spike_monitor.count[0]))
show()