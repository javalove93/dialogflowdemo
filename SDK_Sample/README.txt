Dialogflow API를 사용하려면 Google Cloud의 Service Account를 생성해서 권한부여를 해야 함

- http://console.cloud.google.com
- IAM & Admin
- Service Accounts
- Create Service Account
- Role에서 Dialogflow / Dialogflow API Admin 추가
- 생성된 Service Account에서 Create Key하여 JSON 파일 다운로드
- 다음과 같이 환경변수 지정
  export GOOGLE_APPLICATION_CREDENTIALS="/home/jerryj/google/dialogflow_api/ShoppingMallDemo-3630d931979e.json"
- GCP Console에서 Dialogflow API 활성화
- Python Dialogflow API 설치: pip install dialogflow
