import React, { useState } from "react";
import "./SearchBar.css";

function SearchBar() {
  const [query, setQuery] = useState("");
  const [open, setOpen] = useState(false);
  const [suggestions] = useState(["watch", "wallet", "belt"]); // demo

  function onSearch(e) {
    e.preventDefault();
    alert("Searching for: " + query); // just a action for demo
  }

  return (
    <div className="search-container" role="search" aria-label="Site search">
      <form onSubmit={onSearch} style={{ position: "relative" }}>
        <input
          className="search-input"
          type="text"
          placeholder="Search"
          aria-label="Search input field"
          value={query}
          onChange={(e) => {
            setQuery(e.target.value);
            setOpen(e.target.value.length > 0);
          }}
          aria-haspopup="listbox"
          aria-expanded={open}
          aria-controls={open ? "search-list" : undefined}
          aria-autocomplete="list"
        />

        <button className="search-btn" aria-label="Search button" type="submit">
          🔍
        </button>

        {/* simple suggestion area */}
        {open && (
          <ul
            id="search-list"
            role="listbox"
            aria-label="Search suggestions"
            style={{
              position: "absolute",
              left: 0,
              right: 0,
              marginTop: "0.25rem",
              background: "#fff",
              border: "1px solid #ddd",
              borderRadius: "0.5rem",
              listStyle: "none",
              padding: "0.5rem",
            }}
          >
            {suggestions
              .filter((s) => s.includes(query.toLowerCase()))
              .map((s, i) => (
                <li
                  key={i}
                  role="option"
                  aria-selected="false"
                  style={{ padding: "0.25rem 0.5rem" }}
                >
                  {s}
                </li>
              ))}
          </ul>
        )}
      </form>
    </div>
  );
}

export default SearchBar;
