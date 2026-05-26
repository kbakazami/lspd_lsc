export function initAnimations(): void {
  if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return

  // ── Hero (au-dessus du fold, déclenché au chargement) ───────────────────

  requestAnimationFrame(() => {
    document.querySelector("[data-hero='badge']")?.classList.add("visible")
  })

  document.querySelectorAll<HTMLElement>("[data-hero]:not([data-hero='badge'])").forEach(el => {
    const order = parseInt(el.dataset.hero ?? "1", 10)
    setTimeout(() => el.classList.add("visible"), order * 130)
  })

  // ── Scroll (IntersectionObserver natif) ─────────────────────────────────

  const once = (el: Element, fn: (el: Element) => void) => {
    const io = new IntersectionObserver(
      entries => {
        if (!entries[0].isIntersecting) return
        fn(el)
        io.disconnect()
      },
      { rootMargin: "0px 0px -60px 0px" },
    )
    io.observe(el)
  }

  document.querySelectorAll("[data-anim='fade-up'], [data-anim='fade-in']").forEach(el => {
    once(el, target => target.classList.add("visible"))
  })

  document.querySelectorAll("[data-anim='stagger']").forEach(el => {
    once(el, parent => {
      Array.from(parent.children).forEach((child, i) => {
        const c = child as HTMLElement
        c.style.transitionDelay = `${i * 100}ms`
        c.classList.add("visible")
      })
    })
  })
}
