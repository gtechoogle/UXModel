import subprocess
import json

def catch_launch_trace(traceName):
    with open ('trace_config.json', 'r', encoding='utf-8') as file:
        raw = json.load(file)
    launch_trace_cmd = raw['app_launch']
    cmd_time = launch_trace_cmd['-t']
    cmd_buffer = launch_trace_cmd['-b']
    cmd_tag = launch_trace_cmd['tag']

    trace_cmd = [
        "python", "bin/record_android_trace",
        "-o", traceName,
        "-t", cmd_buffer,
        "-n",
        cmd_tag
    ]
    process = subprocess.Popen(trace_cmd)
    return process