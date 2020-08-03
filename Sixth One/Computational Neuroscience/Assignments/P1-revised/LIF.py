from brian2 import *
from neurodynex.tools import input_factory, plot_tools
import matplotlib.pyplot as plt
import random

v_rest = -70 * mV
v_reset = -65 * mV
firing_threshold = -50 * mV
membrane_resistance = 10. * Mohm
membrane_time_scale = 8. * ms
abs_refractory_period   = 2.0 * ms
simulation_time=300 * ms

# constant input current
# input_current = input_factory.get_step_current(
#     t_start=100, t_end=200, unit_time=ms,
#     amplitude=2.5 * namp)

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
dv/dt =
( -(v-v_rest) + membrane_resistance * input_current(t,i) ) / membrane_time_scale : volt (unless refractory)"""

neuron = NeuronGroup(
    1, model=eqs, reset="v=v_reset", threshold="v>firing_threshold",
    refractory=abs_refractory_period, method="linear")
neuron.v = v_rest  

state_monitor = StateMonitor(neuron, ["v"], record=True)
spike_monitor = SpikeMonitor(neuron)
run(simulation_time)

# plotting membrane potential and input current
plot_tools.plot_voltage_and_current_traces(state_monitor, input_current)
print("nr of spikes: {}".format(len(spike_monitor.t)))
show()
