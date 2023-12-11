/** @type {import('next').NextConfig} */
const nextConfig = {
    reactStrictMode: true,
    compiler: {
        styledComponents: true,
    },
    async rewrites() {
        return [
            {
                source: `${process.env.NEXT_PUBLIC_API_URL}/:match*`,
                destination: `${process.env.API_BASE_URL}/:match*`,
            }
        ]
    }
}

module.exports = nextConfig
