from brian2 import *
from neurodynex.tools import input_factory, plot_tools


N = 100
tau = 10*ms
v0_max = 3.
duration = 1000*ms
sigma = 0.2

eqs = '''
dv/dt = (v0-v)/tau+sigma*xi*tau**-0.5 : 1 (unless refractory)
v0 : 1
'''

G = NeuronGroup(N, eqs, threshold='v>1', reset='v=0', refractory=5*ms, method='euler')
G1 = G[:80]
G1.v0 = 'i*v0_max/(80-1)'
G2 = G[80:]
G2.v0 = 'i*v0_max/(20-1)'

spike_monitor = SpikeMonitor(G)
state_monitor = StateMonitor(G, ['v'], record=True)

G.v0 = 'i*v0_max/(N-1)'

stimulus = TimedArray(np.hstack([[c, c, c, 0, 0] for c in np.random.rand(1000)]), dt=10*ms)

net = NeuronGroup(10, 'dv/dt = (-v + stimulus(t))/(10*ms) : 1',
                threshold='v>0.4', reset='v=0')
net.v = '0.5*rand()' 
mon = StateMonitor(net, ['v'], record=True)
mon = SpikeMonitor(net)
run(duration)
plot(mon.t, mon.i, '.k')

show()
quit()


n = 1000
duration = 1*second
tau = 10*ms
eqs = '''
dv/dt = (v0 - v) / tau : volt (unless refractory)
v0 : volt
'''
group = NeuronGroup(n, eqs, threshold='v > 10*mV', reset='v = 0*mV',
                    refractory=5*ms, method='exact')
group1 = group[:800]
group2 = group[800:]
group1.v = 0*mV
group2.v = 2*mV
group.v0 = '20*mV * i / (n-1)'

monitor = SpikeMonitor(group)

run(duration)
plot(monitor.t, monitor.i, '.k')
xlabel('v0 (mV)')
ylabel('Firing rate (sp/s)')

# figure(figsize=(12,4))
# subplot(121)
# plot(spike_monitor.t/ms, spike_monitor.i, '.k')
# xlabel('Time (ms)')
# ylabel('Neuron index')
# subplot(122)
# plot(state_monitor.t/ms, state_monitor.v.T)
# xlabel('v0')
# ylabel('Firing rate (sp/s)')
show()