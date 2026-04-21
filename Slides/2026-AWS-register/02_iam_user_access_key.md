# 02 - 建立 IAM 使用者與 Access Key / Create IAM User & Access Key

您好 {{客戶稱呼}},非常感謝您協助我們完成 AWS 環境的設定!這個步驟是幫我們建立一個「專用部署帳號」,讓我們的系統能自動連接 AWS。整個過程約 15 分鐘,照下方步驟操作即可,遇到任何不清楚的地方歡迎直接來信告訴我們。

> 💡 **貼心提醒**:截圖可能因 AWS 介面更新略有差異,以實際畫面為準。若畫面找不到按鈕,請寄信告訴我們,我們立刻協助。

> ⚠️ **重要:請勿使用 AWS 中國區 / Do NOT use AWS China**
> 操作請使用 `aws.amazon.com`。若頁面出現「中國區 / 光環新網 / 西雲 / Sinnet / NWCD」字樣,請關閉視窗從 `https://aws.amazon.com` 重新進入。
> (中國區是另一個獨立服務,與我們要部署的系統不相容。)

---

## 預估 / Estimate

- **時間 (Time)**:約 15 分鐘
- **費用 (Cost)**:免費 — IAM 服務本身完全不收費 (IAM is always free)
- **需準備 (Prerequisites)**:
  - 已完成第 01 篇「註冊 AWS 帳號」
  - AWS Root 帳號的 email 與密碼(用於登入 Console)

---

## 為什麼不能直接用主帳號的 Key? / Why NOT the Root Account Key?

您在註冊 AWS 時建立的「根帳號 (Root user)」擁有**所有服務的完整控制權**,包括刪除帳號、修改帳單、清空所有資料。若這把鑰匙外洩,後果無法挽回。

正確做法是幫我們建立一個「只有部署所需權限」的 IAM 使用者,交給我們使用。就算這個帳號出問題,影響範圍也僅限特定服務,且您隨時可以一鍵停用。

> 🔑 **根帳號 = 大樓萬能鑰匙;IAM 使用者 = 只能進特定樓層的門禁卡**

---

## 名詞解說 / Glossary

以下是本篇會出現的技術名詞,全部用白話解釋:

| 名詞 | 說明 |
|------|------|
| IAM (Identity and Access Management) | AWS 的「人員與權限管理」服務 — 就像公司的 HR 系統,決定誰能做什麼 |
| IAM 使用者 (IAM User) | 我們在 AWS 裡建立的一個「專用帳號身分」,只給我們的部署系統使用 |
| 政策 (Policy) | 一份「許可清單」,定義這個 IAM 使用者被允許操作哪些服務 |
| Access Key ID | 類似帳號名稱,公開部分,格式如 `AKIAIOSFODNN7EXAMPLE` |
| Secret Access Key | 類似密碼,私密部分,**只在建立時顯示一次**,請務必立刻儲存 |
| 主控台 (Console) | 就是 `console.aws.amazon.com` — AWS 的網頁管理介面 |
| 根使用者 (Root User) | 您當初用 email 註冊 AWS 時的主帳號,擁有最高權限 |

---

## 操作步驟 / Steps

### 步驟 1:登入 AWS 管理主控台 (Step 1: Sign In to the AWS Management Console)

1. 開啟瀏覽器,前往 `https://aws.amazon.com/tw/console/` (繁體中文介面) 或 `https://aws.amazon.com/console/` (英文介面)
2. 點擊頁面上的「**登入 (Sign in)**」按鈕

   ![中文版:AWS 管理主控台 — 登入入口](images/02_console_login_zh.webp)
   *來源: [AWS Management Console](https://aws.amazon.com/tw/console/), 取用日期 2026-04-21*

   ![English: AWS Management Console — Sign in](images/02_console_login_en.webp)
   *來源: [AWS Management Console](https://aws.amazon.com/console/), 取用日期 2026-04-21*

3. 在登入頁面,選擇「**根使用者 (Root user)**」
4. 輸入您的 AWS 帳號 email 與密碼
5. 若有設定 MFA(兩步驟驗證),輸入驗證碼後即可進入主控台

---

### 步驟 2:進入 IAM 服務 (Step 2: Open the IAM Service)

IAM(身分識別與存取管理)是管理帳號與權限的地方,也是我們接下來操作的核心。

1. 登入後,您會看到 AWS 管理主控台首頁
2. 在頁面**頂部搜尋列**輸入 `IAM`,點擊出現的「**IAM**」服務

   > 💡 搜尋列在畫面頂端中央,是一個灰色的長方形輸入框,旁邊可能有放大鏡圖示。

   以下為 IAM 服務的產品介紹頁示意:

   ![中文版:AWS IAM 服務產品頁示意](images/02_iam_product_zh.webp)
   *來源: [AWS Identity and Access Management (IAM)](https://aws.amazon.com/tw/iam/), 取用日期 2026-04-21*

   ![English: AWS IAM Service Product Page](images/02_iam_product_en.webp)
   *來源: [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/), 取用日期 2026-04-21*

3. 進入 IAM 後,您會看到左側有一個選單(可能需要點擊展開)。IAM 是「全域服務 (Global)」,不受地區 (Region) 影響,右上角的地區顯示為「Global」是正常的。

   以下是主控台內 IAM 導覽路徑示意:
   ```
   AWS Console 首頁
   └── 頂部搜尋列輸入「IAM」
       └── 點擊「IAM」進入
           └── 左側選單 → 使用者 (Users)
   ```

---

### 步驟 3:建立 IAM 使用者 (Step 3: Create an IAM User)

1. 在 IAM 左側選單中,點擊「**使用者 (Users)**」
2. 點擊右上角橘色按鈕「**建立使用者 (Create user)**」
3. 在「**使用者名稱 (User name)**」欄位,填入以下名稱(請完整複製貼上):

   ```
   lattice-cast-deploy
   ```

4. **不要**勾選「提供使用者對 AWS 管理主控台的存取權 (Provide user access to the AWS Management Console)」
   - 這個帳號只是給我們的程式使用,不需要人工登入 Console 的權限
5. 點擊「**下一步 (Next)**」

   > 💡 若您的 Console 介面是英文,步驟如下:
   > Left menu → **Users** → **Create user** → Enter `lattice-cast-deploy` as User name → **Do NOT** check "Provide user access to the AWS Management Console" → **Next**

---

### 步驟 4:附加必要的服務權限 (Step 4: Attach Permissions)

這一步是告訴 AWS「我們的帳號可以操作哪些服務」。

1. 在「**設定許可 (Set permissions)**」頁面,選擇第三個選項:「**直接附加政策 (Attach policies directly)**」
   - 頁面上通常有三個選項排列在一起,選最右邊或最下面那個即可

2. 在下方的搜尋框,**逐一**搜尋以下 5 個政策名稱,每找到一個就在左側打勾:

   | 政策名稱 (Policy Name) | 用途說明 |
   |----------------------|----------|
   | `AmazonEC2FullAccess` | 管理虛擬伺服器 (EC2) |
   | `AmazonS3FullAccess` | 管理檔案儲存空間 (S3) |
   | `AmazonRDSFullAccess` | 管理資料庫 (RDS) |
   | `AmazonRoute53FullAccess` | 管理網域名稱 (Route 53) |
   | `CloudWatchLogsFullAccess` | 讀取系統運作日誌 (CloudWatch Logs) |

   > ⚠️ **請勿勾選以下高風險政策 (Do NOT attach these)**:
   > - `AdministratorAccess`
   > - `IAMFullAccess`
   > - `PowerUserAccess`
   >
   > 以上三個政策權限過大,超出我們的實際需求。

3. 確認右側「**許可摘要 (Permissions summary)**」區塊顯示剛才勾選的 5 項政策
4. 點擊「**下一步 (Next)**」

   以下為附加政策步驟的導覽路徑示意:
   ```
   建立使用者 — 設定許可頁面
   ├── 選擇「直接附加政策 (Attach policies directly)」
   ├── 搜尋並勾選 AmazonEC2FullAccess      ✓
   ├── 搜尋並勾選 AmazonS3FullAccess       ✓
   ├── 搜尋並勾選 AmazonRDSFullAccess      ✓
   ├── 搜尋並勾選 AmazonRoute53FullAccess  ✓
   ├── 搜尋並勾選 CloudWatchLogsFullAccess ✓
   └── 點擊「下一步 (Next)」
   ```

---

### 步驟 5:確認並建立使用者 (Step 5: Review and Create)

1. 確認頁面顯示:
   - **使用者名稱 (User name)**:`lattice-cast-deploy`
   - **附加政策 (Attached policies)**:5 項如上
2. 點擊「**建立使用者 (Create user)**」橘色按鈕
3. 看到「**已成功建立使用者 (User created successfully)**」的訊息即表示完成

---

### 步驟 6:為使用者建立 Access Key (Step 6: Create an Access Key)

Access Key 是我們的程式連接 AWS 時使用的「鑰匙」,分為公開的 ID 和私密的 Secret。

1. 在 IAM 使用者清單中,點擊剛建立的「**`lattice-cast-deploy`**」使用者名稱
2. 進入使用者詳細頁面後,點擊「**安全憑證 (Security credentials)**」標籤
3. 往下捲動到「**存取金鑰 (Access keys)**」區塊,點擊「**建立存取金鑰 (Create access key)**」

   導覽路徑示意:
   ```
   IAM 左側選單 → 使用者 (Users)
   → 點擊「lattice-cast-deploy」
   → 標籤列: 安全憑證 (Security credentials)
   → 往下捲動到「存取金鑰 (Access keys)」區塊
   → 點擊「建立存取金鑰 (Create access key)」
   ```

4. 在「**使用案例 (Use case)**」選擇頁面,選擇:
   - 「**在 AWS 外部執行的應用程式 (Application running outside AWS)**」
   - 或選「**其他 (Other)**」(依您看到的選項而定)
   - 勾選下方確認框後點擊「**下一步 (Next)**」

5. 「**描述標籤值 (Description tag value)**」欄位選填,可輸入 `lattice-cast-deploy-key` 方便日後識別

6. 點擊「**建立存取金鑰 (Create access key)**」

---

### 步驟 7:儲存金鑰(非常重要!)(Step 7: Save the Keys — Critical!)

> ⚠️ **這是唯一一次能看到完整金鑰的機會！**
> Secret Access Key(私密存取金鑰)在視窗關閉後**永遠無法再查看或找回**。請務必在關閉頁面前完成儲存。
>
> This is the **only time** you can view the Secret Access Key. Once you close this page, it cannot be retrieved.

1. 畫面會顯示兩組資料:
   - **存取金鑰 ID (Access key ID)**:格式如 `AKIAIOSFODNN7EXAMPLE`(公開部分)
   - **私密存取金鑰 (Secret access key)**:格式如 `wJalrXUtnFEMI/K7MDENG/bPxRfiCY...`(機密部分)

2. 點擊「**下載 .csv 檔案 (Download .csv file)**」,將金鑰儲存到本機的安全位置
   - `.csv` 檔案可用 Excel 或記事本開啟,裡面有兩欄:Access key ID 和 Secret access key

3. 確認 `.csv` 已成功下載後,點擊「**完成 (Done)**」關閉頁面

   > 📁 建議將此 `.csv` 存入密碼管理器(1Password / Bitwarden),**不要**放在桌面、Google Drive 或任何未加密的地方。

---

## 完成後請提供以下資訊 / Please Send Us

完成後,麻煩您把以下資訊用**安全管道**傳給我們,我們收到後就可以開始部署系統,不會再打擾您進行其他操作。

**需要用加密方式傳送(含機密內容)**:
- Access Key ID(格式:`AKIA...`)
- Secret Access Key(從下載的 `.csv` 取得)

**可以用一般訊息回報(非機密)**:
- AWS 帳號 ID(12 位數字 — 登入 Console 後,點擊右上角帳號名稱即可看到)
- IAM 使用者名稱:`lattice-cast-deploy`(如實際填入的名稱)
- AWS 主要地區(例:`ap-northeast-1` 東京、`us-east-1` 維吉尼亞)

> 🚫 **請勿透過以下管道傳送**:純文字 email、LINE 訊息、Slack 明文、Telegram、Google 文件
>
> ✅ **建議使用**:1Password 共享連結、Bitwarden Send、ProtonMail 加密信件
>
> **若不確定如何加密傳送,歡迎來信告訴我們,我們會提供 1Password 共享連結讓您直接填入。**

---

## 操作確認清單 / Checklist

以下項目完成後可以打勾,方便您和我們對照進度:

- [ ] 確認使用 `aws.amazon.com`(非 `.cn` 結尾的網址)登入
- [ ] 已用 Root 帳號登入 AWS Console
- [ ] 已建立名稱為 `lattice-cast-deploy` 的 IAM 使用者
- [ ] 確認**沒有**勾選 Console 登入存取權限(使用者只做程式用途)
- [ ] 已附加以下 5 個 Policy,且**沒有**附加 `AdministratorAccess`：
  - [ ] `AmazonEC2FullAccess`
  - [ ] `AmazonS3FullAccess`
  - [ ] `AmazonRDSFullAccess`
  - [ ] `AmazonRoute53FullAccess`
  - [ ] `CloudWatchLogsFullAccess`
- [ ] 已建立 Access Key(選擇使用案例「Other」或「Application running outside AWS」)
- [ ] 已下載 `.csv` 金鑰檔案並存放到安全位置
- [ ] 已將 Access Key ID + Secret Access Key 用安全管道傳給我們
- [ ] 已將 AWS 帳號 ID / IAM 使用者名稱 / Region 回報給我們

---

## 常見問題 / FAQ

**Q:找不到「直接附加政策 (Attach policies directly)」選項?**
A:若畫面只看到「新增使用者至群組 (Add user to group)」,請找找頁面右側或下方是否有其他選項。AWS Console 偶爾改版,但「直接附加政策」的選項通常在同一頁的右側區塊。若找不到,截圖寄給我們,我們告訴您在哪裡。

**Q:Secret Access Key 的視窗不小心關掉了怎麼辦?**
A:無法找回。請回到 IAM → 使用者 → `lattice-cast-deploy` → 安全憑證 (Security credentials),先點「**停用 (Deactivate)**」再「**刪除 (Delete)**」舊金鑰,然後重新執行步驟 6-7 建立新的一組。

**Q:下載的 CSV 檔案要放在哪裡保管?**
A:建議存入 1Password 或 Bitwarden 等加密密碼管理器。**請勿**放在 Google Drive、Dropbox、桌面等未加密位置。

**Q:一個 IAM 使用者需要建立幾組 Access Key?**
A:只需一組。AWS 每個 IAM 使用者最多可建立 2 組;保留一個空位是好習慣,方便日後需要輪換金鑰時使用。

**Q:Console 介面顯示英文看不懂某個按鈕?**
A:AWS Console 語言設定在右上角帳號選單 → 「Language & Region」→ 選「繁體中文 (Traditional Chinese)」即可切換。若仍有疑問,把畫面截圖寄給我們(lifetreemastery@gmail.com),我們告訴您要按哪裡。

**Q:哪裡找到我的 AWS 帳號 ID(12 位數字)?**
A:登入 Console 後,點擊右上角帳號名稱,12 位數字 ID 會顯示在下拉選單上方。

**Q:不小心附加了 AdministratorAccess 怎麼辦?**
A:沒關係。回到 IAM → 使用者 → `lattice-cast-deploy` → 許可 (Permissions) 標籤,找到 `AdministratorAccess`,點「**移除 (Remove)**」即可。我們的系統只需要上面列出的 5 個 Policy。

---

## 遇到問題聯絡我們 / If Something Goes Wrong

📧 **lifetreemastery@gmail.com** — 請附上畫面截圖,我們會儘快回覆並協助您完成設定。

---

再次感謝您協助完成這個步驟!設定完成後,我們就能接手把 lattice-cast 系統架起來,您不需要再做任何額外操作。有任何問題隨時歡迎來信。
