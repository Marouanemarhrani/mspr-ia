// config-overrides.js
module.exports = function override(config, env) {
    if (env === 'development') {
      config.devServer = {
        ...config.devServer,
        setupMiddlewares: (middlewares, devServer) => {
          if (!devServer) {
            throw new Error('webpack-dev-server is not defined');
          }
          // Configure your middlewares here if needed
          return middlewares;
        },
      };
    }
    return config;
  };