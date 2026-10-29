/* =========================================================
   이규영 포트폴리오 — interactions
   ========================================================= */
(function () {
  "use strict";

  const $ = (sel, ctx = document) => ctx.querySelector(sel);
  const $$ = (sel, ctx = document) => Array.from(ctx.querySelectorAll(sel));
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const fine = window.matchMedia("(pointer: fine)").matches;

  /* ---------- nav: stuck state ---------- */
  const nav = $(".nav");
  if (nav) {
    const onScroll = () => {
      nav.classList.toggle("is-stuck", window.scrollY > 24);
    };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  /* ---------- nav: mobile menu ---------- */
  const burger = $(".nav__burger");
  if (burger && nav) {
    burger.addEventListener("click", () => {
      const open = nav.classList.toggle("is-open");
      burger.setAttribute("aria-expanded", String(open));
      document.body.classList.toggle("is-locked", open);
    });
    $$(".nav__panel a").forEach((a) =>
      a.addEventListener("click", () => {
        nav.classList.remove("is-open");
        burger.setAttribute("aria-expanded", "false");
        document.body.classList.remove("is-locked");
      })
    );
    window.addEventListener("keydown", (e) => {
      if (e.key === "Escape" && nav.classList.contains("is-open")) burger.click();
    });
  }

  /* ---------- nav: invert over paper ---------- */
  const paper = document.getElementById("paper");
  if (nav && paper) {
    const paperToggle = () => {
      nav.classList.toggle("is-paper", window.scrollY + 46 >= paper.offsetTop);
    };
    paperToggle();
    window.addEventListener("scroll", paperToggle, { passive: true });
    window.addEventListener("resize", paperToggle);
  }

  /* ---------- seoul clock ---------- */
  const clock = $("[data-clock]");
  if (clock) {
    const tick = () => {
      const now = new Date();
      const t = new Intl.DateTimeFormat("ko-KR", {
        timeZone: "Asia/Seoul",
        hour: "2-digit",
        minute: "2-digit",
        second: "2-digit",
        hour12: false,
      }).format(now);
      clock.textContent = `SEONGNAM ${t}`;
    };
    tick();
    setInterval(tick, 1000);
  }

  /* ---------- reveal on scroll ---------- */
  const revealEls = $$("[data-reveal]");
  if (revealEls.length) {
    if (!("IntersectionObserver" in window) || reduce) {
      revealEls.forEach((el) => el.classList.add("is-in"));
    } else {
      const io = new IntersectionObserver(
        (entries) => {
          entries.forEach((entry) => {
            if (entry.isIntersecting) {
              entry.target.classList.add("is-in");
              io.unobserve(entry.target);
            }
          });
        },
        { rootMargin: "0px 0px -8% 0px", threshold: 0.08 }
      );
      revealEls.forEach((el) => io.observe(el));
    }
  }

  /* ---------- marquee: seamless duplication ---------- */
  const track = $(".marquee__track");
  if (track && !reduce) {
    track.innerHTML += track.innerHTML;
  }

  /* ---------- design cards: image presence ---------- */
  $$(".dcard__img").forEach((img) => {
    const mark = () => img.classList.add("is-loaded");
    if (img.complete && img.naturalWidth > 0) mark();
    img.addEventListener("load", mark);
    img.addEventListener("error", () => img.remove());
  });

  /* ---------- work: mobile colour chips ---------- */
  $$(".work").forEach((row) => {
    const chip = $(".work__chip", row);
    if (!chip) return;
    chip.textContent = row.dataset.num || "";
    chip.style.background = row.dataset.grad || "#1a1a1e";
    if (row.dataset.ink === "dark") chip.classList.add("is-dark");
  });

  /* ---------- design gallery: broken image fallback ---------- */
  $$(".dfig img").forEach((img) => {
    img.addEventListener("error", () => {
      const fig = img.closest(".dfig");
      if (fig) fig.classList.add("is-missing");
      img.remove();
    });
  });

  /* ---------- work: cursor-follow preview ---------- */
  const preview = $("[data-preview]");
  if (preview && fine && !reduce) {
    const poster = $(".preview__poster", preview);
    const pLabel = $("[data-preview-label]", preview);
    const pTitle = $("[data-preview-title]", preview);
    const pNum = $("[data-preview-num]", preview);
    let tx = 0,
      ty = 0,
      cx = 0,
      cy = 0,
      active = false;

    const move = (e) => {
      tx = e.clientX;
      ty = e.clientY;
    };
    window.addEventListener("pointermove", move, { passive: true });

    const render = () => {
      cx += (tx - cx) * 0.14;
      cy += (ty - cy) * 0.14;
      preview.style.transform = `translate(${cx}px, ${cy}px) translate(-50%, -50%)`;
      requestAnimationFrame(render);
    };

    $$(".work").forEach((row) => {
      row.addEventListener("pointerenter", (e) => {
        if (!active) {
          cx = e.clientX;
          cy = e.clientY;
          active = true;
          requestAnimationFrame(render);
        }
        pLabel.textContent = row.dataset.label || "";
        pTitle.textContent = row.dataset.title || "";
        pNum.textContent = row.dataset.num || "";
        poster.style.background = row.dataset.grad || "#1a1a1e";
        poster.classList.toggle("is-dark", row.dataset.ink === "dark");
        preview.classList.add("is-on");
      });
      row.addEventListener("pointerleave", () => {
        preview.classList.remove("is-on");
      });
    });
  }

  /* ---------- detail page: subtle parallax on cover ---------- */
  const cover = $("[data-cover]");
  if (cover && fine && !reduce) {
    const img = $("img", cover);
    if (img) {
      let raf = null;
      window.addEventListener(
        "scroll",
        () => {
          if (raf) return;
          raf = requestAnimationFrame(() => {
            const r = cover.getBoundingClientRect();
            const p = Math.max(-1, Math.min(1, r.top / window.innerHeight));
            img.style.transform = `translateY(${p * -14}px) scale(1.03)`;
            raf = null;
          });
        },
        { passive: true }
      );
    }
  }
})();
