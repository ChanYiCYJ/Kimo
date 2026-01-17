 /* Loading */
   const hideLoader = () => {
  const loader = document.getElementById("global-loading");
  if (!loader) return;
  loader.classList.add("fade-out");
  setTimeout(() => loader.remove(), 600);
};

// 正常 load
window.addEventListener("load", hideLoader);

setTimeout(hideLoader, 15000);

  /* Blur-up 背景 */
  document.addEventListener("DOMContentLoaded", () => {
    const el = document.getElementById("bg-image");
    const bg = getComputedStyle(el).backgroundImage.slice(5, -2);
    const img = new Image();
    img.src = bg;
    img.onload = () => el.classList.add("loaded");
  });