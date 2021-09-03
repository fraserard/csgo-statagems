// @ts-check

/**
 * @type {import('next').NextConfig}
 **/

module.exports = {
  reactStrictMode: true,
  images: {
    domains: ['cdn.akamai.steamstatic.com'],
  },
  async rewrites() {
    return [
      {
        source: '/api/:path*',
        destination: 'http://127.0.0.1:5000/api/:path*' // Proxy to Backend
      },
      {
        source: '/auth/:path*',
        destination: 'http://127.0.0.1:5000/auth/:path*' // Proxy to Backend
      },
    ]
  }
}
