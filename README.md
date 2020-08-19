## 태그 서버

* Django
* MySQL
* Tensorflow ( https://github.com/Below0/DeepAudioClassification )
* 기타 노래 장르 판별 트레이닝법은 위 주소 참고

-----


## 사용법
### 도커 사용시
```
디렉토리 시작 home/src/tag/mit-cf/
docker build -t tag .
docker run -d -p 8000:8000 --name tag tag
```
### 직접 실행
```
./run.sh
```


