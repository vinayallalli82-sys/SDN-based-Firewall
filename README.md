# SDN Firewall using POX Controller

## 📌 Problem Statement

The objective of this project is to implement a Software Defined Networking (SDN) based firewall using a POX controller. The firewall should control network traffic by allowing or blocking packets based on predefined rules.

---

## 🛠️ Tools Used

* Mininet (for network simulation)
* POX Controller (for control logic)
* OpenFlow Protocol

---

## 🌐 Topology

A simple topology is used:

* 1 Switch (s1)
* 3 Hosts (h1, h2, h3)

IP Addresses:

* h1 → 10.0.0.1
* h2 → 10.0.0.2
* h3 → 10.0.0.3

---

## ⚙️ How to Run

### Step 1: Start POX Controller

```
cd ~/pox
./pox.py openflow.of_01 misc.firewall
```

### Step 2: Start Mininet

```
sudo mn --topo single,3 --controller remote
```

---

## 🔐 Firewall Rule

* Block traffic from **h1 (10.0.0.1) → h2 (10.0.0.2)**
* Allow all other traffic

---

## 🧠 Working

* The switch sends unknown packets to the controller (PacketIn)
* The controller checks source and destination IP
* If rule matches → packet is dropped
* Else → flow rule is installed in switch
* Future packets are handled directly by the switch

---

## ✅ Results

### ❌ Blocked Traffic

* h1 → h2 is blocked
* Ping fails

### ✅ Allowed Traffic

* h1 → h3 works successfully
* Flow rules are installed

### 📊 Flow Table

* Entries exist only for allowed traffic

### ⚡ Performance

* High throughput observed using iperf

---



## 🎯 Conclusion

The project demonstrates how SDN enables centralized control of network traffic. The firewall dynamically filters packets and improves efficiency by installing flow rules for allowed traffic.

---

## 👨‍💻 Author

A Vinay
