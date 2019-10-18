## run_make_as_is_data.py
하는일
```
1.as is data를 만든다.
2.만든 data를 elastic search에 넣는다.
* 1번은 function으로 구현 되어 있어서 따로 실행 할 수 있다. src/make_as_is_data.py
``` 

## run_make_to_be_data.py
하는일
```
1.to be data를 만든다.
2.만든 data를 elastic search에 넣는다.
* 1번은 function으로 구현 되어 있어서 따로 실행 할 수 있다. src/make_as_is_data.py
``` 

## run_ingest.py
하는일
```
1.더미 디렉토리와 파일을 생성한다.
2.elastic search에 inactive상태인 1개의 row를 create한다.
3.n초를 대기한다(실제로는 파일이 copy되는 시간)
4.elastic search에 해당 row의 status field를 active라고 update한다.
```

### run_ingest.py실행 방법
1. elastic search가 설치 되어 있어야 한다.
2. run_ingest.py에서 elasticsearch의 주소를 바꿔준다.
3. python3 run_ingest.py 를 실행한다.
* 이렇게 하면 ingest되는 과정이 보인다.

