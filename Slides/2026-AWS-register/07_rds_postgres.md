# 07 - 建立 RDS PostgreSQL 資料庫 / Create RDS PostgreSQL Database

> ⚠️ **重要警告 / Critical Warning**
> 本教學僅適用 AWS Global(`aws.amazon.com`)。
> 若註冊頁出現「中國區 / 由光環新網或西雲營運 / Sinnet / NWCD」字樣,請立即關閉重來。
> This guide applies to AWS Global only. Close and restart if you see "China region / operated by Sinnet or NWCD".

---

## 預估 / Estimate

- 時間 (Time):約 20 分鐘(建立後等待約 10 分鐘)
- 費用 (Cost):
  - **免費方案 (Free Tier)**:db.t4g.micro,第一年每月 750 小時免費
  - **正式環境 (Production)**:db.t4g.micro 約 USD $15 / 月、db.t4g.small 約 USD $30 / 月
  - 另加儲存費用:20 GB gp3 ≈ USD $2.30 / 月
- 需準備 (Prerequisites):
  - AWS 帳號已建立(參閱 01 篇)
  - EC2 執行個體已建立於相同 Region(參閱 05 篇)
  - 已知 EC2 使用的 VPC 和 Security Group 名稱
  - 手邊有隨機密碼產生器(建議用 1Password 或 Bitwarden 的內建產生器)

---

## 名詞快查 / Glossary

| 中文 | English | 說明 |
|------|---------|------|
| 關聯式資料庫服務 | RDS (Relational Database Service) | AWS 管理型資料庫服務,自動備份、更新 |
| 執行個體 | Instance | 一台資料庫伺服器 |
| 執行個體類型 | Instance Type | 資料庫的規格(CPU / 記憶體) |
| 虛擬私有雲 | VPC (Virtual Private Cloud) | 隔離的虛擬網路,EC2 和 RDS 須在同一 VPC |
| 安全群組 | Security Group | 防火牆規則,控制哪些 IP / 服務可連入 |
| 端點 | Endpoint | 連接資料庫的網址(xxxxx.rds.amazonaws.com) |
| 公開存取 | Public Access | 是否允許網際網路直接連入資料庫 |
| 備份保留期 | Backup Retention | 自動備份保存天數 |
| 免費方案 | Free Tier | 新帳號前 12 個月的免費用量 |
| gp3 | gp3 | AWS 通用 SSD 儲存類型 |

---

## 服務介紹 / Service Overview

Amazon RDS for PostgreSQL 是 AWS 提供的全受管 PostgreSQL 資料庫服務,無需自行安裝、維護資料庫軟體。

![RDS for PostgreSQL 中文介紹](images/07_rds_product_zh.webp)
![RDS for PostgreSQL English Overview](images/07_rds_product_en.webp)

![RDS 定價頁(中文)](images/07_rds_pricing_zh.webp)
![RDS Pricing Page (English)](images/07_rds_pricing_en.webp)

---

## 操作步驟 / Steps

### 步驟 1:進入 RDS 控制台 (Step 1: Open RDS Console)

1. 開啟瀏覽器,前往 `https://console.aws.amazon.com/rds/`
2. 確認右上角區域 (Region) 與您的 EC2 **相同**
   - 例:EC2 在「亞太地區(東京)(ap-northeast-1)」,RDS 也要選東京
3. 點擊左側選單「資料庫 (Databases)」
4. 點擊「建立資料庫 (Create database)」按鈕

![待補:RDS 控制台首頁 — 點擊 Create database (zh)](images/placeholder_07_rds_console_zh.webp)
![待補:RDS Console — Create database button (en)](images/placeholder_07_rds_console_en.webp)

---

### 步驟 2:選擇資料庫建立方式 (Step 2: Choose Creation Method)

1. 選擇「標準建立 (Standard create)」
   - 不要選「輕鬆建立 (Easy create)」,選項較少無法精細設定

![待補:Standard create 選項 (zh)](images/placeholder_07_rds_create_method_zh.webp)
![待補:Standard create option (en)](images/placeholder_07_rds_create_method_en.webp)

---

### 步驟 3:選擇資料庫引擎 (Step 3: Select Database Engine)

1. 引擎類型 (Engine type) 選擇「PostgreSQL」
2. 引擎版本 (Engine version) 選擇最新的 **PostgreSQL 16.x**
   - 畫面會列出多個版本,選清單最上方(版本號最高)的 16.x

![待補:選擇 PostgreSQL 引擎與版本 (zh)](images/placeholder_07_rds_engine_zh.webp)
![待補:PostgreSQL engine and version selection (en)](images/placeholder_07_rds_engine_en.webp)

---

### 步驟 4:選擇範本 (Step 4: Select Template)

依使用情境選擇:

| 情境 | 範本 (Template) | 說明 |
|------|----------------|------|
| 測試 / 第一年免費 | **免費方案 (Free tier)** | 12 個月內 db.t4g.micro 免費 |
| 正式上線 | **生產 (Production)** | 啟用多可用區域 (Multi-AZ) 高可用性 |

> 💡 建議第一次先選「免費方案」測試,確認部署成功後再升級為「生產」。

![待補:Template 選擇畫面 (zh)](images/placeholder_07_rds_template_zh.webp)
![待補:Template selection (en)](images/placeholder_07_rds_template_en.webp)

---

### 步驟 5:設定資料庫識別碼與帳號 (Step 5: Configure Identifier and Credentials)

1. **資料庫執行個體識別碼 (DB instance identifier)**:填入
   ```
   lattice-cast-pg
   ```
2. **主使用者名稱 (Master username)**:填入
   ```
   lattice_admin
   ```
3. **主密碼 (Master password)**:
   - 點擊「自動產生密碼 (Auto generate a password)」**不勾選**
   - 手動填入一組 **16 碼隨機密碼**
   - 建議使用 1Password / Bitwarden 產生:大小寫英數 + 特殊字元
   - ⚠️ **立即儲存密碼到 1Password / Bitwarden,之後不會再顯示**
4. **確認密碼 (Confirm master password)**:再輸入一次相同密碼

![待補:DB identifier 和 credentials 設定 (zh)](images/placeholder_07_rds_credentials_zh.webp)
![待補:DB identifier and credentials setup (en)](images/placeholder_07_rds_credentials_en.webp)

---

### 步驟 6:選擇執行個體規格 (Step 6: Choose Instance Type)

1. **DB 執行個體類型 (DB instance class)**:
   - 點選「高載類別 (Burstable classes)」
   - 下拉選擇「**db.t4g.micro**」(免費方案 / 測試)或「**db.t4g.small**」(正式)
2. **儲存類型 (Storage type)**:選「gp3」
3. **分配儲存空間 (Allocated storage)**:填入 `20` GB
4. **儲存自動擴展 (Storage autoscaling)**:可保持預設開啟,上限建議設 `100` GB

![待補:Instance type 和 storage 設定 (zh)](images/placeholder_07_rds_instance_zh.webp)
![待補:Instance type and storage settings (en)](images/placeholder_07_rds_instance_en.webp)

---

### 步驟 7:設定連線與 VPC (Step 7: Configure Connectivity)

> ⚠️ **關鍵步驟**:VPC 必須與您的 EC2 相同,否則無法連線。

1. **計算資源 (Compute resource)**:選「不要連接至 EC2 計算資源 (Don't connect to an EC2 compute resource)」
   - 我們稍後手動設定 Security Group
2. **虛擬私有雲 (VPC)**:
   - 下拉選擇與 EC2 **相同的 VPC**
   - 通常只有一個 VPC,名稱為「Default VPC」或您當初建立 EC2 時選的 VPC
3. **公開存取 (Public access)**:選「**否 (No)**」
   - 資料庫只允許從 EC2 連入,禁止網際網路直接存取
4. **VPC 安全群組 (VPC security group)**:
   - 選「建立新的安全群組 (Create new)」
   - 新安全群組名稱填入:`rds-sg`

![待補:VPC 和 Public access 設定 (zh)](images/placeholder_07_rds_vpc_zh.webp)
![待補:VPC and Public access settings (en)](images/placeholder_07_rds_vpc_en.webp)

---

### 步驟 8:設定資料庫驗證 (Step 8: Database Authentication)

1. **資料庫驗證 (Database authentication)**:選「**密碼驗證 (Password authentication)**」即可

---

### 步驟 9:其他設定 — 初始資料庫名稱 (Step 9: Additional Configuration)

1. 展開「其他設定 (Additional configuration)」
2. **初始資料庫名稱 (Initial database name)**:填入
   ```
   latticecast
   ```
   > ⚠️ 若此處留空,RDS 不會自動建立資料庫,之後需手動建立。
3. **備份保留期間 (Backup retention period)**:設定為 `7` 天
4. **備份視窗 (Backup window)**:保持預設即可
5. **維護視窗 (Maintenance window)**:保持預設即可
6. **刪除保護 (Deletion protection)**:建議勾選「啟用刪除保護 (Enable deletion protection)」,防止誤刪

![待補:Additional configuration — 初始 DB 名稱與備份設定 (zh)](images/placeholder_07_rds_additional_zh.webp)
![待補:Additional configuration — initial DB name and backup (en)](images/placeholder_07_rds_additional_en.webp)

---

### 步驟 10:建立資料庫 (Step 10: Create the Database)

1. 確認所有設定後,捲動到頁面底部
2. 點擊「**建立資料庫 (Create database)**」按鈕
3. 畫面會跳回資料庫清單,狀態顯示「建立中 (Creating)」
4. **等待約 8–10 分鐘**,直到狀態變為「可用 (Available)」
   - 可以先去做其他事,不需要一直盯著畫面

![待補:資料庫建立中 — 狀態 Creating (zh)](images/placeholder_07_rds_creating_zh.webp)
![待補:Database status — Creating (en)](images/placeholder_07_rds_creating_en.webp)

---

### 步驟 11:設定 Security Group 規則 (Step 11: Configure Security Group Inbound Rule)

> 資料庫建立完成後,需要讓 `rds-sg` 只允許 EC2 連入。

1. 前往 EC2 控制台,找到您的 EC2 執行個體
2. 記下 EC2 使用的 **Security Group ID**,格式為 `sg-xxxxxxxxxxxxxxxxx`
3. 回到 RDS → 點擊 `lattice-cast-pg` → 點擊「連線與安全 (Connectivity & security)」標籤
4. 點擊 `rds-sg` 連結,進入 Security Group 設定
5. 點擊「入站規則 (Inbound rules)」→「編輯入站規則 (Edit inbound rules)」
6. 點擊「新增規則 (Add rule)」:
   - **類型 (Type)**:`PostgreSQL`(自動填入 Port 5432)
   - **來源 (Source)**:`Custom`
   - **值**:填入您的 EC2 Security Group ID(`sg-xxxxxxxxxxxxxxxxx`)
7. 點擊「儲存規則 (Save rules)」

![待補:rds-sg inbound rule 設定 — EC2 SG 來源 (zh)](images/placeholder_07_rds_sg_zh.webp)
![待補:rds-sg inbound rule — EC2 SG as source (en)](images/placeholder_07_rds_sg_en.webp)

---

### 步驟 12:取得資料庫端點 (Step 12: Get the Database Endpoint)

1. 前往 RDS → 「資料庫 (Databases)」
2. 點擊「lattice-cast-pg」
3. 在「連線與安全 (Connectivity & security)」標籤找到「端點 (Endpoint)」
4. 複製端點網址,格式如:
   ```
   lattice-cast-pg.xxxxxxxxxx.ap-northeast-1.rds.amazonaws.com
   ```
5. **將端點、Port、DB 名稱、帳號、密碼全數儲存至 1Password / Bitwarden**

![待補:RDS Endpoint 複製位置 (zh)](images/placeholder_07_rds_endpoint_zh.webp)
![待補:RDS Endpoint location (en)](images/placeholder_07_rds_endpoint_en.webp)

---

## 完成後請回報 / Deliverables to Send Us

完成後請把以下資訊用安全管道(**1Password 共用保險庫 / Bitwarden 共用資料夾**)傳給我們:

| 項目 | 值 |
|------|----|
| Endpoint | `xxxxxxxxxx.rds.amazonaws.com` |
| Port | `5432` |
| Database name | `latticecast` |
| Master username | `lattice_admin` |
| Master password | (您設定的 16 碼密碼) |
| AWS Region | 例:ap-northeast-1 |

> ⚠️ **禁止**用 LINE、Email 明文、Slack、Google Doc 傳送以上資訊。
> 請使用 1Password / Bitwarden 共用,或以 ProtonMail 加密寄送。

---

## 檢核清單 / Checklist

助理操作完逐項打勾後回傳本文件:

- [ ] 已確認使用 `aws.amazon.com`(非 .cn)
- [ ] RDS Region 與 EC2 相同
- [ ] 資料庫引擎選擇 PostgreSQL 16.x
- [ ] DB instance identifier 填入 `lattice-cast-pg`
- [ ] Master username 填入 `lattice_admin`
- [ ] Master password 已儲存至 1Password / Bitwarden
- [ ] Instance type 選擇 db.t4g.micro 或 db.t4g.small
- [ ] Storage 設定為 20 GB gp3
- [ ] VPC 與 EC2 相同
- [ ] Public access 設定為「否 (No)」
- [ ] 新建 Security Group `rds-sg`
- [ ] Initial database name 填入 `latticecast`
- [ ] Backup retention 設定為 7 天
- [ ] 已啟用刪除保護 (Deletion protection)
- [ ] 資料庫狀態已變為「可用 (Available)」
- [ ] `rds-sg` Inbound rule 已設定只允許 EC2 Security Group 連入 Port 5432
- [ ] 已取得 Endpoint 並儲存至 1Password / Bitwarden
- [ ] 已將上方「完成後請回報」的資訊傳給我方

---

## 常見問題 / FAQ

**Q: 建立時找不到我的 VPC 怎麼辦?**
A: 確認您選擇的 Region 與 EC2 相同。VPC 和 Subnet 是 Region 限定的,切換到正確 Region 後即可看到。

**Q: 建立後狀態一直是「建立中 (Creating)」超過 20 分鐘?**
A: 屬正常範圍,最久可能需要 15 分鐘。若超過 30 分鐘仍未完成,請截圖聯絡我方。

**Q: 忘記儲存密碼,密碼不見了怎麼辦?**
A: 進入 RDS 資料庫詳情頁 → 右上角「修改 (Modify)」→ 修改 Master password。重設後再存入 1Password。

**Q: 要如何確認 EC2 可以連上 RDS?**
A: 我方部署時會使用 DB endpoint 測試連線,如果 Security Group 設定正確即可連通,不需要您手動測試。

**Q: Free Tier 到期後會怎樣?**
A: 第 13 個月起開始按量計費(db.t4g.micro 約 USD $15 / 月)。建議在 03 篇設定的 Billing Alert 提醒下密切注意帳單。

**Q: 可以把 RDS Public access 設成 Yes 讓我直接用 DBeaver 連嗎?**
A: **不建議**。公開存取會增加資料外洩風險。建議透過 SSH Tunnel 連至 EC2 再轉發至 RDS,或使用 AWS Session Manager。有需要請詢問我方技術人員。

---

## 出問題時 / If Something Goes Wrong

聯絡:lifetreemastery@gmail.com,附上錯誤訊息截圖與以下資訊:
- 目前停在哪個步驟
- 畫面上顯示的錯誤文字或代碼
- 您使用的 AWS Region

---

## 待補截圖 / Pending Screenshots (Console 內頁)

以下截圖需要助理操作時實際截圖後補入:

| Placeholder 檔名 | 說明 |
|-----------------|------|
| `placeholder_07_rds_console_zh.webp` | RDS 控制台首頁 — 點擊 Create database (中文 UI) |
| `placeholder_07_rds_console_en.webp` | RDS Console — Create database button (英文 UI) |
| `placeholder_07_rds_create_method_zh.webp` | Standard create 選項 (中文 UI) |
| `placeholder_07_rds_create_method_en.webp` | Standard create option (英文 UI) |
| `placeholder_07_rds_engine_zh.webp` | 選擇 PostgreSQL 引擎與版本 (中文 UI) |
| `placeholder_07_rds_engine_en.webp` | PostgreSQL engine and version selection (英文 UI) |
| `placeholder_07_rds_template_zh.webp` | Template 選擇畫面 (中文 UI) |
| `placeholder_07_rds_template_en.webp` | Template selection (英文 UI) |
| `placeholder_07_rds_credentials_zh.webp` | DB identifier 和 credentials 設定 (中文 UI) |
| `placeholder_07_rds_credentials_en.webp` | DB identifier and credentials setup (英文 UI) |
| `placeholder_07_rds_instance_zh.webp` | Instance type 和 storage 設定 (中文 UI) |
| `placeholder_07_rds_instance_en.webp` | Instance type and storage settings (英文 UI) |
| `placeholder_07_rds_vpc_zh.webp` | VPC 和 Public access 設定 (中文 UI) |
| `placeholder_07_rds_vpc_en.webp` | VPC and Public access settings (英文 UI) |
| `placeholder_07_rds_additional_zh.webp` | Additional configuration — 初始 DB 名稱與備份設定 (中文 UI) |
| `placeholder_07_rds_additional_en.webp` | Additional configuration — initial DB name and backup (英文 UI) |
| `placeholder_07_rds_creating_zh.webp` | 資料庫建立中 — 狀態 Creating (中文 UI) |
| `placeholder_07_rds_creating_en.webp` | Database status — Creating (英文 UI) |
| `placeholder_07_rds_sg_zh.webp` | rds-sg inbound rule 設定 — EC2 SG 來源 (中文 UI) |
| `placeholder_07_rds_sg_en.webp` | rds-sg inbound rule — EC2 SG as source (英文 UI) |
| `placeholder_07_rds_endpoint_zh.webp` | RDS Endpoint 複製位置 (中文 UI) |
| `placeholder_07_rds_endpoint_en.webp` | RDS Endpoint location (英文 UI) |
