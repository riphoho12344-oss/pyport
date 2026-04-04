# pyport
A lightweight security tool that combines high-concurrency scanning using Python sockets with deep service identification via Nmap.

**Key Features**
1. **High-Speed Scanning**
   - Utilizes a multi-threaded architecture (one port per thread) for rapid reconnaissance of network assets.
   - Significantly faster than single-threaded scans via concurrent port probing.

2. **Smart Integration**
   - Feeds open ports to Nmap (-sV) for detailed service version detection.
   - Combines socket probing efficiency with Nmap's fingerprinting accuracy.

3. **Customizable**
   - User-defined IP targets and port ranges (e.g., specific networks or services).
   - Flexible for broad sweeps or targeted assessments.

**Disclaimer**
This tool is for EDUCATIONAL/RESEARCH/AUTHORIZED TESTING ONLY.
- NEVER scan public or third-party networks without explicit permission.
- Ensure legality and ethical compliance (e.g., within your own infrastructure).
- High-speed scanning can impact networks; use responsibly to avoid disruption.

**Note**
Always prioritize security best practices and local regulations during assessments.

---
