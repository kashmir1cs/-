# Numpy 연습하기

## 1차원 Array 만들기


```python
%config Completer.use_jedi = False
# 자동완성 위한 설정
```


```python
import numpy as np
# 1차원 Array
v1=np.array([1,2,3,4])
for i in range(len(v1)):
    print(v1[i])

```

    1
    2
    3
    4
    

## 연속되는 숫자 Arrary로 만들기


```python
v1=np.arange(5) # 0부터 연속된 숫자 다섯개 생성 arrary
print(v1) #  0,1,2,3,4,5
```

    [0 1 2 3 4]
    

### 연속되는 Array 만들때 증감 간격 지정


```python
v2=np.arange(1,10,2, dtype=int)
v3=np.arange(3.5,10.5,2,dtype=float)
print("v2:",v2)
print("v3:",v3)
```

    v2: [1 3 5 7 9]
    v3: [3.5 5.5 7.5 9.5]
    

### 제곱/세제곱/n제곱 하기


```python
n=6
v4=np.arange(1,10,2)**2
v5=np.arange(1,10,2)**3
v6=np.arange(2,13,2,dtype=int)**n # n 제곱
print(v4)
print(v5)
print(v6)
```

    [ 1  9 25 49 81]
    [  1  27 125 343 729]
    [     64    4096   46656  262144 1000000 2985984]
    

# 행렬 만들기

- np.reshape : 행렬 만들기 (Array를 행렬로 변환)
- 차원수 지정 필요
- order="C" : 값을 행부터 채워 놓음, 기본 값
- order="F" : 값을 열부터 채워 놓음

## 행렬만들기 - 기본


```python
v1= np.arange(12)
print("v1: ",v1)
v2=v1.reshape(2,6)
print("v2:", v2)
v3=v1.reshape(2,6,order="F")
print("v3:",v3)
```

    v1:  [ 0  1  2  3  4  5  6  7  8  9 10 11]
    v2: [[ 0  1  2  3  4  5]
     [ 6  7  8  9 10 11]]
    v3: [[ 0  2  4  6  8 10]
     [ 1  3  5  7  9 11]]
    

## 행렬 연산

- note : chaining 활용하면 식이 간결해진다


```python
# Chaining 활용
v1=np.arange(1,5).reshape(2,2)
print(v1)
```

    [[1 2]
     [3 4]]
    

### 행렬 사칙 연산 (덧셈)


```python
print(np.add(v1,v1))
```

    [[2 4]
     [6 8]]
    

### 행렬 사칙 연산 (뺄셈)


```python
print(np.subtract(v1,v1))
```

    [[0 0]
     [0 0]]
    

### 행렬 사칙 연산 (곱셈) : 행렬 곱셈 X


```python
print(np.multiply(v1,v1))
```

    [[ 1  4]
     [ 9 16]]
    

### 행렬 연산 (곱셈)


```python
print(np.dot(v1,v1))
```

    [[ 7 10]
     [15 22]]
    

# 다차원 배열 만들기

## 다차원 배열 만들기 기본 : 3차원 배열


```python
v1=np.arange(12)
print(v1)
v2=v1.reshape(2,3,2, order="F")
print(v2)
```

    [ 0  1  2  3  4  5  6  7  8  9 10 11]
    [[[ 0  6]
      [ 2  8]
      [ 4 10]]
    
     [[ 1  7]
      [ 3  9]
      [ 5 11]]]
    

## 다차원배열 차원 확인


```python
print(v2.shape)
```

    (2, 3, 2)
    

## 배열내 합계, 최소,최대값,대각 성분 확인


```python
v3=np.arange(3.5,10.5,2, dtype=float)
print(v3)
v4=np.arange(1,5).reshape(2,2)
print(v4)
```

    [3.5 5.5 7.5 9.5]
    [[1 2]
     [3 4]]
    


```python
print(np.amax(v3))
print(np.amax(v4))
print(np.amin(v3))
print(np.amin(v4))
print(np.sum(v3))
print(np.sum(v4))
print(v3.sum())
print(v4.sum())
print(v4.diagonal())
```

    9.5
    4
    3.5
    1
    26.0
    10
    26.0
    10
    [1 4]
    


```python

```
