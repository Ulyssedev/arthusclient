import { invoke } from "@tauri-apps/api/tauri";

if (localStorage.theme === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
  // add data-theme="dark" to <html>, if the os is in dark mode
  document.documentElement.setAttribute('data-theme', 'dark');
} else {
  document.documentElement.setAttribute('data-theme', 'light');
}

let darkModeToggleEl: HTMLInputElement | null = null;
let musicToggleEl: HTMLInputElement | null = null;

async function switchTheme() {
  if (darkModeToggleEl) {
    if (darkModeToggleEl.checked) {
      document.documentElement.setAttribute('data-theme', 'dark');
      localStorage.theme = 'dark';
    } else {
      document.documentElement.setAttribute('data-theme', 'light');
      localStorage.theme = 'light';
    }
  }
}

window.addEventListener("DOMContentLoaded", () => {
  darkModeToggleEl = document.querySelector("#theme-button");
  document.querySelector("#theme-button")?.addEventListener("click", (_) => {
    console.log("clicked")
    switchTheme();
  });
  musicToggleEl = document.querySelector("#music");
  document.querySelector("#music")?.addEventListener("click", (_) => {
    invoke("music")
  });
});
