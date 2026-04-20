
from mininet.topo import Topo
from mininet.link import TCLink

class CustomTopo1(Topo):
    def build(self):

        # Add switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')

        # Add hosts
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')

        # Connect hosts to switches (fast links)
        self.addLink(h1, s1, cls=TCLink, bw=100)
        self.addLink(h2, s1, cls=TCLink, bw=100)
        self.addLink(h3, s2, cls=TCLink, bw=100)
        self.addLink(h4, s2, cls=TCLink, bw=100)

        # Bottleneck link between switches
        self.addLink(s1, s2, cls=TCLink, bw=10, delay='20ms')


class CustomTopo2(Topo):
    def build(self):

        # Add switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')

        # Add hosts
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')

        # Connect hosts to switches (fast links)
        self.addLink(h1, s2, cls=TCLink, bw=100)
        self.addLink(h2, s2, cls=TCLink, bw=100)
        self.addLink(h3, s3, cls=TCLink, bw=100)
        self.addLink(h4, s3, cls=TCLink, bw=100)

        # link between switches
        self.addLink(s1, s2, cls=TCLink, delay='20ms')
        self.addLink(s1, s3, cls=TCLink, delay='20ms')



topos = {'customtopo1': (lambda: CustomTopo1()), 'customtopo2': (lambda: CustomTopo2())}
