# Let's save the user's provided JSON to inspect it
user_json = """[
  {
    "id": 1794990537590,
    "zone": "METCON",
    "name": "리그 & 랙 설치비",
    "price": 1000000,
    "qty": 1,
    "note": ""
  },
  {
    "id": 1794990523987,
    "zone": "METCON",
    "name": "타이머 삼각대",
    "price": 34000,
    "qty": 1,
    "note": ""
  },
  {
    "id": 1794990427498,
    "zone": "METCON",
    "name": "타이머",
    "price": 190000,
    "qty": 2,
    "note": ""
  },
  {
    "id": 1794990404876,
    "zone": "METCON",
    "name": "줄넘기/밴드 정리대",
    "price": 80000,
    "qty": 2,
    "note": ""
  },
  {
    "id": 1794990319987,
    "zone": "METCON",
    "name": "짐네스틱 RING",
    "price": 50000,
    "qty": 4,
    "note": ""
  },
  {
    "id": 1794990106326,
    "zone": "METCON",
    "name": "줄넘기(기본)",
    "price": 24000,
    "qty": 20,
    "note": ""
  },
  {
    "id": 1794989948034,
    "zone": "METCON",
    "name": "풀업밴드(레드)",
    "price": 5000,
    "qty": 20,
    "note": ""
  },
  {
    "id": 1794989937911,
    "zone": "METCON",
    "name": "풀업밴드(블랙)",
    "price": 7000,
    "qty": 10,
    "note": ""
  },
  {
    "id": 1794989927387,
    "zone": "METCON",
    "name": "풀업밴드(퍼플)",
    "price": 9000,
    "qty": 14,
    "note": ""
  },
  {
    "id": 1794989900678,
    "zone": "METCON",
    "name": "풀업밴드(그린)",
    "price": 13000,
    "qty": 14,
    "note": ""
  },
  {
    "id": 1794989889241,
    "zone": "METCON",
    "name": "풀업밴드(블루)",
    "price": 18000,
    "qty": 4,
    "note": ""
  },
  {
    "id": 1794989835650,
    "zone": "METCON",
    "name": "마사지볼(라크라스볼)",
    "price": 4500,
    "qty": 30,
    "note": ""
  },
  {
    "id": 1794989795539,
    "zone": "METCON",
    "name": "폼롤러(33cm)",
    "price": 12000,
    "qty": 24,
    "note": ""
  },
  {
    "id": 1794989755867,
    "zone": "METCON",
    "name": "요가매트",
    "price": 30000,
    "qty": 24,
    "note": ""
  },
  {
    "id": 1794989699420,
    "zone": "METCON",
    "name": "월볼 30LB",
    "price": 64000,
    "qty": 8,
    "note": ""
  },
  {
    "id": 1794989681198,
    "zone": "METCON",
    "name": "월볼 20LB",
    "price": 58000,
    "qty": 14,
    "note": ""
  },
  {
    "id": 1794989669530,
    "zone": "METCON",
    "name": "월볼 14LB",
    "price": 52000,
    "qty": 16,
    "note": ""
  },
  {
    "id": 1794989594741,
    "zone": "METCON",
    "name": "월볼 10LB",
    "price": 49000,
    "qty": 14,
    "note": ""
  },
  {
    "id": 1794989582521,
    "zone": "METCON",
    "name": "월볼 6LB",
    "price": 45000,
    "qty": 8,
    "note": ""
  },
  {
    "id": 1794989565432,
    "zone": "METCON",
    "name": "월볼 4LB",
    "price": 43000,
    "qty": 6,
    "note": ""
  },
  {
    "id": 1794989537353,
    "zone": "METCON",
    "name": "케틀벨 32kg",
    "price": 120000,
    "qty": 6,
    "note": ""
  },
  {
    "id": 1794989525317,
    "zone": "METCON",
    "name": "케틀벨 24kg",
    "price": 83000,
    "qty": 8,
    "note": ""
  },
  {
    "id": 1794989506575,
    "zone": "METCON",
    "name": "케틀벨 20kg",
    "price": 69000,
    "qty": 10,
    "note": ""
  },
  {
    "id": 1794989481764,
    "zone": "METCON",
    "name": "케틀벨 16kg",
    "price": 55000,
    "qty": 12,
    "note": ""
  },
  {
    "id": 1794989465850,
    "zone": "METCON",
    "name": "케틀벨 12kg",
    "price": 41000,
    "qty": 10,
    "note": ""
  },
  {
    "id": 1794989452436,
    "zone": "METCON",
    "name": "케틀벨 8kg",
    "price": 28000,
    "qty": 10,
    "note": ""
  },
  {
    "id": 1794989435370,
    "zone": "METCON",
    "name": "케틀벨 4kg",
    "price": 14000,
    "qty": 4,
    "note": ""
  },
  {
    "id": 1794989346469,
    "zone": "METCON",
    "name": "덤벨 50LB",
    "price": 78000,
    "qty": 10,
    "note": ""
  },
  {
    "id": 1794989319619,
    "zone": "METCON",
    "name": "덤벨 40LB",
    "price": 62000,
    "qty": 14,
    "note": ""
  },
  {
    "id": 1794989300757,
    "zone": "METCON",
    "name": "덤벨 35LB",
    "price": 55000,
    "qty": 16,
    "note": ""
  },
  {
    "id": 1794989288645,
    "zone": "METCON",
    "name": "덤벨 30LB",
    "price": 47000,
    "qty": 14,
    "note": ""
  },
  {
    "id": 1794989275294,
    "zone": "METCON",
    "name": "덤벨 25LB",
    "price": 39000,
    "qty": 14,
    "note": ""
  },
  {
    "id": 1794989261245,
    "zone": "METCON",
    "name": "덤벨 20LB",
    "price": 31000,
    "qty": 14,
    "note": ""
  },
  {
    "id": 1794989248479,
    "zone": "METCON",
    "name": "덤벨 15LB",
    "price": 24000,
    "qty": 14,
    "note": ""
  },
  {
    "id": 1794989233095,
    "zone": "METCON",
    "name": "덤벨 10LB",
    "price": 16000,
    "qty": 12,
    "note": ""
  },
  {
    "id": 1794989210035,
    "zone": "METCON",
    "name": "덤벨 5LB",
    "price": 8000,
    "qty": 6,
    "note": ""
  },
  {
    "id": 107,
    "zone": "METCON",
    "name": "고무매트 바닥재 (1m×1m×2.5cm)",
    "price": 35000,
    "qty": 360,
    "note": "METCON ZONE 고무매트"
  },
  {
    "id": 109,
    "zone": "METCON",
    "name": "맞춤형 트윈 사각 스테이션 RIG (각 7.2m×1.8m 2세트)",
    "price": 16000000,
    "qty": 1,
    "note": "G4~G5, G5~G6 사이 2세트 배치 · [셀1.2m+긴바1.8m+셀1.2m+긴바1.8m+셀1.2m] · 총 6스쿼트셀 (기둥간섭 0%)"
  },
  {
    "id": 110,
    "zone": "METCON",
    "name": "대형 스토리지 랙 (2850*500*2000)",
    "price": 1800000,
    "qty": 4,
    "note": "장비 및 메디신볼/소도구 전용 랙"
  },
  {
    "id": 112,
    "zone": "METCON",
    "name": "바벨 정리대 (9홀)",
    "price": 140000,
    "qty": 4,
    "note": "바벨 40자루 거치대 (3호점 실단가)"
  },
  {
    "id": 113,
    "zone": "METCON",
    "name": "GHD (Glute Ham Developer)",
    "price": 540000,
    "qty": 2,
    "note": "하체 및 코어 훈련 머신 (3호점 실단가)"
  },
  {
    "id": 115,
    "zone": "METCON",
    "name": "역도 블럭 (Drop Block)",
    "price": 375000,
    "qty": 2,
    "note": "역도 클린/스내치 부분 훈련 블럭 (3호점 실단가)"
  },
  {
    "id": 116,
    "zone": "METCON",
    "name": "딥스 어태치먼트 바",
    "price": 95000,
    "qty": 2,
    "note": "리그 장착형 딥스 바 (3호점 실단가)"
  },
  {
    "id": 117,
    "zone": "METCON",
    "name": "로프 클라임 로프",
    "price": 75000,
    "qty": 6,
    "note": ""
  },
  {
    "id": 118,
    "zone": "METCON",
    "name": "포디움 바벨 20KG (남성용)",
    "price": 220000,
    "qty": 12,
    "note": "탄력바 (포디움 23년 기준)"
  },
  {
    "id": 119,
    "zone": "METCON",
    "name": "포디움 바벨 15KG (여성용)",
    "price": 200000,
    "qty": 12,
    "note": "탄력바 (포디움 23년 기준)"
  },
  {
    "id": 120,
    "zone": "METCON",
    "name": "스킬바벨 7.5KG (초심자용)",
    "price": 110000,
    "qty": 10,
    "note": "탄력바 (포디움 23년 기준)"
  },
  {
    "id": 121,
    "zone": "METCON",
    "name": "철제 마구리 (쌍)",
    "price": 16000,
    "qty": 30,
    "note": "기본 철제 마구리"
  },
  {
    "id": 122,
    "zone": "METCON",
    "name": "보급형 범퍼 플레이트 45lb",
    "price": 77000,
    "qty": 30,
    "note": "Xpodium 우레탄/고무 범퍼 플레이트 (3호점 실단가)"
  },
  {
    "id": 123,
    "zone": "METCON",
    "name": "보급형 범퍼 플레이트 35lb",
    "price": 70000,
    "qty": 20,
    "note": "Xpodium 우레탄/고무 범퍼 플레이트 (3호점 실단가)"
  },
  {
    "id": 124,
    "zone": "METCON",
    "name": "보급형 범퍼 플레이트 25lb",
    "price": 54000,
    "qty": 50,
    "note": "Xpodium 우레탄/고무 범퍼 플레이트 (3호점 실단가)"
  },
  {
    "id": 125,
    "zone": "METCON",
    "name": "보급형 범퍼 플레이트 15lb",
    "price": 40000,
    "qty": 60,
    "note": "Xpodium 우레탄/고무 범퍼 플레이트 (3호점 실단가)"
  },
  {
    "id": 126,
    "zone": "METCON",
    "name": "보급형 범퍼 플레이트 10lb",
    "price": 35000,
    "qty": 60,
    "note": "Xpodium 우레탄/고무 범퍼 플레이트 (3호점 실단가)"
  },
  {
    "id": 127,
    "zone": "METCON",
    "name": "보급형 플레이트 5lb",
    "price": 25000,
    "qty": 20,
    "note": "저중량 플레이트 (3호점 실단가)"
  },
  {
    "id": 128,
    "zone": "METCON",
    "name": "보급형 플레이트 2.5lb",
    "price": 20000,
    "qty": 12,
    "note": "미세 중량 조절용 플레이트 (3호점 실단가)"
  },
  {
    "id": 133,
    "zone": "METCON",
    "name": "나무 점핑박스 (40*50*60)",
    "price": 80000,
    "qty": 10,
    "note": "우드 플라이오메트릭 박스 (3호점 실단가)"
  },
  {
    "id": 1794990185367,
    "zone": "METCON",
    "name": "나무 점핑박스 (50*60*70)",
    "price": 90000,
    "qty": 15,
    "note": ""
  },
  {
    "id": 136,
    "zone": "METCON",
    "name": "AB MAT (일반)",
    "price": 17000,
    "qty": 30,
    "note": ""
  },
  {
    "id": 137,
    "zone": "METCON",
    "name": "화물 통합 운송비",
    "price": 3500000,
    "qty": 1,
    "note": "지하 1층 하역"
  },
  {
    "id": 114,
    "zone": "ROX",
    "name": "각도조절 벤치",
    "price": 250000,
    "qty": 6,
    "note": "상체 및 프리웨이트 인클라인 벤치 (3호점 실단가)"
  },
  {
    "id": 1794990380831,
    "zone": "ROX",
    "name": "평 벤치",
    "price": 150000,
    "qty": 6,
    "note": ""
  },
  {
    "id": 1794990691981,
    "zone": "ROX",
    "name": "샌드백 30KG",
    "price": 93000,
    "qty": 5,
    "note": ""
  },
  {
    "id": 1794990680093,
    "zone": "ROX",
    "name": "샌드백 20KG",
    "price": 78000,
    "qty": 10,
    "note": ""
  },
  {
    "id": 1794990658523,
    "zone": "ROX",
    "name": "샌드백 10KG",
    "price": 77000,
    "qty": 10,
    "note": ""
  },
  {
    "id": 1794990569210,
    "zone": "ROX",
    "name": "월볼타겟",
    "price": 140000,
    "qty": 12,
    "note": ""
  },
  {
    "id": 1794988474475,
    "zone": "ROX",
    "name": "고무매트 바닥재 (1m×1m×2.5cm)",
    "price": 35000,
    "qty": 120,
    "note": ""
  },
  {
    "id": 105,
    "zone": "ROX",
    "name": "하이록스 Sled",
    "price": 350000,
    "qty": 6,
    "note": "좌측 3대 + 우측 3대 동시 출발 (12.5m 편도 × 2구간 6대 동시 운영)"
  },
  {
    "id": 106,
    "zone": "ROX",
    "name": "29m 3레인 직선 썰매 전용 인조잔디 트랙 (Turf)",
    "price": 40000,
    "qty": 87,
    "note": "폭 3.0m × 길이 29.0m (87m² · 좌우 터닝 1m + 12.5m×2 + 중앙 터닝 2m)"
  },
  {
    "id": 104,
    "zone": "ERG",
    "name": "무동력 트레드밀",
    "price": 2900000,
    "qty": 6,
    "note": "남측 에르그 라인 우측 6대(길이 175cm) 북측 운동구역 향 배치"
  },
  {
    "id": 101,
    "zone": "ERG",
    "name": "컨셉2 로잉머신 (RowErg PM5)",
    "price": 169000,
    "qty": 10,
    "note": "북서 사선벽 수납랙 우측 끝 10대 직립 보관 (3호점 실단가)"
  },
  {
    "id": 103,
    "zone": "ERG",
    "name": "컨셉2 스키에르그 (SkiErg)",
    "price": 1890000,
    "qty": 6,
    "note": "남측 에르그 라인 좌측 6대 북측 운동구역 향 배치 (3호점 실단가)"
  },
  {
    "id": 102,
    "zone": "ERG",
    "name": "컨셉2 바이크에르그 (BikeErg)",
    "price": 1890000,
    "qty": 4,
    "note": "기둥 G4 좌측 4대 배치 (남측 ROX·터프 조망 · 3호점 실단가)"
  },
  {
    "id": 201,
    "zone": "LOUNGE",
    "name": "오픈 가방 큐비클랙 (2.0m · 서측 상단 소지품 수납장)",
    "price": 450000,
    "qty": 1,
    "note": "탈의실 미이용 회원 가방·소지품 오픈 수납장 (깊이 0.45m × 길이 2.0m)"
  },
  {
    "id": 202,
    "zone": "LOUNGE",
    "name": "회원 신발장 & 40cm 돌출 플린스 착석 벤치 일체형 (2.0m)",
    "price": 650000,
    "qty": 1,
    "note": "서측 벽 일일 오픈형 신발장 및 40cm 돌출 착석 벤치 일체형"
  },
  {
    "id": 203,
    "zone": "LOUNGE",
    "name": "셀프 프로틴바 카운터 & 언더싱크 수전·제빙기·쇼케이스 (1.7m)",
    "price": 1200000,
    "qty": 1,
    "note": "동측 상단 화장실 배관 직결 · 정수기·제빙기·싱크·냉장 쇼케이스"
  },
  {
    "id": 204,
    "zone": "LOUNGE",
    "name": "모놀리식 콘크리트 아일랜드 리셉션 데스크 (1.8×0.75m) & 출석 태블릿·스툴",
    "price": 950000,
    "qty": 1,
    "note": "동측 중단 아일랜드 데스크 · 출석 태블릿·방문객 스툴 2석·스태프 체어"
  },
  {
    "id": 205,
    "zone": "LOUNGE",
    "name": "오픈 MD 리테일 진열장 (1.8m) & 남측 코너 미니멀 전신거울",
    "price": 550000,
    "qty": 1,
    "note": "동측 하단 전면 개방형 의류·보충제 진열장 및 남측 코너 전신거울"
  },
  {
    "id": 206,
    "zone": "LOUNGE",
    "name": "ㄱ자 일체형 빌트인 플린스 벤치 소파 (서측 2.6m + 남측 4.2m)",
    "price": 2200000,
    "qty": 1,
    "note": "8~10인 수용 가능한 연속 빌트인 플린스 벤치 소파 (등받이 쿠션 포함)"
  },
  {
    "id": 207,
    "zone": "LOUNGE",
    "name": "카페 사각 테이블 (2세트·체어 4석) & 로우 원형 라운지 테이블 세트",
    "price": 600000,
    "qty": 1,
    "note": "남측 카페 사각 테이블 2세트·체어 4석 + 서측 로우 원형탁자·스툴"
  },
  {
    "id": 302,
    "zone": "INTERIOR",
    "name": "웰컴라운지·복도·화장실·남녀 탈의실·샤워실 일괄 시공 (직영)",
    "price": 1500000,
    "qty": 50,
    "note": "라운지(17.85평)+복도(6.8평)+화장실(8.3평)+남·여 탈의·샤워(각 8.3평) = 실면적 49.6평(약 50평) × 평당 150만원"
  },
  {
    "id": 305,
    "zone": "INTERIOR",
    "name": "운동공간 180평 (도장·전기·배선·조명·간판·사인물·소방 등 일괄)",
    "price": 500000,
    "qty": 180,
    "note": "도장, 전기, 배선, 조명, 간판, 사인물, 소방 등 일괄 (평당 80만원 · 약식으로 기재, 전문가이신 의장님 자문 요망)"
  },
  {
    "id": 401,
    "zone": "MEP",
    "name": "40평형 천장형 시스템 냉난방기 (인버터 4-Way)",
    "price": 30000000,
    "qty": 1,
    "note": "운동공간 40평형 (4대) + 라운지 (1대) + 탈의실 벽걸이 (2대)"
  },
  {
    "id": 403,
    "zone": "MEP",
    "name": "고효율 벽걸이형 순간 가스온수기 (린나이 상업용 병렬 시스템)",
    "price": 1600000,
    "qty": 3,
    "note": "남·여 총 10수전 동시 샤워 시 온수 끊김 방지 3대 병렬 직결 및 가스 배관"
  },
  {
    "id": 404,
    "zone": "MEP",
    "name": "지하 전용 대용량 업소용 제습기 & 대형 에어서큘레이터 세트",
    "price": 700000,
    "qty": 4,
    "note": "하절기 지하 결로·습도 제어용 대용량 제습기 4대 및 공기순환 팬"
  },
  {
    "id": 405,
    "zone": "MEP",
    "name": "JBL 파티박스 음향 앰프",
    "price": 600000,
    "qty": 2,
    "note": "METCON·ROX 듀얼 클래스 고출력 앰프, 스피커 8채널 및 코치용 무선 마이크"
  },
  {
    "id": 406,
    "zone": "MEP",
    "name": "크로스핏(H6) & ROX(G6) 구역별 전용 대형 디지털 타이머·칠판",
    "price": 850000,
    "qty": 2,
    "note": "동측 H6 기둥 벽면(METCON용) 및 G6 벽면(ROX용) 독립 WOD 화이트보드 & LED 타이머"
  },
  {
    "id": 407,
    "zone": "MEP",
    "name": "운영 데스크 PC·출석 체크 태블릿 키오스크 및 오픈 초도 비품",
    "price": 2500000,
    "qty": 1,
    "note": "CRM 연동 출석 태블릿, 운영 PC, 상담 집기, 구급함·초도 운영 물품"
  }
]"""

import json
items = json.loads(user_json)
print(f"Total items in user_json: {len(items)}")

# Check ROX sandbag items:
sandbags = [it for it in items if "샌드백" in it["name"]]
print("Sandbags found:", sandbags)
