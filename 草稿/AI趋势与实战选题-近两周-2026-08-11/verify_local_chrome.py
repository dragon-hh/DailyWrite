from pathlib import Path
from playwright.sync_api import sync_playwright


ROOT = Path(__file__).resolve().parent
HTML_DIR = ROOT / "design-demos"
OUT_DIR = ROOT / "verification-screenshots"
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
FILES = ["editorial-brief.html", "operations-manual.html", "signal-map.html"]
VIEWPORTS = [(1440, 900), (390, 844)]
REQUIRED = [
    "2026-07-29",
    "AI HOT",
    "Builders",
    "每个成功任务的成本",
    "Harness",
    "Agent 安全别只靠",
    "Skill 越装越多",
    "AI 写代码、AI 审代码后",
]


def main():
    OUT_DIR.mkdir(exist_ok=True)
    failed = False
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=CHROME, headless=True)
        for filename in FILES:
            for width, height in VIEWPORTS:
                errors = []
                warnings = []
                context = browser.new_context(
                    viewport={"width": width, "height": height},
                    device_scale_factor=1,
                )
                page = context.new_page()
                page.on("pageerror", lambda exc: errors.append(str(exc)))
                page.on(
                    "console",
                    lambda msg: warnings.append(f"{msg.type}: {msg.text}")
                    if msg.type in ("warning", "error")
                    else None,
                )
                page.goto((HTML_DIR / filename).as_uri(), wait_until="load")
                page.wait_for_timeout(400)
                body_text = page.locator("body").inner_text()
                missing = [value for value in REQUIRED if value not in body_text]
                overflow = page.evaluate(
                    "document.documentElement.scrollWidth > document.documentElement.clientWidth + 1"
                )
                broken_anchors = page.evaluate(
                    """
                    Array.from(document.querySelectorAll('a[href^="#"]'))
                      .map(a => a.getAttribute('href'))
                      .filter(h => h && h !== '#' && !document.querySelector(h))
                    """
                )
                stem = Path(filename).stem
                page.screenshot(
                    path=str(OUT_DIR / f"{stem}-{width}x{height}.png"), full_page=False
                )
                page.screenshot(
                    path=str(OUT_DIR / f"{stem}-{width}x{height}-full.png"), full_page=True
                )
                buttons = page.locator("button:not(.print-btn):not(#printPage)")
                for index in range(min(buttons.count(), 5)):
                    button = buttons.nth(index)
                    if button.is_visible():
                        button.click()
                        page.wait_for_timeout(60)
                ok = not errors and not missing and not overflow and not broken_anchors
                failed = failed or not ok
                print(
                    f"{filename} {width}x{height} ok={ok} "
                    f"errors={len(errors)} warnings={len(warnings)} "
                    f"missing={missing} overflow={overflow} broken_anchors={broken_anchors}"
                )
                context.close()
        browser.close()
    raise SystemExit(1 if failed else 0)


if __name__ == "__main__":
    main()
