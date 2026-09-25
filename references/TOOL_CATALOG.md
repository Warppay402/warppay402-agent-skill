# Tool Catalog & Input Schemas

| Tool Name | Price (USDC) | Category | Required Inputs |
| --- | --- | --- | --- |
| `public_data_feed` | $0.0001 | Data Feed | `filename: string` |
| `data_feeds` | $0.0010 | Data Feed | `feedId: string` |
| `web_scraper` | $0.0010 | Web Tool | `url: string` |
| `browser_scraper` | $0.0050 | Web Tool | `url: string` |
| `base_analytics` | $0.0020 | Analytics | `address: string` |
| `arc_analytics` | $0.0010 | Analytics | None |
| `arc_network_oracle_query` | $0.1000 | Telemetry | Optional: `includeGasTrends`, `checkMerchantAccount` |
| `arc_dex_oracle` | $0.0010 | Oracle | Optional: `pair` (default: "ETH/USDC") |
| `x402_telemetry_feed` | Free | Telemetry | None |
| `pdf_extractor` | $0.0050 | Document | `pdfUrl: string` |
| `render_screenshot` | $0.0100 | Document | `url: string` |
| `extract_json` | $0.0100 | Data Tool | `url: string`, `schema: object` |
| `smart_contract_verifier` | $0.0200 | Security | `address: string` |
| `get_aerodrome_yields` | $0.0030 | DeFi | None |
| `aerodrome_swap` | $0.0100 | DeFi | `tokenIn`, `tokenOut`, `amountIn`, `decimalsIn`, `isStable` |
| `aerodrome_clamm` | $0.0100 | DeFi | `action`: ("mint", "increaseLiquidity", "decreaseLiquidity", "collect") |
| `aerodrome_veaero` | $0.0100 | Governance | `action`: ("createLock", "increaseAmount", "increaseUnlockTime", "vote", "claimBribes") |
| `deploy_contract` | $5.0000 | Deployment | `contractType`: ("escrow", "bounty", "subscription", "pendle") |
| `deploy_solana_contract` | $5.0000 | Deployment | `contractType`: ("spl_escrow", "cnft_badge", "raydium_vault"), `params` |
| `deploy_arc_contract` | $5.0000 | Deployment | `contractType`: ("escrow", "bounty", "subscription") |
| `arc_cctp_bridge` | $0.2500 | Bridge | `amountUsdc`, `destinationChain`, `recipientAddress` |
| `real_estate_calculator` | $0.0005 | Real Estate | `purchasePrice: number`, `monthlyRent: number` |
| `address_normalizer` | $0.0010 | Geocoding | `address: string` |
| `weather_oracle` | $0.0010 | Logistics | `latitude: number`, `longitude: number` |
| `forex_oracle` | $0.0005 | Finance | Optional: `baseCurrency: string` (default: "USD") |
| `shipping_rate_estimator` | $0.0010 | E-Commerce | `weightLbs: number`, `originZip: string`, `destinationZip: string` |
| `github_health_analyzer` | $0.0020 | Developer | `repository: string` (e.g., "honojs/hono") |
| `property_comps_estimator` | $0.0050 | Real Estate | `squareFeet: number`, `bedrooms: number`, `zipCode: string` |