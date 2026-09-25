---
name: warppay402-gateway
description: Use WarpPay402 MCP Gateway to run Web3 smart contract deployments (Base, Solana, Arc), Aerodrome DEX swaps/CLAMM/veAERO yield operations, Circle CCTP bridging, web/PDF scrapers, address geocoding, flight weather, forex rates, USPS shipping rates, property tax comps, and GitHub health audits via x402 USDC micropayments. Use when the user asks for Web3 DeFi execution, cross-chain transfers, contract deployment, or real-world data oracles.
license: MIT
compatibility: Fully compatible with HTTP JSON-RPC 2.0, MCP v2.0, and x402 micropayments.
metadata:
  author: WarpPay402 Studio
  version: "1.0.0"
  homepage: https://www.warppay402.com
  mcp_endpoint: https://api.warppay402.com/mcp?v=2
  openapi_spec: https://api.warppay402.com/openapi.json
---

# WarpPay402 MCP Gateway & Micro-Oracle Skill

This skill allows agents to invoke 28 specialized Web3, real-world utility, and developer automation tools on-demand via the x402 micropayment protocol ($0.0001–$5.00 USDC).

## Quick Start Guidelines

1. **Endpoint Access:** All tools are accessible via the MCP SSE Stream endpoint `https://api.warppay402.com/mcp?v=2` or direct POST requests to `https://api.warppay402.com/api/v1/tools/{tool_name}`.
2. **x402 Micropayments:** Every protected endpoint returns a `402 Payment Required` challenge with payment instructions in the `PAYMENT-REQUIRED` header if payment is unfulfilled.
3. **Supported Settlement Networks:**
   - **Base Mainnet** (`eip155:8453`): USDC (`0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913`)
   - **Solana Mainnet** (`solana:5eykt4UsFv8P8NJdTREpY1vzqKqZKvdp`): SPL USDC (`EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v`)
   - **Arbitrum One** (`eip155:42161`): USDC (`0xaf88d065e77c8cC2239327C5EDb3A432268e5831`)
   - **Arc Mainnet** (`eip155:5042`): Native USDC (`0x0000000000000000000000000000000000000000`)

---

## Decision Rules (When to Choose Which Tool)

- **If the user asks for Web3 DeFi or Yields:**
  - Aerodrome yield pools/APYs → Use `get_aerodrome_yields`
  - Token swaps on Base → Use `aerodrome_swap`
  - Concentrated liquidity range management → Use `aerodrome_clamm`
  - Governance voting, locking, or bribe claims → Use `aerodrome_veaero`
- **If the user asks to deploy smart contracts ($5.00 USDC):**
  - Base Mainnet escrow/bounty/subscription → Use `deploy_contract`
  - Solana SPL escrow/cNFT badge/Raydium vault → Use `deploy_solana_contract`
  - Arc Mainnet escrow/bounty/subscription → Use `deploy_arc_contract`
- **If the user asks for cross-chain transfers:**
  - Bridge USDC from Arc to Solana/Base/Arbitrum → Use `arc_cctp_bridge`
- **If the user asks for real-world utilities or micro-oracles:**
  - Real estate Cap Rate, NOI, DSCR financial modeling → Use `real_estate_calculator`
  - Address standardization & Lat/Lon geocoding → Use `address_normalizer`
  - Live atmospheric conditions & drone flight safety → Use `weather_oracle`
  - Global fiat currency conversion rates → Use `forex_oracle`
  - Domestic USPS shipping rate estimates → Use `shipping_rate_estimator`
  - Public GitHub repository star/issue/license health → Use `github_health_analyzer`
  - Property market valuations & tax assessor comps → Use `property_comps_estimator`

---

## Detailed References

Refer to the included sub-documents for exhaustive technical specifications:
- Read `references/TOOL_CATALOG.md` for complete argument schemas for all 28 tools.
- Read `references/X402_PAYMENT_SPEC.md` for EIP-712 payment authorization formats.