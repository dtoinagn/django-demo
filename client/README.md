Windows configuration for Node and npm
The Node is installed using fnm to %NODE_HOME%, the path is modified to override the system default %ProgramFiles%\nodejs

Run the following command to see where npm will isntall global packages to verify it is correct:
`npm config get prefix -g`
By default, it is set to `<X>:\Users\<user>\AppData\Roaming\npm`. Since we used fnm to install node and npm, the global packages need to be installed to %NODE_HOME%\npm, and you can run the following command to correct it:

```
npm config set prefix %NODE_HOME%\npm -g
```

Run `yarn create vite app` and select `React` and `JavaScript` to create your first React website
