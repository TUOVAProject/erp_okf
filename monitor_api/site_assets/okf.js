(() => {
  const root = window.OKF_ROOT || "";
  const index = window.OKF_INDEX || [];
  const search = document.getElementById("search");
  const results = document.getElementById("results");
  const nav = document.getElementById("nav");
  const side = document.getElementById("side");
  const esc = s => s.replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  const LIMIT = 60;

  // Ranks exact names first, then prefix, then substring, then description matches.
  function rank(e, term) {
    const t = e.t.toLowerCase();
    const cls = e.id.slice(e.id.indexOf(".") + 1).toLowerCase();
    if (t === term || cls === term) return 0;
    if (t.startsWith(term) || cls.startsWith(term)) return 1;
    if (t.includes(term) || cls.includes(term)) return 2;
    if (e.d.toLowerCase().includes(term)) return 3;
    return -1;
  }

  function run() {
    const term = search.value.trim().toLowerCase();
    if (!term) {
      results.hidden = true;
      nav.hidden = false;
      return;
    }
    const hits = [];
    for (const e of index) {
      const r = rank(e, term);
      if (r >= 0) hits.push([r, e]);
    }
    hits.sort((a, b) => a[0] - b[0] || a[1].t.localeCompare(b[1].t));
    results.innerHTML = hits.length
      ? hits.slice(0, LIMIT).map(([, e]) =>
          `<a class="hit" href="${root}${e.p}">` +
          `<span class="hit-t">${esc(e.t)}</span>` +
          `<span class="hit-m">${e.m} · ${e.k}</span>` +
          `<span class="hit-d">${esc(e.d)}</span></a>`
        ).join("") + (hits.length > LIMIT ? `<p class="hit-more">+${hits.length - LIMIT} more — refine the search</p>` : "")
      : `<p class="hit-more">No entities match.</p>`;
    results.hidden = false;
    nav.hidden = true;
  }

  search.addEventListener("input", run);
  search.addEventListener("keydown", e => {
    if (e.key === "Enter") {
      const first = results.querySelector("a");
      if (first) location.href = first.href;
    } else if (e.key === "Escape") {
      search.value = "";
      run();
    }
  });
  document.addEventListener("keydown", e => {
    const tag = document.activeElement && document.activeElement.tagName;
    if (e.key === "/" && tag !== "INPUT" && tag !== "TEXTAREA") {
      e.preventDefault();
      side.classList.add("open");
      search.focus();
      search.select();
    }
  });

  document.getElementById("menu").addEventListener("click", () => side.classList.toggle("open"));
  side.addEventListener("click", e => {
    if (e.target.closest("a")) side.classList.remove("open");
  });

  // Highlight the table-of-contents entry for the section in the URL hash.
  function markHash() {
    for (const a of nav.querySelectorAll("a.here")) a.classList.remove("here");
    if (!location.hash) return;
    const a = nav.querySelector(`.toc a[href="${location.hash.replace(/"/g, "")}"]`);
    if (a) {
      a.classList.add("here");
      a.scrollIntoView({ block: "nearest" });
    }
  }
  window.addEventListener("hashchange", markHash);
  markHash();

  // Row filter on long tables (property lists, permission and module listings).
  for (const wrap of document.querySelectorAll(".content .table-wrap")) {
    const rows = [...wrap.querySelectorAll("tbody tr")];
    if (rows.length < 15) continue;
    const filter = document.createElement("input");
    filter.type = "search";
    filter.className = "table-filter";
    filter.placeholder = `Filter ${rows.length} rows…`;
    filter.addEventListener("input", () => {
      const term = filter.value.trim().toLowerCase();
      for (const row of rows) {
        row.hidden = term !== "" && !row.textContent.toLowerCase().includes(term);
      }
    });
    wrap.before(filter);
  }
})();
