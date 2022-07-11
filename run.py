import subprocess

output = subprocess.check_output(
    "kubectl get pods -n kube-system | grep CrashLoopBackOff"
).decode()
result = {}
for row in output.splitlines():
    # if 'CrashLoopBackOff' in row:
    #     print(row)
    #     print("restart")
    print(row)

