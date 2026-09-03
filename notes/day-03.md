# Day 3 - Processes, Services, Logs and Networking

## What I Learned

A process is a program that is currently running.

A service is normally a long-running program that provides a function and is often managed by the operating system.

I started a Python web server on port 8000 and opened it from my browser.

## Ports

A port allows network traffic to reach a particular application.

My Python server listened on port 8000.

I used `ss -tulpn | grep :8000` to find the program using the port.

## Processes

I used `ps aux | grep '[p]ython'` to find the Python process.

Every process has a Process ID or PID.

## Logs

The Python server produced logs when my browser and curl sent requests.

HTTP status code 200 showed that the requests succeeded.

## DNS

DNS translates domain names into addresses that computers can use.

I tested DNS using `dig example.com +short`.

## Routes

I used `ip route` to view the Linux routing table.

Routes help the system decide where network traffic should be sent.

## Firewall

A firewall can allow or block network traffic based on rules.

A running application can still be unreachable if the firewall blocks its port.

## Troubleshooting

My basic troubleshooting order is:

1. Check whether the process is running.
2. Check whether the expected port is listening.
3. Test the application with curl.
4. Check the logs.
5. Check DNS.
6. Check the route.
7. Check firewall rules.

## Application Path

Browser
↓
DNS
↓
Load Balancer
↓
Application
↓
Database
