const path = require('path');
const HtmlWebPackPlugin = require('html-webpack-plugin');
const CleanWebPackPlugin = require('clean-webpack-plugin');
const webpack = require('webpack');

module.exports = {
  mode: 'development',
  entry: {
    app: './src/index.js',
    print: './src/print.js',
  },
  output: {
    filename: '[name].bundle.js',
    path: path.resolve(__dirname, 'js', 'dist')
  },
  devtool: 'inline-source-map',
  devServer: {
      contentBase: './dist',
      hot: true,
      disableHostCheck: true,
      port: 5000,
      host: "0.0.0.0"
  },
  module: {
      rules: [
      {
      test: /\.css$/, 
      use: [
          'style-loader',
          'css-loader'
      ]},
      {
          test: /\.(png|svg|jpg|gif)$/,
      use:[
          {
           loader: 'file-loader',
           options: {
               outputPath: 'images/'
           }
          }
      ]},
      ],
  },
  plugins: [
      new CleanWebPackPlugin(['dist']),
      new HtmlWebPackPlugin({
          title: 'dev',
          template: './src/index.html',
          filename: 'index.html'
      }),
      new webpack.HotModuleReplacementPlugin()

    ],
  output: {
    filename: '[name].bundle.js',
    path: path.resolve(__dirname, 'dist')
  }
};
