# Drill 3 

# Processes & Ports 

- **what is Processes ?**
  - A process is a **running instance** of a program on your system.

  - Every time you run a command, program, or service, the OS creates a process for it.

  - Each process has:

    - **PID (Process ID)** → a unique number identifying the process.

    - **State** → running, sleeping, stopped, etc.

    - **Owner/User** → which user started it.
  - **Eg :** 
  
    | Command | Description |
    |---------|-------------|
    | `ps aux` | Shows all running processes with details: PID, user, CPU/memory usage, command. |
    | `top` | Shows an interactive view of running processes and system resources. |
    | `htop` | Like `top` but more visual and interactive (needs to be installed). |


- **What is Port ?**
  - A port is like a “door” your computer uses to communicate with other computers or programs.

  - Ports allow multiple networked services to run simultaneously without interfering.

  - Each process that communicates over a network usually listens on a specific port.
- **common Ports**

    | Port | Service    |
    | ---- | ---------- |
    | 80   | HTTP       |
    | 443  | HTTPS      |
    | 22   | SSH        |
    | 3306 | MySQL      |
    | 5432 | PostgreSQL |


- **Why Ports and Processes are Useful in CLI**
  - Sometimes you need to check which program is using a port (e.g., port 80 for web server).

  - Sometimes you need to stop or kill a process that is blocking a port.


- **Some of the Important Processes and ports CLI Commands**

    | Importance | Command | What it Does | Example |
    |------------|---------|--------------|---------|
    |  1 | `ps aux` | Shows all running processes with details: PID, user, CPU/memory usage, command | `ps aux` |
    |  2 | `top` | Interactive view of running processes and system resources | `top` |
    |  3 | `htop` | More visual and interactive version of `top` (needs installation) | `htop` |
    |  4 | `kill <PID>` | Stops a running process by PID | `kill 1234` |
    |  5 | `kill -9 <PID>` | Forcefully stops a running process | `kill -9 1234` |
    |  6 | `sudo lsof -i :<port>` | Shows which process is using a specific network port | `sudo lsof -i :8080` |
    |  7 | `netstat -tulnp` | Displays all listening ports and the processes using them | `netstat -tulnp` |
    |  8 | `ss -tulnp` | Modern replacement for netstat; shows listening ports and processes | `ss -tulnp` |
    |  9 | `pkill <process_name>` | Stops all processes with the given name | `pkill nginx` |
    |  10 | `jobs` | Shows background jobs started in the current shell | `jobs` |


- **Excercise**

  1. **List your browser's process IDs (PID) and parent process IDs (PPID)**

     - Step 1: Use `ps` to list processes
       ```bash
       ps -ef | grep <browser_name>
       # Example: ps -ef | grep firefox
       ```

  2. **Stop the browser application from the command line**

     - Step 1: Kill the process by PID
       ```bash
       kill <PID>
       # Or force kill: kill -9 <PID>
       ```

  3. **List the top 3 processes by CPU usage**

     - Step 1: Use `ps` and sort by CPU
       ```bash
       ps aux --sort=-%cpu | head -n 4
       # head -n 4 because first line is the header
       ```

  4. **List the top 3 processes by memory usage**

     - Step 1: Use `ps` and sort by memory
       ```bash
       ps aux --sort=-%mem | head -n 4
       ```

  5. **Start a Python HTTP server on port 8000**

     - Step 1: Start the server
       ```bash
       python3 -m http.server 8000
       ```

  6. **Open another tab and stop the Python HTTP server you started**

     - Step 1: Find the PID of the server
       ```bash
       ps aux | grep "http.server"
       ```
     - Step 2: Kill the server process
       ```bash
       kill <PID>
       ```

  7. **Start a Python HTTP server on port 90**

     - Step 1: Start the server
       ```bash
       sudo python3 -m http.server 90
       ```

  8. **Display all active connections and the corresponding TCP/UDP ports**

     - Step 1: Use `netstat` or `ss`
       ```bash
       sudo netstat -tulnp
       # or
       sudo ss -tulnp
       ```

  9. **Find the PID of the process that is listening on port 5432**

     - Step 1: Use `lsof` or `ss`
       ```bash
       sudo lsof -i :5432
       # or
       sudo ss -tulnp | grep 5432
       ```

  10. **List all processes in a tree structure to see parent-child relationships**

      - Step 1: Use `pstree`
        ```bash
        pstree -p
        ```


# Misc

## **Exercise**

1. **What's your local IP address?**

   - Step 1: Use `ip` or `ifconfig` to check IP
     ```bash
     ip addr show
     # or
     ifconfig
     ```
   - Step 2: Look for your network interface (e.g., `eth0`, `wlan0`)  
     - `inet` → shows your local IP address

---

2. **Find the IP address of google.com**

   - Step 1: Use `ping` or `nslookup` or `dig`
     ```bash
     ping -c 1 google.com
     ```
     - Output shows the IP in square brackets
     ```bash
     nslookup google.com
     ```
     ```bash
     dig +short google.com
     ```

---

3. **How to check if Internet is working using CLI?**

   - Step 1: Ping a reliable server
     ```bash
     ping -c 4 8.8.8.8
     ```
     - Successful replies → Internet is working
   - Step 2: Ping a domain name
     ```bash
     ping -c 4 google.com
     ```
     - If DNS resolves and replies come → Internet is working fully

---

4. **Where is the `node` command located? What about `code`?**

   - Step 1: Use `which` or `command -v`
     ```bash
     which node
     # Example output: /usr/bin/node
     ```
     ```bash
     which code
     # Example output: /usr/bin/code
     ```
   - Step 2: Verify version to confirm
     ```bash
     node -v
     code --version
     ```


