#!/usr/bin/env python3

import psutil
import os
import sys
import shutil


def checkCPU():
    total_cpu = psutil.cpu_count()
    per_cpu_util = ", ".join([str(i)+'%' for i in psutil.cpu_percent(interval=2,percpu=True)])
    return f"System Total CPU: {total_cpu}. Cpu's utilization percentage {per_cpu_util}"

def checkMem():
    system_memory = psutil.virtual_memory()
    return f"System Total Memory: {system_memory.total}Bytes, Available Memory:{system_memory.available}, Percent Used: {system_memory.percent}%."

def checkNet():
    ref = psutil.net_io_counters()
    return f"Network Info: {ref}"


def main():
    print(f'''
"""""""""""""""""""""""""""""""
""
""
""    {checkCPU()}
"""""""""""""""""""""""""""""""
""    {checkMem()}
"""""""""""""""""""""""""""""""
""    {checkNet()}
""
""
"""""""""""""""""""""""""""""""
    ''')

    print("Every thing Look Good!")


if __name__ == '__main__':

    main()
