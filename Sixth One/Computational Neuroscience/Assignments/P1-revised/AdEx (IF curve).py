from brian2 import *
from neurodynex.tools import input_factory, plot_tools

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

# generating input for 100 neurons ranging input current between (0.01, 0.51)namp 
amplitude = 0.01
t_end = 120
t_start = 20
tmp_size = 1 + t_end
tmp = np.zeros((tmp_size, 100)) * amp
for j in range(100):
    tmp[t_start: t_end + 1, j] = (amplitude + j*0.005)*namp
input_current = TimedArray(tmp, dt=1. * ms)

v_spike_str = "v>{:f}*mvolt".format(v_spike / mvolt)

eqs = """
    dv/dt = (-(v-v_rest) +delta_T*exp((v-v_rheobase)/delta_T)+ R * input_current(t,i) - R * w)/(tau_m) : volt
    dw/dt=(a*(v-v_rest)-w)/tau_w : amp
    """

neuron = NeuronGroup(100, model=eqs, threshold=v_spike_str, reset="v=v_reset;w+=b", method="euler")
neuron.v = v_rest
neuron.w = 0.0 * pA

state_monitor = StateMonitor(neuron, ["v", "w"], record=True)
spike_monitor = SpikeMonitor(neuron)
run(simulation_time)

# plotting I-F curve
plot(linspace(amplitude, amplitude+0.5, 100), spike_monitor.count / simulation_time)
show()