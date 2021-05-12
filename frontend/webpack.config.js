// Replace src path
module.exports = {
    resolve: {
        alias: {
            "@": require("path").resolve(__dirname, "./src")
        }
    }
};