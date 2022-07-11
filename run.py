import subprocess
cmdpipe = subprocess.Popen(
    "kubectl get pods -n kube-system | grep CrashLoopBackOff",
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    shell=True)
result = {}
for row in cmdpipe.stdout.readline():
    if 'CrashLoopBackOff' in row:
        print(row)
        print("restart")

# You need to close the file handles, as they will stay open "forever" otherwise.
cmdpipe.stdout.close()
cmdpipe.stderr.close()
