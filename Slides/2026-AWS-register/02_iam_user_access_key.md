# 02 - 建立 IAM 使用者與 Access Key / Create IAM User & Access Key

> ⚠️ **重要警告 / Critical Warning**
> 本教學僅適用 AWS Global(`aws.amazon.com`)。
> 若註冊頁出現「中國區 / 由光環新網或西雲營運 / Sinnet / NWCD」字樣,請立即關閉重來。
> This guide applies to AWS Global only. Close and restart if you see "China region / operated by Sinnet or NWCD".

---

## 預估 / Estimate

- 時間 (Time):約 15 分鐘
- 費用 (Cost):免費 (IAM 服務本身不收費 / IAM is free)
- 需準備 (Prerequisites):
  - 已完成 01 - 註冊 AWS 帳號(Task 1 完成)
  - AWS 帳號 email 與密碼(用於登入 Console)

---

## 為何不能用 Root Access Key / Why NOT Root Access Key

Root 帳號(您註冊 AWS 時的主帳號)擁有**所有服務、所有資源的完整控制權**,包括刪除帳號、修改帳單、移除所有資料。一旦 Root Access Key 外洩,攻擊者可以：

- 開啟大量 EC2 挖礦,產生巨額帳單
- 刪除所有資料庫與 S3 備份
- 無法追蹤是誰操作的

**正確做法**:建立一個「只有部署所需權限」的 IAM 使用者,把 Access Key 給我方使用。就算金鑰外洩,影響範圍也限於被授權的服務,且可立刻停用。

> 🔑 **Root 帳號 = 大樓萬能鑰匙;IAM 使用者 = 只能進特定樓層的門禁卡**

---

## 名詞快查 / Glossary

| 中文 | English | 說明 |
|------|---------|------|
| 身分識別與存取管理 | IAM (Identity and Access Management) | AWS 權限管理服務 |
| 使用者 | User | IAM 中的一個帳號身分 |
| 政策 / 原則 | Policy | 定義「可以做哪些事」的規則文件 |
| 存取金鑰 | Access Key | 程式呼叫 AWS API 用的金鑰對 |
| 存取金鑰 ID | Access Key ID | 公開部分(類似帳號) |
| 私密存取金鑰 | Secret Access Key | 私密部分(類似密碼,只顯示一次) |
| 主控台 | Console | AWS 網頁管理介面 |
| 根使用者 | Root User | 註冊 AWS 時的主帳號,避免日常使用 |

---

## 操作步驟 / Steps

### 步驟 1:登入 AWS 管理主控台 (Step 1: Sign in to AWS Management Console)

1. 開啟瀏覽器,前往 `https://aws.amazon.com`
2. 點擊右上角「登入主控台 (Sign in to the Console)」或「登入 (Sign in)」按鈕

   ![中文版:AWS 管理主控台入口](images/02_console_signin_zh.webp)
   ![English: AWS Management Console](images/02_console_signin_en.webp)

3. 選擇「根使用者 (Root user)」並輸入您的 email 與密碼登入
4. 完成 MFA 驗證(如已設定)

---

### 步驟 2:進入 IAM 服務 (Step 2: Open IAM Service)

1. 登入後,在頂部搜尋列輸入 `IAM`,點擊出現的「IAM」服務

   ![待補:Console 搜尋 IAM](images/placeholder_02_console_search_iam.webp)

2. 確認左上角顯示為 Global(IAM 是全域服務,不受 Region 影響)

---

### 步驟 3:建立 IAM 使用者 (Step 3: Create IAM User)

1. 在左側選單點擊「使用者 (Users)」
2. 點擊右上角「建立使用者 (Create user)」

   ![待補:IAM Users 頁面 — 點擊 Create user (zh)](images/placeholder_02_iam_users_create_zh.webp)
   ![待補:IAM Users page — click Create user (en)](images/placeholder_02_iam_users_create_en.webp)

3. **使用者名稱 (User name)** 欄位填入:
   ```
   lattice-cast-deploy
   ```
4. **不要**勾選「提供使用者對 AWS 管理主控台的存取權 (Provide user access to the AWS Management Console)」
   - 此帳號只供程式使用,不需要 Console 登入權限
5. 點擊「下一步 (Next)」

   ![待補:填入 User name 畫面 (zh)](images/placeholder_02_iam_username_zh.webp)

---

### 步驟 4:附加權限 (Step 4: Attach Permissions)

1. 在「設定許可 (Set permissions)」頁面,選擇「直接附加政策 (Attach policies directly)」

   ![待補:選擇 Attach policies directly (zh)](images/placeholder_02_iam_attach_policies_zh.webp)

2. 在搜尋框逐一搜尋並勾選以下 5 個政策:

   | 政策名稱 (Policy Name) | 用途 |
   |----------------------|------|
   | `AmazonEC2FullAccess` | 管理虛擬機器 (EC2) |
   | `AmazonS3FullAccess` | 管理物件儲存 (S3) |
   | `AmazonRDSFullAccess` | 管理資料庫 (RDS) |
   | `AmazonRoute53FullAccess` | 管理 DNS 域名 (Route 53) |
   | `CloudWatchLogsFullAccess` | 讀取應用程式日誌 (CloudWatch Logs) |

   > ⚠️ **絕對不要勾選 (Do NOT attach)**:
   > - `AdministratorAccess`
   > - `IAMFullAccess`
   > - `PowerUserAccess`

   ![待補:勾選 5 個 Policy 畫面 (zh)](images/placeholder_02_iam_policies_selected_zh.webp)

3. 確認右側「許可摘要 (Permissions summary)」顯示剛勾選的 5 項政策
4. 點擊「下一步 (Next)」

---

### 步驟 5:確認並建立使用者 (Step 5: Review and Create)

1. 確認畫面顯示:
   - 使用者名稱 (User name):`lattice-cast-deploy`
   - 附加政策 (Attached policies):5 項如上
2. 點擊「建立使用者 (Create user)」

   ![待補:Review and Create 畫面 (zh)](images/placeholder_02_iam_review_create_zh.webp)

3. 成功後會看到「已成功建立使用者 (User created successfully)」提示

---

### 步驟 6:建立 Access Key (Step 6: Create Access Key)

1. 在 IAM 使用者清單,點擊剛建立的「`lattice-cast-deploy`」
2. 點擊「安全憑證 (Security credentials)」標籤

   ![待補:Security credentials 標籤 (zh)](images/placeholder_02_iam_security_credentials_zh.webp)

3. 往下捲動到「存取金鑰 (Access keys)」區塊,點擊「建立存取金鑰 (Create access key)」
4. 在使用案例選擇頁面,選擇「在 AWS 外部執行的應用程式 (Application running outside AWS)」→「其他 (Other)」

   ![待補:選擇 Use case — Other (zh)](images/placeholder_02_iam_key_usecase_zh.webp)

5. 描述標籤 (Description tag value) 可填入:`lattice-cast-deploy-key`(選填)
6. 點擊「建立存取金鑰 (Create access key)」

---

### 步驟 7:下載並保存金鑰 (Step 7: Download and Save the Key)

> ⚠️ **這是唯一一次能看到 Secret Access Key 的機會!視窗關閉後永遠無法再查看。**
> This is the **only time** you can view the Secret Access Key. Once closed, it cannot be retrieved.

1. 畫面會顯示:
   - **存取金鑰 ID (Access key ID)**:格式如 `AKIAIOSFODNN7EXAMPLE`
   - **私密存取金鑰 (Secret access key)**:格式如 `wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`

   ![待補:Access Key 顯示畫面 (zh)](images/placeholder_02_iam_key_created_zh.webp)

2. 點擊「下載 .csv 檔案 (Download .csv file)」,將金鑰儲存到本機安全位置
3. 確認 `.csv` 檔案已下載成功後,點擊「完成 (Done)」關閉視窗

> 📁 下載的 CSV 檔案包含 `Access key ID` 與 `Secret access key` 兩欄,請妥善保管。

---

## 完成後請回報 / Deliverables to Send Us

完成後請把以下資訊用**安全管道**(1Password / Bitwarden 共享連結、ProtonMail 加密)傳給我們:

**安全管道傳送(加密方式)**:
- Access Key ID(格式:`AKIA...`)
- Secret Access Key(從下載的 `.csv` 取得)

**可用一般訊息回報(非機密)**:
- AWS 帳號 ID(12 位數字,在 Console 右上角帳號名稱下方可找到)
- IAM 使用者名稱:`lattice-cast-deploy`
- AWS Region(您主要使用的區域,例如:`ap-northeast-1` 東京 / `us-east-1` 維吉尼亞)

> 🚫 **禁止傳送管道**:純文字 email、LINE、Slack 明文、Telegram、Google Doc
> ✅ **建議管道**:1Password 共享連結、Bitwarden Send、ProtonMail 加密信件

---

## 檢核清單 / Checklist

助理操作完逐項打勾後回傳本文件:

- [ ] 已確認使用 `aws.amazon.com`(非 `.cn`)登入
- [ ] 已以 Root 帳號登入 Console
- [ ] 已建立名為 `lattice-cast-deploy` 的 IAM 使用者
- [ ] 確認**未**勾選 Console 存取權限
- [ ] 已附加以下 5 個 Policy(且未附加 AdministratorAccess / IAMFullAccess):
  - [ ] `AmazonEC2FullAccess`
  - [ ] `AmazonS3FullAccess`
  - [ ] `AmazonRDSFullAccess`
  - [ ] `AmazonRoute53FullAccess`
  - [ ] `CloudWatchLogsFullAccess`
- [ ] 已建立 Access Key(選擇「Other / Application running outside AWS」)
- [ ] 已下載 `.csv` 金鑰檔案
- [ ] 已將 Access Key ID + Secret Access Key 用安全管道傳給我方
- [ ] 已將 AWS 帳號 ID / IAM user name / Region 回報給我方

---

## 常見問題 / FAQ

**Q: 找不到「直接附加政策 (Attach policies directly)」選項?**
A: 若畫面顯示「新增使用者至群組 (Add user to group)」,請往右找到「直接附加政策 (Attach policies directly)」那一格點擊。AWS Console 偶爾改版,但三個選項都在同一頁。

**Q: Secret Access Key 視窗不小心關掉了怎麼辦?**
A: 無法找回。請回到 `lattice-cast-deploy` → 安全憑證 (Security credentials) → 先「停用 (Deactivate)」再「刪除 (Delete)」舊金鑰,然後重新建立一組新的 Access Key,重複步驟 6-7。

**Q: CSV 下載後應該放在哪裡?**
A: 建議儲存在加密的密碼管理器(1Password / Bitwarden)或加密硬碟,**不要**儲存在 Google Drive、Dropbox、桌面等未加密位置。

**Q: 要建立幾組 Access Key?**
A: 只需一組。AWS 每個 IAM 使用者最多可建立 2 組;保留一個空位以便日後輪換。

**Q: 頁面出現英文,看不懂怎麼辦?**
A: AWS Console 語言設定在右上角帳號選單 → 「Language & Region」→ 選「繁體中文 (Traditional Chinese)」即可切換。

**Q: 找不到 AWS 帳號 ID?**
A: 登入 Console 後,點擊右上角帳號名稱,12 位數字帳號 ID 會顯示在下拉選單上方。

---

## 出問題時 / If Something Goes Wrong

聯絡:lifetreemastery@gmail.com,附上錯誤訊息截圖。

---

## 待補截圖 / Pending Screenshots (Console Internal Pages)

以下截圖需助理實際操作時補充:

| Placeholder 檔名 | 說明 |
|----------------|------|
| `placeholder_02_console_search_iam.webp` | Console 頂部搜尋 IAM 的畫面 |
| `placeholder_02_iam_users_create_zh.webp` | IAM Users 頁面點擊 Create user(中文 UI) |
| `placeholder_02_iam_users_create_en.webp` | IAM Users 頁面點擊 Create user(英文 UI) |
| `placeholder_02_iam_username_zh.webp` | 填入 User name: lattice-cast-deploy |
| `placeholder_02_iam_attach_policies_zh.webp` | 選擇 Attach policies directly |
| `placeholder_02_iam_policies_selected_zh.webp` | 5 個 Policy 已勾選的畫面 |
| `placeholder_02_iam_review_create_zh.webp` | Review and Create 確認畫面 |
| `placeholder_02_iam_security_credentials_zh.webp` | 使用者 Security credentials 標籤 |
| `placeholder_02_iam_key_usecase_zh.webp` | 選擇 Use case: Other |
| `placeholder_02_iam_key_created_zh.webp` | Access Key ID + Secret Key 顯示畫面 |
