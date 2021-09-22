from brian2 import *

taupre = taupost = 20*ms
Apre = 0.01
Apost = -Apre*taupre/taupost*1.05
tmax = 50*ms
N = 40

pre     = NeuronGroup(N, 'tspike:second', threshold='t>tspike', refractory=100*ms)
post    = NeuronGroup(N, 'tspike:second', threshold='t>tspike', refractory=100*ms)
pre.tspike = 'i*tmax/(N-1)'
post.tspike = '(N-1-i)*tmax/(N-1)'

S = Synapses(pre, post,
             '''
             w : 1
             dapre/dt = -apre/taupre : 1 (event-driven)
             dapost/dt = -apost/taupost : 1 (event-driven)
             ''',
             on_pre='''
             apre += Apre
             w = w+apost
             ''',
             on_post='''
             apost += Apost
             w = w+apre
             ''')
S.connect(j='i')

run(tmax+1*ms)

plot((post.tspike-pre.tspike)/ms, S.w, '.k')
xlabel(r'$\Delta t$ (ms)')
ylabel(r'$\Delta w$')
axhline(0, ls='-', c='k')
show()