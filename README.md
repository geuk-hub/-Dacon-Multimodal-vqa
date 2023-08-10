# 월간 데이콘 이미지 기반 질의 응답 AI 경진대회

## 1. Introduction

이미지의 id, 해당 이미지와 관련된 질문이 담긴 csv 파일이 실제 이미지와 함께 데이터셋으로 제공.

이미지에서 확인할 수 있는 정보들을 바탕으로, 질문에 대해 올바르게 답변할 수 있는 AI 모델을 개발하는 것이 목표.

## 2. Data

image
- train image : 107,231개
- test image : 11,915개

train.csv
- ID : 질문ID
- image_id : 이미지ID
- question : 이미지 관련 질문
- answer : 질문에 대한 정답

test.csv
- ID : 질문ID
- image_id : 이미지 ID
- question : 이미지 관련 질문

sample_submission.csv
- ID : 질문ID
- answer : 질문에 대한 답변

