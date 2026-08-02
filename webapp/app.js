const form = document.getElementById("scanForm");
const scanBtn = document.getElementById("scanBtn");
const btnLabel = scanBtn.querySelector(".btn-label");
const btnSpinner = scanBtn.querySelector(".btn-spinner");
const formError = document.getElementById("formError");
const resultsMeta = document.getElementById("resultsMeta");
const patchPanel = document.getElementById("patchPanel");
const tableWrap = document.getElementById("resultsTableWrap");
const resultsBody = document.getElementById("resultsBody");
const resultsActions = document.getElementById("resultsActions");
const downloadBtn = document.getElementById("downloadJson");
const brandDot = document.getElementById("brandDot");

const MAX_PORTS = 500;

// Common ports get a friendly service name + a plausible "open" bias,
// purely to make the simulated output look realistic. None of this
// touches the network.
const KNOWN_PORTS = {
  21: ["ftp", "220 (vsFTPd 3.0.5)"],
  22: ["ssh", "SSH-2.0-OpenSSH_8.9"],
  23: ["telnet", null],
  25: ["smtp", "220 mail ESMTP Postfix"],
  53: ["domain", null],
  80: ["http", "Server: nginx/1.24.0"],
  110: ["pop3", "+OK POP3 ready"],
  143: ["imap", null],
  443: ["https", "Server: nginx/1.24.0"],
  3306: ["mysql", "5.7.42-log"],
  3389: ["ms-wbt-server", null],
  5432: ["postgresql", null],
  6379: ["redis", "-ERR wrong number of arguments"],
  8080: ["http-alt", "Server: Werkzeug/3.0"],
  27017: ["mongod", null],
};

let lastResult = null;

// Small deterministic string hash so the same host+port always
// produces the same simulated result (feels consistent across runs).
function hash(str) {
  let h = 2166136261;
  for (let i = 0; i < str.length; i++) {
    h ^= str.charCodeAt(i);
    h = Math.imul(h, 16777619);
  }
  return h >>> 0;
}

function parsePortSpec(spec) {
  const ports = new Set();
  for (const chunk of spec.split(",")) {
    const c = chunk.trim();
    if (!c) continue;
    if (c.includes("-")) {
      const [a, b] = c.split("-").map((x) => parseInt(x.trim(), 10));
      if (Number.isNaN(a) || Number.isNaN(b) || a < 1 || b > 65535 || a > b) {
        throw new Error(`Invalid port range segment: '${c}'`);
      }
      for (let p = a; p <= b; p++) ports.add(p);
    } else {
      const p = parseInt(c, 10);
      if (Number.isNaN(p) || p < 1 || p > 65535) {
        throw new Error(`Invalid port value: '${c}'`);
      }
      ports.add(p);
    }
  }
  if (!ports.size) throw new Error("No valid ports parsed from input.");
  if (ports.size > MAX_PORTS) {
    throw new Error(`Demo caps scans at ${MAX_PORTS} ports (requested ${ports.size}).`);
  }
  return [...ports].sort((a, b) => a - b);
}

function simulatePort(host, port) {
  const known = KNOWN_PORTS[port];
  const roll = hash(`${host}:${port}`) % 100;
  // Known/common ports are biased toward "open" so the demo looks realistic.
  const openThreshold = known ? 55 : 6;
  const filteredThreshold = openThreshold + 8;

  let status;
  if (roll < openThreshold) status = "open";
  else if (roll < filteredThreshold) status = "filtered";
  else status = "closed";

  return {
    port,
    status,
    service: known ? known[0] : status === "open" ? "unknown" : null,
    banner: status === "open" && known ? known[1] : null,
  };
}

function setLoading(isLoading) {
  scanBtn.disabled = isLoading;
  btnSpinner.hidden = !isLoading;
  btnLabel.textContent = isLoading ? "Simulating…" : "Run simulated scan";
  brandDot.style.background = isLoading ? "#ffb000" : "#35d48a";
  brandDot.style.boxShadow = isLoading ? "0 0 8px #ffb000" : "0 0 8px #35d48a";
}

function showError(message) {
  formError.textContent = message;
  formError.hidden = false;
}

function clearError() {
  formError.hidden = true;
  formError.textContent = "";
}

function renderPanel(results) {
  patchPanel.innerHTML = "";
  if (!results.length) {
    patchPanel.innerHTML = '<p class="patch-empty">No ports in range.</p>';
    return;
  }
  const frag = document.createDocumentFragment();
  results.forEach((r, i) => {
    const jack = document.createElement("div");
    jack.className = "jack";
    jack.dataset.status = r.status;
    jack.style.animationDelay = Math.min(i * 4, 500) + "ms";
    jack.title = r.service ? `${r.port} · ${r.service}` : String(r.port);
    jack.innerHTML = `<span class="jack-led"></span><span class="jack-port">${r.port}</span>`;
    frag.appendChild(jack);
  });
  patchPanel.appendChild(frag);
}

function escapeHtml(str) {
  const div = document.createElement("div");
  div.textContent = str;
  return div.innerHTML;
}

function renderTable(results) {
  resultsBody.innerHTML = "";
  const openFirst = [...results].sort((a, b) => {
    if (a.status === b.status) return a.port - b.port;
    return a.status === "open" ? -1 : b.status === "open" ? 1 : a.port - b.port;
  });
  const frag = document.createDocumentFragment();
  openFirst.forEach((r) => {
    const tr = document.createElement("tr");
    tr.innerHTML = `
      <td>${r.port}</td>
      <td class="status-${r.status}">${r.status}</td>
      <td>${r.service || "—"}</td>
      <td>${r.banner ? escapeHtml(r.banner) : "—"}</td>
    `;
    frag.appendChild(tr);
  });
  resultsBody.appendChild(frag);
}

form.addEventListener("submit", (e) => {
  e.preventDefault();
  clearError();

  const host = document.getElementById("host").value.trim();
  const portSpec = document.getElementById("ports").value.trim();

  if (!host) {
    showError("Enter a target host or IP.");
    return;
  }

  let ports;
  try {
    ports = parsePortSpec(portSpec);
  } catch (err) {
    showError(err.message);
    return;
  }

  setLoading(true);
  resultsMeta.textContent = `Simulating ${host}…`;
  tableWrap.hidden = true;
  resultsActions.hidden = true;
  patchPanel.innerHTML = '<p class="patch-empty">Generating simulated results…</p>';

  // Small artificial delay so it feels like a scan, not an instant table dump.
  setTimeout(() => {
    const started = performance.now();
    const results = ports.map((p) => simulatePort(host, p));
    const duration = ((performance.now() - started) / 1000).toFixed(3);
    const openCount = results.filter((r) => r.status === "open").length;

    lastResult = {
      host,
      resolved_ip: "(simulated — no DNS lookup performed)",
      duration_seconds: Number(duration),
      ports_scanned: results.length,
      open_count: openCount,
      results,
      engine: "simulated-demo",
    };

    resultsMeta.textContent =
      `simulated · ${openCount} open / ${results.length} scanned · ${duration}s`;
    renderPanel(results);
    renderTable(results);
    tableWrap.hidden = false;
    resultsActions.hidden = false;
    setLoading(false);
  }, 350);
});

downloadBtn.addEventListener("click", () => {
  if (!lastResult) return;
  const blob = new Blob([JSON.stringify(lastResult, null, 2)], { type: "application/json" });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = `mini-scanner-demo_${lastResult.host}_${Date.now()}.json`;
  a.click();
  URL.revokeObjectURL(url);
});
