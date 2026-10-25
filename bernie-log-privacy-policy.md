# 개인정보 처리방침 · Privacy Policy

**앱 · App:** 버니기록 (Bernie Log)  
**최종 수정일 · Last updated:** 2026-10-25

[한국어](#한국어) · [English](#english)

---

## 한국어

버니기록은 사진이 언제, 어디서 찍혔는지를 읽어 여행과 장소별로 정리해 주는 앱입니다. 광고나 분석 도구를 사용하지 않으며, 개인정보를 판매하지 않습니다.

### 1. 기기 안에서 처리하는 정보

- **사진:** 갤러리의 사진은 갤러리에 그대로 있습니다. 앱은 사진의 촬영 시각과 위치(사진에 기록된 GPS 정보)를 읽어 기기 안의 데이터베이스에 저장합니다.
- **카메라와 위치:** 앱의 카메라로 찍을 때, 사진에 촬영 위치를 남기기 위해 현재 위치를 사용합니다.
- **영수증 글자 인식:** 영수증 사진의 글자는 기기 안에서 인식합니다.

### 2. 기기 밖으로 보내는 정보

- **장소 이름:** 사진의 위치(좌표)를 휴대폰의 위치 서비스(Android에서는 Google)에 보내 도시와 지역 이름을 받아옵니다.
- **지도:** 지도를 보여 줄 때 Google 지도를 사용합니다.
- **영수증 읽기:** 영수증을 스캔하면, 기기에서 인식한 영수증의 **글자**와 사진의 촬영 날짜·시각·국가를 Google Gemini API에 보내 가게 이름, 금액, 품목을 읽어옵니다. **사진 자체는 보내지 않습니다.**
- **가게 위치 찾기:** 영수증의 가게 이름과 주소, 사진의 촬영 위치를 버니기록 서버를 거쳐 Google Places API에 보내 지도에 가게를 표시합니다.

### 3. 계정과 백업 (선택)

계정 없이도 앱을 모두 쓸 수 있습니다. 계정을 만들면:

- **계정 정보:** 사용자 이름과 비밀번호(원래 비밀번호를 알 수 없는 해시로만 저장), 또는 Google로 로그인할 경우 Google 계정의 이름, 이메일 주소, 고유 ID를 저장합니다.
- **백업 데이터:** 기기 간 동기화와 백업을 위해 기록(사진의 촬영 시각과 위치, 여행, 영수증 내용)과 사진 파일을 버니기록 서버에 저장합니다.

### 4. 정보 이용 목적

사진을 여행과 장소로 정리하고, 영수증을 읽고, 여러 기기에서 같은 기록을 보여 주고, 백업하기 위해서만 사용합니다.

### 5. 제3자 서비스

- **Google 로그인** — 인증
- **Google 지도, Google Places API** — 지도와 가게 위치
- **Google Gemini API** — 영수증 글자 읽기
- **휴대폰 위치 서비스(Android: Google)** — 장소 이름

각 서비스의 처리는 [Google 개인정보처리방침](https://policies.google.com/privacy)을 따릅니다.

### 6. 보관 기간과 삭제

- 기기 안의 기록은 앱을 지우면 함께 삭제됩니다. 갤러리의 사진은 지워지지 않습니다.
- 서버의 계정과 백업은 계정이 있는 동안 보관합니다. 앱의 **설정 › 계정 › 계정 삭제**에서 계정과 백업을 바로 삭제할 수 있으며, 아래 이메일로 요청할 수도 있습니다.

### 7. 아동 개인정보 보호

이 앱은 만 13세 미만 아동을 대상으로 하지 않으며, 만 13세 미만 아동의 개인정보를 알면서 수집하지 않습니다.

### 8. 방침 변경

방침이 바뀌면 이 페이지에 수정일과 함께 알립니다.

### 9. 문의

**이메일:** ankylos.bernie@gmail.com

---

## English

Bernie Log reads when and where your photos were taken and groups them into trips and places. It uses no ads or analytics, and never sells personal information.

### 1. What stays on your phone

- **Photos:** Your gallery photos stay in your gallery. The app reads when and where each was taken (its recorded GPS location) and keeps that in a database on your phone.
- **Camera and location:** When you take a photo with the app's camera, it uses your current location to record where the photo was taken.
- **Receipt text recognition:** The text on a receipt photo is recognized on your phone.

### 2. What leaves your phone

- **Place names:** Photo locations (coordinates) are sent to your phone's location service (Google, on Android) to get city and area names.
- **Maps:** Maps are shown with Google Maps.
- **Reading receipts:** When you scan a receipt, the receipt's **text**, recognized on your phone, is sent with the photo's date, time and country to the Google Gemini API to read the store, amounts and items. **The photo itself is never sent.**
- **Finding stores:** A receipt's store name and address, with where the photo was taken, are sent through the Bernie Log server to the Google Places API to show the store on the map.

### 3. Account and backup (optional)

You can use the whole app without an account. If you create one:

- **Account details:** your username and password (stored only as a one-way hash), or, when you sign in with Google, your Google account's name, email address and unique ID.
- **Backup:** to sync between your devices and keep a backup, your timeline (when and where photos were taken, trips, receipt details) and your photo files are stored on the Bernie Log server.

### 4. How information is used

Only to group your photos into trips and places, read your receipts, show the same timeline on your devices, and back it up.

### 5. Third-party services

- **Google Sign-In** — sign-in
- **Google Maps and the Google Places API** — maps and store locations
- **Google Gemini API** — reading receipt text
- **Your phone's location service (Google, on Android)** — place names

These services handle data under the [Google Privacy Policy](https://policies.google.com/privacy).

### 6. Keeping and deleting data

- Everything on your phone is deleted when you uninstall the app. Your gallery photos are not.
- Your account and backup on the server are kept while you have an account. Delete both at once in the app under **Settings › Account › Delete account**, or ask by email below.

### 7. Children

The app is not meant for children under 13, and does not knowingly collect personal information from them.

### 8. Changes

Changes to this policy are posted on this page with a new date.

### 9. Contact

**Email:** ankylos.bernie@gmail.com
