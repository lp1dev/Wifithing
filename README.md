# WifiThing

It's a Wi-Fi bruteforce script based on nmcli (which seems to be the most time-efficient way to connect to a network from what I've tested).

> Please note, given the fact that you can't parallelize associations operations on a network interface, this will always be (very) much less efficient than offline cracking using a handshake.
You could use multiple network interfaces though, from my calculations it takes ~ 200 seconds to try 100 PSKs on WPA2 on a single card.

---

# Installation

## Requirements

- Python3
- nmcli (now default on debian-based distributions)

## Setup

`pip install wifi`


---

# Usage

`brute.py {interface} {SSID} {dictionary}`

---

> This tool has been written as a PoC to answer the question "But how much more efficient is offline cracking on Wi-Fi networks?" - Answer : So much more, using a GTX 1080 you can crack ~2000kH/s from a WPA2 handshake, compared to the sad 0.5H/s you can expect from an online approach, it's about 4 Million times faster - BTW I'm not responsible for your actions, if you're stupid (and patient) enough to use this to bruteforce networks you're not authorized to audit, you should rethink your life choices.
