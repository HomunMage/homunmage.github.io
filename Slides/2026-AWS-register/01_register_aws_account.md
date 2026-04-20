# 01 - 註冊 AWS Global 帳號 / Register AWS Global Account

> ⚠️ **重要警告 / Critical Warning**
> 本教學僅適用 AWS Global（`aws.amazon.com`）。
> 若註冊頁出現「中國區 / 由光環新網或西雲營運 / Sinnet / NWCD」字樣，請立即關閉重來。
> This guide applies to AWS Global only. Close and restart if you see "China region / operated by Sinnet or NWCD".

---

## 預估 / Estimate

- 時間 (Time)：約 30〜45 分鐘
- 費用 (Cost)：首月 $1 USD 信用卡驗證扣款（會退還）；Free Tier 免費方案可使用 12 個月
- 需準備 (Prerequisites)：
  - 信用卡（VISA / Mastercard，需可付外幣 / Must support foreign currency）
  - Email 信箱（建議用公司 email，避免使用 Gmail 可能的驗證延遲）
  - 手機（收 SMS 驗證碼 / For SMS verification code）
  - Authenticator App（如 Authy、Google Authenticator，用於 MFA）

---

## 名詞快查 / Glossary

| 中文 | English | 說明 |
|------|---------|------|
| 區域 | Region | AWS 機房的地理位置，例如東京、維吉尼亞 |
| 帳號 | Account | 您的 AWS 帳號，有唯一 12 碼 Account ID |
| 根使用者 | Root user | 帳號主帳號，擁有完整權限，僅用於初始設定 |
| 多因素驗證 | MFA (Multi-Factor Authentication) | 登入需要密碼以外的第二驗證，大幅提升安全性 |
| 免費方案 | Free Tier | AWS 提供 12 個月的免費使用額度 |
| IAM | IAM (Identity and Access Management) | AWS 的帳號與權限管理服務 |

---

## 操作步驟 / Steps

### 步驟 1：確認使用正確網址（Step 1: Verify Correct Website）

1. 開啟瀏覽器（Chrome 或 Edge 建議），前往 `https://aws.amazon.com`

   **台灣中文版**：
   ![AWS 台灣首頁（中文版）](images/01_register_home_zh.webp)

   **英文版**：
   ![AWS Homepage (English)](images/01_register_home_en.webp)

2. ✅ 確認網址列顯示 `aws.amazon.com`（**不是** `amazonaws.com.cn`）

3. 如果畫面出現「西雲數據」、「光環新網」、「Sinnet」或「NWCD」，代表進入了中國區，請立即關閉並重新輸入 `https://aws.amazon.com`

   **中國區對照（請勿使用）**：
   ![中國區警告對照 / AWS China — Do NOT use](images/01_warning_china.webp)

---

### 步驟 2：建立 AWS 帳號（Step 2: Create AWS Account）

1. 在 `https://aws.amazon.com` 首頁，點擊右上角橘色按鈕「建立 AWS 帳戶 (Create an AWS Account)」

2. 進入註冊頁 `https://portal.aws.amazon.com/billing/signup`：

   ![AWS 註冊表單 / AWS Sign Up Form (English)](images/01_register_form_en.webp)

   > 📌 **說明**：AWS 註冊表單固定以英文顯示，這是正常的。

3. 填寫以下欄位：
   - **Root user email address**：輸入您的公司 email（此為帳號的主 email，請妥善保管）
   - **AWS account name**：輸入公司或組織名稱（例如 `MyCompany-AWS`）

4. 點擊「Verify email address」按鈕，系統會寄送驗證碼到您的 email

5. 開啟信箱，找到主旨為「AWS Email Verification」的信，複製 6 位數驗證碼

6. 回到 AWS 頁面，貼上驗證碼，點擊「Verify」

---

### 步驟 3：設定密碼（Step 3: Set Password）

![待補：密碼設定頁面截圖](images/placeholder_01_password_en.webp)

1. 填寫「Root user password」（根使用者密碼）：
   - 建議長度 ≥ 16 字元，包含大寫、小寫、數字、符號
   - 範例格式：`MyAWS#2024!Secure`
   - **強烈建議**使用密碼管理器（1Password / Bitwarden）儲存

2. 再次輸入密碼「Confirm root user password」

3. 點擊「Continue (Step 1 of 5)」

---

### 步驟 4：選擇帳號類型（Step 4: Account Type）

![待補：帳號類型選擇頁](images/placeholder_01_account_type_en.webp)

1. 選擇用途：
   - 公司使用 → 選「Business - for your work, school, or organization」
   - 個人使用 → 選「Personal - for your own projects」

2. 填寫基本資訊（公司名稱、電話、地址）

3. 勾選「I have read and agree to the terms of the AWS Customer Agreement」

4. 點擊「Continue (Step 2 of 5)」

---

### 步驟 5：綁定信用卡（Step 5: Payment Information）

![待補：信用卡綁定頁面](images/placeholder_01_payment_en.webp)

1. 填寫信用卡資訊：
   - **Card number**：信用卡號碼
   - **Expiration date**：到期年月
   - **Cardholder's name**：信用卡持卡人姓名（與卡面一致）

2. 填寫帳單地址「Billing address」

3. 點擊「Verify and Continue (Step 3 of 5)」

4. ⚠️ AWS 會扣款 **$1 USD** 進行驗證，**此款項會於幾天內退還**，屬於正常流程

---

### 步驟 6：手機驗證（Step 6: Phone Verification）

![待補：手機驗證頁面](images/placeholder_01_phone_en.webp)

1. 選擇驗證方式：
   - **Text message (SMS)**：簡訊（推薦）
   - Voice call：語音電話

2. 輸入手機號碼（台灣格式：`+886 912345678`，去掉開頭的 0）

3. 輸入頁面上顯示的驗證圖形文字（CAPTCHA）

4. 點擊「Send SMS」

5. 收到 SMS 後，輸入 4〜6 位數驗證碼

6. 點擊「Continue (Step 4 of 5)」

---

### 步驟 7：選擇 Support Plan（Step 7: Support Plan）

![待補：Support Plan 選擇頁](images/placeholder_01_support_plan_en.webp)

1. 選擇「Basic support - Free」（免費方案，一般初期使用已足夠）

2. 點擊「Complete sign up」

3. 等待畫面顯示「Congratulations! Your AWS account is now activated.」即代表完成

---

### 步驟 8：登入 Console，確認 Region（Step 8: Login & Region Check）

![待補：AWS Console 首頁](images/placeholder_01_console_en.webp)

1. 前往 `https://console.aws.amazon.com`，以 Root user email 登入

2. 登入後，右上角會顯示目前的 Region（區域）

3. 點擊 Region 下拉選單，建議選擇：
   - 🇯🇵 **ap-northeast-1（東京）**：台灣連線速度較佳
   - 🇺🇸 **us-east-1（維吉尼亞北部）**：部分服務首選區域

4. 記錄您選擇的 Region，後續部署會用到

---

### 步驟 9：啟用 Root MFA（Step 9: Enable Root MFA — 重要 / Critical）

> 🔐 **強烈建議**：Root 帳號若沒有 MFA，被盜後損失難以估計。請務必在此步驟完成！

![待補：IAM Security Credentials 頁面](images/placeholder_01_mfa_iam_en.webp)

1. 在 Console 右上角，點擊您的帳號名稱 → 選「Security credentials」

2. 往下捲到「Multi-factor authentication (MFA)」區塊

3. 點擊「Assign MFA device」

4. 選擇裝置類型：**Authenticator app**（推薦 Authy 或 Google Authenticator）

5. 依畫面指示：
   - 在手機安裝 Authy 或 Google Authenticator
   - 用 App 掃描畫面上的 QR Code
   - 連續輸入 2 組 6 位數 OTP 碼確認綁定

6. 點擊「Add MFA」，看到成功提示即完成

---

## 完成後請回報 / Deliverables to Send Us

完成後請把以下資訊用安全管道（1Password / Bitwarden 共享、ProtonMail 加密 email）傳給我們：

- **AWS Account ID（12 碼）**
  - 取得方式：登入 Console → 右上角點帳號名稱 → 「Account」→ 看「Account ID」欄位
  - 格式範例：`123456789012`

> ⛔ **請勿傳送**：Root 帳號的 email、密碼、MFA 設定。我們只需要 Account ID。

---

## 檢核清單 / Checklist

助理操作完後，請逐項打勾，再將本文件（含勾選狀態）傳給我們：

- [ ] 已確認使用 `aws.amazon.com`（網址無 `.cn`）
- [ ] 已完成 Email 驗證
- [ ] 已填寫信用卡資訊（$1 驗證扣款正常）
- [ ] 已完成手機 SMS 驗證
- [ ] 已選擇 **Basic support - Free** 方案
- [ ] 已成功登入 AWS Console
- [ ] 已確認並記錄使用的 Region（ap-northeast-1 東京 / us-east-1 維吉尼亞）
- [ ] 已啟用 Root 帳號 MFA（TOTP / Authenticator App）
- [ ] 已將 **AWS Account ID（12 碼）** 透過安全管道傳給我方

---

## 常見問題 / FAQ

**Q：信用卡刷不過怎麼辦？(Credit card declined?)**
A：確認信用卡有開通「網路交易」及「外幣交易」功能，聯絡發卡銀行開通後再試。部分預付卡（儲值卡）不支援，建議改用實體 VISA 或 Mastercard。

**Q：不小心進入中國區（.cn）了怎麼辦？(Accidentally entered AWS China?)**
A：立即關閉視窗，不要填寫任何資料。重新開啟瀏覽器，輸入 `https://aws.amazon.com` 確認網址正確。

**Q：收不到 Email 驗證碼怎麼辦？(Didn't receive verification email?)**
A：檢查垃圾信件夾（Spam / Junk）。等待 5 分鐘後點擊「Resend email」。若仍未收到，確認 email 地址輸入正確。

**Q：$1 扣款後沒退還怎麼辦？(The $1 charge wasn't refunded?)**
A：通常 3〜5 個工作天退還，若超過 7 天仍未退，聯絡 AWS Support 或信用卡發卡行確認。

**Q：忘記密碼怎麼辦？(Forgot password?)**
A：前往 `https://signin.aws.amazon.com`，點擊「Forgot your password?」，以 Root user email 收取重設連結。

**Q：沒有 Authenticator App 可以跳過 MFA 嗎？(Can I skip MFA?)**
A：技術上可以跳過，但**強烈不建議**。Root 帳號無 MFA 等同於將全部 AWS 資源暴露在風險中。請先安裝 Authy（免費）再繼續。

---

## 出問題時 / If Something Goes Wrong

聯絡：**lifetreemastery@gmail.com**

請附上：
1. 錯誤訊息截圖（完整畫面，含網址列）
2. 操作步驟描述（卡在哪一步）
3. 使用的瀏覽器及作業系統

---

## 待補截圖 / Pending Screenshots (Console Pages)

以下頁面需登入後操作，將由助理實際操作時截圖補充：

| Placeholder 檔名 | 說明 |
|-----------------|------|
| `placeholder_01_password_en.webp` | 步驟 3：密碼設定頁面 |
| `placeholder_01_account_type_en.webp` | 步驟 4：帳號類型選擇頁 |
| `placeholder_01_payment_en.webp` | 步驟 5：信用卡綁定頁面 |
| `placeholder_01_phone_en.webp` | 步驟 6：手機驗證頁面 |
| `placeholder_01_support_plan_en.webp` | 步驟 7：Support Plan 選擇頁 |
| `placeholder_01_console_en.webp` | 步驟 8：AWS Console 首頁（Region 選擇）|
| `placeholder_01_mfa_iam_en.webp` | 步驟 9：IAM Security Credentials / MFA 設定頁 |
