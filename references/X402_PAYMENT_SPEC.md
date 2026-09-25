# x402 Micropayment Protocol Specification

## Flow Overview

1. The client sends a standard HTTP POST or MCP `tools/call` request.
2. If payment is required and not attached, the server responds with HTTP Status `402 Payment Required`.
3. The response headers include `PAYMENT-REQUIRED` containing a Base64-encoded JSON challenge payload.
4. The client signs an off-chain EIP-712 authorization (or Solana SPL transfer payload) and re-submits the request with the `PAYMENT-SIGNATURE` header.