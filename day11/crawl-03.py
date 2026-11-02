# 예제3] 동적 페이지 크롤링

# C:\venvs\py314\Scripts\python.exe -m pip install playwright : 셀레니움과 비슷한 동적 페이지 조작 라이브러리 설치
# playwright install    :

import asyncio  # 비동기 라이브러리
from playwright.async_api import async_playwright
# 1) 크롤링할 페이지 주소
url = "https://search.naver.com/search.naver?ssc=tab.image.all&query=위꼴짤"

async def run() :
    async with async_playwright() as p :
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto(url)

        for i in range(2):
            await page.wait_for_timeout(2000)
            await page.evaluate("window.scrollTo (0 , document.body.scrollHeight)")
            items = await page.query_selector_all(".tile_item")

            for item in items:
                title = await item.query_selector('.info_title')
                title = await title.inner_text()
                img = await item.query_selector('._fe_image_tab_content_thumbnail_image')
                img = await img.get_attribute('src') if img else '이미지없음'
                print(title, img)

asyncio.run(run())