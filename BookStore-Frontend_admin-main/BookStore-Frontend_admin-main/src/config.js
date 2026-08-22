/* ============================================================
   Global configuration for the Book Store admin frontend.
   ============================================================ */

// Base URL of the FastAPI backend.
// Default points at the local backend. When deploying, set
// REACT_APP_API_URL to your hosted backend URL (it is inlined at
// build/start time by Create React App).
export const API_BASE_URL =
  process.env.REACT_APP_API_URL || "http://127.0.0.1:8000";

// Currency symbol used when formatting prices.
export const CURRENCY = "$";

// How many books the admin lists per page.
export const BOOKS_PER_PAGE = 15;

