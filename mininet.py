from mininet.topo import Topo
from mininet.log import setLogLevel
from mininet.net import Mininet
from mininet.util import dumpNodeConnections

no_of_hosts = input()
no_of_switches = no_hosts/2 

hosts = []*no_of_hosts
switches = []*no_of_switches


class SingleSwitchTopo(Topo):
	def build(self, n=2):	
	    for h in range(no_hosts):
		ip_mask = (h%2)+1
		ip_add = '10.'+str(ip_mask)+'.0.'+str(h)+'/16'
		host = self.addHost('h'+str(h),ip=ip_add)
		hosts.append(host)                
	    for h in range(no_switches):
		switch= self.addSwitch('s%s' % (h + 1))
		switches.append(switch)
	    print switches
	    print hosts
	    for i in range(0,3):
		self.addLink(switches[i] , switches[i+1])
		self.addLink(switches[i] , hosts[(2*i)])
		self.addLink(switches[i] , hosts[(2*i)+1])
	    self.addLink(switches[3] , switches[0])
	

def simpleTest():
        topo = SingleSwitchTopo(n=4)
        net = Mininet(topo)
        net.start()
        print "Dumping host connections"
        dumpNodeConnections(net.hosts)
        print "Testing network connectivity"
        net.pingAll()
        net.stop()

if __name__ == '__main__':
        setLogLevel('info')
        simpleTest()

