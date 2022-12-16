# level2_dataannotation_nlp-level2-nlp-03

## Reports
- Wrap up Report : [03_Wrapup_Report](https://cerulean-dresser-e85.notion.site/Wrap-up-Report-75ae500eee304dab848dae6c2b76c6b8)
- Relation map : [03_relation.xlsx](https://github.com/boostcampaitech4lv23nlp1/level2_dataannotation_nlp-level2-nlp-03/files/10243830/03_relation.xlsx)
- Guideline : [03_guideline.docx](https://github.com/boostcampaitech4lv23nlp1/level2_dataannotation_nlp-level2-nlp-03/files/10243833/03_guideline.docx)

## Project Summary
<img src=https://user-images.githubusercontent.com/113564875/208052179-39f7d146-040d-45f5-b15f-1f04579d0f67.png>

- '법률'을 주제로 RE(Relation Extraction) 데이터셋 제작
- relation은 KLUE를 참고하여 9개로 구분
- 완성된 데이터셋을 모델에 적용, 성능 검증

## Members
|김근형|김찬|유선종|이헌득|
|:---:|:---:|:---:|:---:|
|<img src="https://user-images.githubusercontent.com/97590480/205299519-174ef1be-eed6-4752-9f3d-49b64de78bec.png">|<img src="https://user-images.githubusercontent.com/97590480/205299316-ea3dc16c-00ec-4c37-b801-3a75ae6f4ca2.png">|<img src="https://user-images.githubusercontent.com/97590480/205299037-aec039ea-f8d3-46c6-8c11-08c4c88e4c56.jpeg">|<img src="https://user-images.githubusercontent.com/97590480/205299457-5292caeb-22eb-49d2-a52e-6e69da593d6f.jpeg">|
|[Github](https://github.com/kimkeunhyeong)|[Github](https://github.com/chanmuzi)|[Github](https://github.com/Trailblazer-Yoo)|[Github](https://github.com/hundredeuk2)|


## Roles
| Member | Role | 
| --- | --- |
| 김근형 | Data annotation, Fine-Tuning  |
| 김찬 | Data annotation, 가이드라인 작성 |
| 유선종 | Data annotation, IAA 계산 |
| 이헌득 | Data annotation, Relation map 작성 |

## Data Overview
- Data split ratio : Train(0.7), Validation(0.15), Test(0.15)
- Train data : 813
- Validation data : 174
- Test data : 175
- Number of entity : 6
    ```
    'PER', 'EVENT', 'ORG', 'DATE', 'LAW', 'THEORY'
    ```
- Number of relation : 9
    ```
    'no_relation', 'per:theory', 'per:event', 'org:naming', 'org:members_of',
    'org:event', 'law:subordinate', 'law:definition','date:event'
    ```
## Entity
| Type | Description | 
| --- | --- |
| PER | person의 약자로 사람(개인)을 의미합니다. 개인을 뜻할 수 있는 모든 단어들과 특정 인물 등이 여기에 포함됩니다.  |
| EVENT | 사건을 의미합니다. 사람(개인) 또는 조직(단체)과 관련될 수 있습니다. |
| ORG | organization의 약자로 조직(단체)을 뜻합니다. person과 대비되는 Entity입니다. |
| DATE | 날짜를 의미합니다. 특정 사건이 발생한 날짜나 시기를 뜻하게 됩니다. |
| LAW | 법률을 의미합니다. 법률과 관련된 단어들이 여기에 포함됩니다. |
| THEORY | 이론 또는 주장을 의미합니다. |
  
## Relation
|id	|class_name (ko)	|class_name (en)	|direction (sub, obj)	|description|
|---|---|---|---|---|
|1	|관계_없음	|no_relation	|(\*,\*)	|관계를 유추할 수 없음.|
|2	|개인:사건	|per:event	|(PER,EVENT)	|Object는 Subject가 일으킨 / 속한 사건|
|3	|개인:이론	|per:theory	|(PER,THEORY)	|Object는 Subject가 주장하는 / 공표한 이론|
|4	|단체:명명_관계	|org:naming	|(ORG,ORG)	|Object는 Subject의 또다른 표현|
|5	|단체:사건	|org:event	|(ORG, EVENT)	|Object는 Subject가 일으킨 / 속한 사건|
|6	|단체:구성원	|org:members_of	|(ORG,ORG)	|Object는 Subject에 속한 단체 / 인물|
|7	|날짜:사건	|date:event	|(DATE,EVENT)	|Object는 Subject에 발생한 사건|
|8	|법:정의	|law:definition	|(LAW, LAW)	|Object는 Subject의 정의 / 정의 구문|
|9	|법:하위_법	|law:subordinate	|(LAW, LAW)	|Object는 Subject에 종속한 법|

## Results (KLUE/BERT-base, lr=1e-5)
- **Fleiss' Kappa** : 0.798
- **Micro F1** : 89.9598
- **AUPRC** : 91.7236

## License
본 데이터셋은 [한국어 위키피디아](https://ko.wikipedia.org/)를 사용하여 제작되었으며, [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.ko) 라이선스 하에 공개되어 있습니다.

<a href="https://creativecommons.org/licenses/by-sa/3.0/deed.ko"><img src="https://user-images.githubusercontent.com/113564875/208059449-000fb28b-f126-4988-9439-eb209e7fd628.png" width="150"/></a>
