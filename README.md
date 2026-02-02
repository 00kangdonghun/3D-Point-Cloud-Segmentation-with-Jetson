This repository contains a tool to train/test models on 3d point cloud segmentation. It is specifically focussed on recongnizing points on a point cloud eg fingertips.
The segementation is done by RandLa-Net. The implementation was based on this repository: [https://github.com/aRI0U/RandLA-Net-pytorch](https://github.com/aRI0U/RandLA-Net-pytorch)

Jetson 기반 임베디드 환경에서 3D Point Cloud Semantic Segmentation을 수행하기 위한 프로젝트입니다.
Intel RealSense D455로 획득한 실제 3D 포인트 클라우드 데이터를 사용하여, RandLa-Net 모델을 학습·추론하고 실시간 시각화까지 구현했습니다.

## 📌 Project Overview
- Task: 3D Point Cloud Semantic Segmentation
- Model: RandLa-Net (CVPR 2020)
- Hardware: NVIDIA Jetson, Intel RealSense D455
- Features:
Custom 3D dataset 직접 레이블링
3D 손 제스처 / 수화 / 얼굴 포인트 인식
Jetson 환경에서 실시간 추론

## 📂 Dataset
본 프로젝트에서는 자체 제작한 Custom 3D Point Cloud Dataset을 사용했습니다.

1️⃣ Count Dataset
- Task: 손가락 개수(1~5) 인식
- Label: Fingertips
- Images: 각 클래스당 5장 (총 26장)
- Purpose: 기본 동작 인식 검증

2️⃣ Sign Language Dataset
- Task: 3D 수화 제스처 인식
- Label: Fingertips + 손가락 방향
- Images: 각 제스처당 3장 + 추가 학습 데이터 (총 111장)
- Purpose: 복잡한 동작 및 방향 변화 대응

3️⃣ Face Dataset
- Task: 얼굴 주요 포인트 인식
- Label: Nose, Chin
- Conditions:
정면 / 좌측 / 우측 시점
모자 착용
- Images: 총 21장
- Purpose: 작은 객체 및 낮은 Point Density 환경 테스트

## 🛠 Sensor & Preprocessing
- Camera: Intel RealSense D455
- Hadeware: NVIDIA Jetson Board
- Data: Real-world 3D Point Cloud
- Augmentation: 3D Rotation 등 적용

## 🧠 Model: RandLa-Net
RandLa-Net은 대규모 Point Cloud를 효율적으로 처리하기 위한 Semantic Segmentation 모델입니다.

- Key Characteristics
Random Sampling 기반 빠른 Downsampling
Voxelization 및 Graph 전처리 불필요
Jetson 환경에 적합한 경량 구조

- Architecture
Encoder–Decoder 구조

  Encoder: Random Sampling + Local Feature Aggregation(LFA)

  Decoder: Interpolation + Skip Connection

- Local Feature Aggregation (LFA)
Local Spatial Encoding
Attention Pooling
Residual + MLP를 통한 Feature Update

## 📊 Result(Demo)
- finger tips
<img width="1347" height="507" alt="{2DC2946D-96A8-4B98-914C-93C83025FEB5}" src="https://github.com/user-attachments/assets/ef10c1b4-83a6-4dae-844e-db52cea37b10" />

![finger_tips_demo](https://github.com/user-attachments/assets/22280a89-93d3-4455-b4d3-02e690732630)


- sign language
<img width="1349" height="509" alt="{FA0B73B9-0623-4903-988A-6EFFF694050D}" src="https://github.com/user-attachments/assets/b9ea83cd-02a3-44b3-9d4c-db64fc0c4e5d" />

![signlanguage_demo_3](https://github.com/user-attachments/assets/940abea2-c81b-41a3-a2af-c324d5c2d201)


- face
<img width="1074" height="509" alt="{E34B79F6-C6BF-4D28-A2D8-192165A0BEEE}" src="https://github.com/user-attachments/assets/bc8c7a3f-9294-4c40-9dcb-b7877b788c79" />

Failure Analysis (Face Dataset)

Dataset 수 부족 

학습 Epoch 부족 

Nose와 Chin의 돌출 크기 차이 

낮은 Point Density 



