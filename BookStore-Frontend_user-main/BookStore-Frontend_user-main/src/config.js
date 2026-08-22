/* ============================================================
   Global configuration for the Book Store user frontend.
   ============================================================ */

// Base URL of the FastAPI backend.
// Default points at the local backend. When deploying, set
// REACT_APP_API_URL to your hosted backend URL (it is inlined at
// build/start time by Create React App).
export const API_BASE_URL =
  process.env.REACT_APP_API_URL || "http://127.0.0.1:8000";

// Currency symbol used when formatting prices.
export const CURRENCY = "$";

// Number of books shown per page on the shop page.
export const BOOKS_PER_PAGE = 12;

