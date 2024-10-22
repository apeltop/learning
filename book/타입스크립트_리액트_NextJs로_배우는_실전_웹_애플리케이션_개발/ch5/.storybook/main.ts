import type {StorybookConfig} from "@storybook/nextjs";
import path from "path";

const config: StorybookConfig = {
    stories: ["../src/**/*.mdx", "../src/**/*.stories.@(js|jsx|mjs|ts|tsx)"],
    addons: [
        "@storybook/addon-links",
        "@storybook/addon-essentials",
        "@storybook/addon-onboarding",
        "@storybook/addon-interactions",
    ],
    framework: {
        name: "@storybook/nextjs",
        options: {},
    },
    docs: {
        autodocs: "tag",
    },
    webpack: async config => {
        if ("resolve" in config) {
            if (config.resolve) {
                config.resolve.alias['@'] = path.resolve(__dirname, '../src/');
            }
        }
        return config;
    },
    webpackFinal: async config => {
        if ("resolve" in config) {
            if (config.resolve) {
                config.resolve.alias['@'] = path.resolve(__dirname, '../src/');
            }
        }
        return config;
    },
    staticDirs: ['../public'],
};
export default config;
