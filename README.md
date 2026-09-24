# 頭骨 Landmark 標註（網頁版）

在瀏覽器裡旋轉 3D 頭骨、點選 landmark、匯出標註 JSON；學習頁可以看標好的點與解剖講解。

- 標註頁：`標註.html`（網站首頁會自動導過去）
- 學習頁：`學習.html`
- 目前的模型：`models/Model-mobile.glb`（塑膠教學頭骨，MAKAR／iPhone 手機掃描）。
  網頁版把貼圖從 PNG 轉成 JPEG（9.6 MB → 2.1 MB），網格一個位元組都沒動：幾何雜湊值與原檔相同，原檔標出的 JSON 可以直接用。
- 大檔由 jsDelivr CDN 傳送（部分網路連 GitHub Pages 很慢），失敗時自動改從本站讀。

> 這是公開網站：任何拿到網址的人都看得到。**不要上傳大體老師資料**（標成 `sensitive` 的模型會被自動拒絕）。

## 學習者（只能看）

打開網址就是學習頁 → 選教材 → 點圖釘或名稱看講解。不用登入，也不能修改任何教材。

## 教學者（線上標註、直接更新）

1. 到「標註」頁 → 右上角「教學者登入」→ 用 Google 帳號登入。
2. 帳號在教學者名單上時，「存成 JSON」會變成「存到網站」：按下去就直接更新網站上的教材（同名＝更新），學習頁重新整理就看得到。
3. 每次存檔都會在資料庫留一份歷史；如果別人在你打開之後先改過，網站會拒絕覆蓋，請重新開最新版再改。
4. 不在名單上的帳號一樣可以練習標註，但只能下載 JSON。

**新增教學者**：Firebase 主控台（專案 skull-landmark）→ Firestore Database → `teachers` 集合 → 新增文件，文件 ID 填對方的 Gmail，欄位隨意（例如 `name`）。

權限由 Firebase 伺服器端規則強制執行：人人可讀；只有名單上的教學者能新增、修改、刪除教材。

## 備用：直接放 JSON 檔

標註 JSON 也可以放在 `models/Model-mobile.landmarks/`（GitHub 網頁 → `Add file` → `Upload files`，同檔名＝替換），部署後會出現在模型庫。
同名時以線上（教學者存到網站）的版本為準。

## 新增模型

上傳 `models/新模型.glb`，再放一個同名的 `models/新模型.meta.json`：

```json
{ "title": "顯示名稱", "description": "一兩句說明", "preset": "skull", "sensitive": false }
```

`preset` 用 `skull`（頭骨清單）或 `blank`（自訂點）。單檔上限 100 MB（GitHub 限制）。
