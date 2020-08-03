from brian2 import *
from neurodynex.tools import input_factory, plot_tools
import random

defaultclock.dt = 0.01 * ms
tau_m = 5 * ms
R = 500 * Mohm
v_rest = -70.0 * mV
v_reset = -51.0 * mV
v_rheobase = -50.0 * mV
delta_T = 2.0 * mV
a = 0.5 * nS
tau_w = 100.0 * ms
b = 7.0 * pA
simulation_time=300 * ms
v_spike = -30. * mV

# constant input current
# input_current = input_factory.get_step_current(10, 200, 1. * ms, 65.0 * pA)

# sinosoidal (non-constant) input current
# input_current = input_factory.get_sinusoidal_current(
#     500, 1500, unit_time=0.1 * ms,
#     amplitude=2.5 * namp, frequency=150 * Hz, direct_current=2. * namp)

# random input current
# amplitude = 2
# t_end = int(simulation_time/ms)
# t_start = 20
# tmp_size = 1 + t_end 
# tmp = np.zeros((tmp_size, 1)) * amp
# for j in range(t_start, t_end):
#     tmp[j, 0] = (amplitude + random.uniform(0.5, 2))*namp
# input_current = TimedArray(tmp, dt=1. * ms) 

v_spike_str = "v>{:f}*mvolt".format(v_spike / mvolt)

eqs = """
    dv/dt = (-(v-v_rest) +delta_T*exp((v-v_rheobase)/delta_T)+ R * input_current(t,i) - R * w)/(tau_m) : volt
    dw/dt=(a*(v-v_rest)-w)/tau_w : amp
    """

neuron = NeuronGroup(1, model=eqs, threshold=v_spike_str, reset="v=v_reset;w+=b", method="euler")
neuron.v = v_rest
neuron.w = 0.0 * pA

state_monitor = StateMonitor(neuron, ["v", "w"], record=True)
spike_monitor = SpikeMonitor(neuron)
run(simulation_time)

plot_tools.plot_voltage_and_current_traces(state_monitor, input_current)
print("nr of spikes: {}".format(spike_monitor.count[0]))
show()