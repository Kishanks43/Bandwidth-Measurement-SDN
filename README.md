# Bandwidth Measurement and Analysis using SDN (Mininet + POX)

## 📌 Problem Statement

Measure and compare bandwidth across different network configurations using Mininet and POX controller.

---

## ⚙️ Tools Used

* Mininet
* POX Controller
* iperf
* Ubuntu (VM)

---

## 🧱 Topologies Implemented

### 1. CustomTopo1 (Bottleneck Topology)

* 2 switches
* 4 hosts
* Bottleneck link (10 Mbps)

### 2. CustomTopo2 (Tree-like Topology)

* 3 switches
* 4 hosts
* Delay added between switches

---

## 🚀 How to Run

### Step 1: Start POX Controller

```bash
cd pox
./pox.py forwarding.l2_learning
```

### Step 2: Run Mininet

```bash
sudo mn --custom custom_topo.py --topo customtopo1 --controller=remote --link tc
```

---

## 🧪 Testing

### Connectivity Test

```bash
pingall
```

### Bandwidth Test

```bash
h1 iperf -s &
h2 iperf -c h1
```

---

## 📊 Results

| Topology                 | Bandwidth   | Observation           |
| ------------------------ | ----------- | --------------------- |
| Same Switch              | ~90 Mbps    | Direct communication  |
| Across Switch (No Limit) | ~60-70 Mbps | Delay impact          |
| Bottleneck Link          | ~10 Mbps    | Bandwidth constrained |

---

## 🔍 Analysis

* Bandwidth is highest when hosts are on the same switch.
* Multi-hop communication introduces delay and reduces throughput.
* Artificial bandwidth constraints (TCLink) effectively limit performance.

---

## 📸 Proof of Execution

Screenshots included:

* pingall output
* iperf results

---

## 🎯 Conclusion

This project demonstrates how network topology and link constraints affect bandwidth and overall network performance in an SDN environment.

---

## 📚 References

* Mininet Documentation
* POX Controller Documentation
