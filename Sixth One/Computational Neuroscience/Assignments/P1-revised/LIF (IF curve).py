from brian2 import *
from neurodynex.tools import input_factory, plot_tools
import matplotlib.pyplot as plt

v_rest = -70 * mV
v_reset = -65 * mV
firing_threshold = -50 * mV
membrane_resistance = 10. * Mohm
membrane_time_scale = 8. * ms
abs_refractory_period   = 2.0 * ms
simulation_time=500 * ms

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
dv/dt =
( -(v-v_rest) + membrane_resistance * input_current(t,i) ) / membrane_time_scale : volt (unless refractory)"""

# using 100 neurons for computing spike numbers of different input currents
neuron = NeuronGroup(
    100, model=eqs, reset="v=v_reset", threshold="v>firing_threshold",
    refractory=abs_refractory_period, method="linear")
neuron.v = v_rest  

state_monitor = StateMonitor(neuron, ["v"], record=True)
spike_monitor = SpikeMonitor(neuron)
run(simulation_time)


# plotting I-F curve
plot(linspace(amplitude, amplitude+0.5, 100), spike_monitor.count / simulation_time)
show()

