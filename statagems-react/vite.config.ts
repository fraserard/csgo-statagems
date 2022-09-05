import react from "@vitejs/plugin-react";
import { defineConfig } from "vite";
import { dependencies } from './package.json'; 

function renderChunks(deps: Record<string, string>) {
  let chunks = {};
  Object.keys(deps).forEach((key) => {
    if (["react", "react-router-dom", "react-dom"].includes(key)) return;
    chunks[key] = [key];
  });
  return chunks;
}

const path = require("path");

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: { "~": path.resolve(__dirname, "src") },
  },
  server: {
    host: true,
    port: 3000,
    proxy: {
      "/auth": {
        target: "http://127.0.0.1:5000",
        changeOrigin: true,
        secure: true,
      },
      "/graphql": {
        target: "http://127.0.0.1:5000",
        changeOrigin: true,
        secure: true,
      },
    },
  },
  build: {
    sourcemap: false,
    rollupOptions: {
      output: {
        manualChunks: {
          vendor: ["react", "react-router-dom", "react-dom"],
          ...renderChunks(dependencies),
        },
      },
    },
  },
});
