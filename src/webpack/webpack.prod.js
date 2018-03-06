const webpack = require("webpack");
const merge = require('webpack-merge');
const parts = require('./webpack.parts');
const common = require('./webpack.common');
const path = require('path');

module.exports = merge([
  common,
  // {
    // performance: {
      // hints: "warning", 
      // maxEntrypointSize: 100000, 
      // maxAssetSize: 450000, 
    // },
    // output: {
      // chunkFilename: "[name].[hash:8].js",
      // filename: "[name].[hash:8].js",
    // },
    // recordsPath: path.join(__dirname, "records.json"),
  // },
  parts.clean(['static'], parts.PATHS.assets),
  parts.minifyJavaScript({}),
  parts.minifyCSS({
    options: {
      discardComments: {
        removeAll: true,
        safe: true,
      },
    },
  }),
  // parts.extractBundles([
    // {
      // name: "vendor",
      // minChunks: ({ resource }) => /node_modules/.test(resource),
    // },
    // {
      // name: "manifest",
      // minChunks: Infinity,
    // },
  // ]),
  parts.generateSourceMaps({ type: "source-map" }),
  parts.loadImages({
    options: {
      limit: 15000,
      name: "[name].[hash:8].[ext]",
    },
  }),
  parts.setFreeVariable("process.env.NODE_ENV", "production"),
]);
