import sys
import subprocess

tag = sys.argv[1]


def exec(command, soft=False):
    print("> {}".format(command))
    try:
        return subprocess.check_call(command, shell=True)
    except Exception as e:
        if not soft:
            raise e


name = "bullet-master-server"
path = "/root/bullet-master-server"
# path = "/Users/vkrasnoperov/Code/bullet-master-server"

print("Deploying tag {}".format(tag))

exec("docker pull neronmoon/bullet-master-server:{}".format(tag))
exec("docker kill {}".format(name), soft=True)
exec("docker rm {}".format(name), soft=True)
exec("docker run -d --restart always --name {name} "
     "-v {path}/cert:/srv/app/cert "
     "--env-file {path}/.env -p 9999:9999 neronmoon/bullet-master-server:{tag}".format(name=name, tag=tag, path=path))
