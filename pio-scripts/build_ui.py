Import('env')

env.Execute("npm install")
env.Execute("npm run build")