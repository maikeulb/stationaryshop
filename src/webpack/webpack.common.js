const webpack = require("webpack");
const merge = require('webpack-merge');
const parts = require('./webpack.parts');
const path = require('path');

module.exports = merge([
  {
    entry: {
      app: path.resolve(parts.PATHS.assets, 'js', 'script.js'),
    },
    output: {
      path: parts.PATHS.output,
      publicPath: parts.PATHS.public,
      filename: 'js/[name].bundle.js',
    },
    plugins: [
      new webpack.NamedModulesPlugin(),
      new webpack.HotModuleReplacementPlugin(),
      new webpack.ProvidePlugin({
        $: "jquery",
        jQuery: "jquery",
        "window.jQuery": "jquery",
        "window.toastr": "toastr"
      })
    ],
  },
  parts.extractCSS({
    use: ['css-loader', 'sass-loader', parts.autoprefix()],
  }),
  parts.copyWebpackPlugin(),
  parts.loadFonts({
    options: {
      // name: "[name].[hash:8].[ext]",
      name: "[name].[ext]",
      outputPath: "css/",
      publicPath: "../"
    },
  }),
  parts.loadJavaScript({
    include: path.resolve(parts.PATHS.assets, 'js'),
    exclude: /node_modules/,
  }),
]);
