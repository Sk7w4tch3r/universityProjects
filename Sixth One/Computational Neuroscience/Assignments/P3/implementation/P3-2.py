from brian2 import *
import random

inp_N   = 10
out_N   = 2

v_rest                     = -70 * mV
v_reset                    = [-65 * mV, -64*mV]
firing_threshold           = [-50 * mV, -48*mV]
membrane_time_scale        = 8.  * ms

taupre = taupost = 80*ms
Apre = 0.01
Apost = -Apre*taupre/taupost*1.01


eqs = """
    dv/dt = (-(v-v_rest))/ membrane_time_scale : volt
    firing_threshold : volt
    v_reset : volt
    """

# for generating random sequence of given/random spike trains
def get_spike_soup(pattern1_i, pattern1_t, pattern2_i, pattern2_t):
    indices     = []
    times       = []
    tmp_ind     = []
    tmp_tim     = []
    pattern1 = []
    pattern2 = []
    last_time   = 0*ms
    jump        = 0.3
    p2, p1 = 0,0
    evo = 500
    for i in range(evo):
        # randomizes the sequence
        tmp = rand()

        if tmp >= 0 and tmp < jump:
            tmp_ind = pattern1_i
            tmp_tim = pattern1_t
            pattern1.append(tmp_tim[0]+last_time)
            p1 += 1
        elif tmp >= jump and tmp < 2*jump:
            tmp_ind = pattern2_i
            tmp_tim = pattern2_t
            pattern2.append(tmp_tim[0]+last_time)
            p2+=1
        else:
            ran_len = random.randint(1,9)
            tmp_ind = random.sample(range(10), ran_len)
            tmp_tim = random.sample(range(10), ran_len)*ms
        
        tmp_tim = [i+last_time for i in tmp_tim]
        last_time = round(max(tmp_tim)/ms+1)*ms
        indices.extend(tmp_ind)
        times.extend(tmp_tim)

    indices.extend(pattern2_i)
    tmp_tim = [last_time+i+550*ms for i in pattern2_t]
    times.extend(tmp_tim)
    pattern2.append(tmp_tim[0])

    indices.extend(pattern1_i)
    tmp_tim = [last_time+i+600*ms for i in pattern1_t]
    times.extend(tmp_tim)
    pattern1.append(tmp_tim[0])

    indices.extend(pattern2_i)
    tmp_tim = [last_time+i+650*ms for i in pattern2_t]
    times.extend(tmp_tim)
    pattern2.append(tmp_tim[0])

    indices.extend(pattern1_i)
    tmp_tim = [last_time+i+700*ms for i in pattern1_t]
    times.extend(tmp_tim)
    pattern1.append(tmp_tim[0])

    print(f'''soup is ready!
pattern1:{p1} | {p1/evo},
pattern2:{p2} | {p2/evo},
noise   :{evo-p1-p2} | {(evo-p1-p2)/evo},
simulation time: {times[-1]} s''')  

    return indices, times, pattern1, pattern2


pattern1_indices = array([0,2,4,6,8])
pattern2_indices = array([0,1,2,3,4])
pattern1_times = array([0,1,2,3,4])*ms
pattern2_times = array([0,2,4,6,8])*ms

indices, times, pattern1, pattern2 = get_spike_soup(pattern1_indices, pattern1_times, pattern2_indices, pattern2_times)

input_layer     = SpikeGeneratorGroup(inp_N, indices, times)
output_layer    = NeuronGroup(out_N,  eqs, threshold='v>=firing_threshold', reset='v=v_reset', method='linear')
output_layer.firing_threshold = firing_threshold
output_layer.v_reset = v_reset

syn = Synapses(input_layer, output_layer, '''
            w : 1
            dapre/dt  = -apre /taupre  : 1 (event-driven)
            dapost/dt = -apost/taupost : 1 (event-driven)
            ''',
            on_pre='''
            v_post += 5*w*mV
            apre += Apre
            w = w+apost
            ''',
            on_post='''             
            apost += Apost
            w = w+apre
            ''')
syn.connect(p=1)
syn.w = [rand() for i in range(20)]

synapse_mon     = StateMonitor(syn, ['w', 'apost', 'apre', 'v_post'] , record=True)
out_mon         = StateMonitor(output_layer, 'v', record=True)
out_spike_mon   = SpikeMonitor(output_layer)
in_spike_mon    = SpikeMonitor(input_layer)

run(times[-1])

plot(synapse_mon.t, synapse_mon.apost[0].T, label='apost')
plot(synapse_mon.t, synapse_mon.apre[0].T, label='apre')
legend()
show()
# quit()


fig, axs = plt.subplots(2, 3)
axs[0, 0].plot(out_mon.t, out_mon.v[0].T, label='neuron 1')
axs[0, 0].set_title("output layer potential")
axs[0, 0].legend()
axs[1, 0].plot(out_mon.t, out_mon.v[1].T, label='neuron 2')
axs[1, 0].set_title("output layer potential")
axs[1, 0].legend()
for i in range(10):
    axs[0, 1].plot(synapse_mon.t, synapse_mon.w[i].T, label='neuron 1')
axs[0, 1].set_title("synaptic weights / neuron 1")
for i in range(10,20):
    axs[1, 1].plot(synapse_mon.t, synapse_mon.w[i].T, label='neuron 1')
axs[1, 1].set_title("synaptic weights / neuron 2")
axs[0, 2].plot(out_spike_mon.t, out_spike_mon.i, '.k')
axs[0, 2].set_title("output layer spikes")
axs[1, 2].plot(in_spike_mon.t, in_spike_mon.i, '.k')
axs[1, 2].set_title("input layer spikes")
# fig.tight_layout()


for j in [0,1]:
    for k in [0,1,2]:
        for i in range(len(pattern1)-50, len(pattern1)):
            axs[j,k].axvspan(pattern1[i], pattern1[i]+5*ms,alpha=0.1, color='red')
        for i in range(len(pattern2)-50, len(pattern2)):
            axs[j,k].axvspan(pattern2[i], pattern2[i]+9*ms, alpha=0.1, color='blue')

show()
quit()