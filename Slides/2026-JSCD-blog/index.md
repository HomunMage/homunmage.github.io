---
title: Why I use Jekyll + WC
---


大約十年前，我的需求單純到近乎天真：我只想要一個地方紀錄我的筆記。

最早，我像大多數人一樣，試過各大部落格平台。Google Blogger 用過，Medium 也寫過一陣子。它們方便，一鍵發佈，但問題很快就浮現：我被平台綁架了。

當我想搬家時，發現內容搬不走，格式亂成一團，SEO 要從頭來過。我受夠了這種「租房子」的感覺，我想要自己的土地，自己的房子。於是我決定一切自己來。

那時候的我，甚至覺得資料庫是多餘的。我在 GitHub 上建了個 repo，把路由邏輯直接映射到檔案系統結構。 home/README.md 是首頁，about/README.md 是關於我，tech/linux/README.md 是技術文章。

每個目錄一個檔案，這就是我的網站。純粹，直接，醜陋但實用。當時我覺得自己很聰明：沒有後端，沒有 Render Loop，就是最原始的 HTTP 檔案傳輸。

但很快地，這種「原始」變成了一種折磨。沒有共用的導覽列，我每寫一篇新文章，就要手動複製貼上 HTML header；沒有樣式管理，整個網站看起來像是 1990 年代的佈告欄。

於是我踏入了 Jekyll 的世界。

Jekyll 讓我第一次體驗到「樣板（Template）」的威力。套上一個 Theme，網站瞬間像樣了。但隨著我對內容的要求變高，痛苦也隨之而來。

我想在文章裡加入互動圖表，或者一個動態的程式碼展示區。在 Jekyll 的邏輯裡，這是一場災難。

我必須在 ```_includes/``` 資料夾裡建立 chart.html，裡面塞滿了 <script> 標籤和 Liquid 邏輯。然後在 Markdown 裡，我得用一種奇怪的語法去呼叫它。

我的專案結構變成了義大利麵：

Markdown 負責內容，但混雜了 Liquid 標籤。
HTML 負責結構，但混雜了 JavaScript 邏輯。
JS 負責互動，但必須依賴 Liquid 注入變數。
每當我要修改一個圖表的顏色，我得同時打開 Markdown 檔、HTML layout 檔和 CSS 檔，在三個視窗間切換，腦袋裡的 Stack 不斷溢出。

我開始逃避。我試過 Hugo（太快但更難改），試過 Gatsby（React 生態系太重，光是設定 Webpack 和 GraphQL 就花掉我寫作的力氣）。

直到我遇見了 Web Components 和 Svelte。

這是我第一次感受到「關注點分離」的真正力量。我不再需要 Jekyll 去處理複雜的邏輯。

嘗試了 Lit 寫 wc，覺得 Lit 是極其反人類的寫法，差點放棄之餘意外發現 Svelte 也能 compile as wc。

我用 Svelte 寫好一個乾淨的 ```<my-chart>``` 元件，編譯成標準的 Web Component。 在 Markdown 裡，我只需要寫： ```<my-chart data="[1,2,3]"></my-chart>```

Jekyll 瞬間退化成一個只負責 content 的空殼路由，而 Svelte 接管了所有互動。那一刻，世界清靜了。Markdown 負責說故事，Component 負責變魔術，兩者互不干擾。

跟 AI 聊天後發現，這就是現代的 Islands Architecture 設計理念，而 Astro 正是這個概念的極致。

雖然想要嘗試其他方法

問題已經不是在呈現方式 而是compile 後的架構結果

hugo template 語法複雜 沒有liquid好用

MDsveX 只能在特定資料夾 不能隨意資料夾檔案自動成為html

svelte 最接近的方法
```
  src/
  ├── routes/
  │   ├── +page.svelte         # Home page (shows recent blog posts)
  │   ├── +layout.svelte       # Global layout with dark theme
  │   ├── blog/
  │   │   ├── +page.svelte     # Blog listing
  │   │   ├── [slug]/          # Dynamic blog post pages
  │   │   └── tags/            # Tags browser with expandable groups
  │   └── docs/
  │       ├── +page.svelte     # Docs listing
  │       ├── [slug]/          # Dynamic doc pages
  │       └── tags/            # Docs tags browser
  ├── content/
  │   ├── blog/
  │   └── docs/
  └── lib/
```

這個方法最接近自動md成為html

但是資料夾仍然沒有jekyll 彈性

最終還是只能使用jekyll + wc