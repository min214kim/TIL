# Numerical Computing with Scipy

- linear algebra
- integration
- differential equation
- root finding
- optimization : 딥러닝, 머신러닝
- interpolation (내사법)
- statistical distributions and random number generations

- numpy위에 올리는 것

### Integration , 그 중 구분구적법

- `quad` : One demension

$\int_0^5 e^{\sin(x)} dx$

```python
import numpy as np
import matplotlib.pyplot as plt

# Integration 예시 - exponential! (e의 sinx제곱을 0,5까지 적분)
from scipy.integrate import quad

f = lambda x : np.exp(np.sin(x))
integral, app_error = quad(f, 0, 5) # app_error : 적분의 오차 
```

- `dblquad` : Multi demensional

$I(n) = \int_0^\infty \int_1^\infty \frac{e^{-xt}}{t^n} dt dx = \frac{1}{n}$

```python
from scipy.integrate import dblquad

n = 10 
# outer integral 먼저, inner을 나중에 써줌
# 안쪽 구간은 x에 대한 함수로 표현해주는 것이 일반적인 form
dblquad(lambda t, x : np.exp(-x*t)/t**n, 0, np.inf, lambda x : 1, lambda x : np.inf()
```

### Differential Equation (ordinary)

- Basic SIR Model : 감염병의 확산 표현
    - the susceptibe (S), the infected (I), the recovered (R), the dead(D)
    
    $\frac{dS}{dt} = -\beta S I$
    
    $\frac{dI}{dt} = \beta S I - \gamma I$
    
    $\frac{dR}{dt} = \gamma I$
    

```python
from scipy.integrate import odeint 

odeint(미분방정식, (초기값), 기간(t))
```

### Root finding

1. **One-demensional**
- `bisect`
    - 둘로 쪼개기 → 근이 들어있을 것이라 예측되는 구간을 파악 (중간값 정리 사용)
    - 구간 파악 후 구간 중간값 대입 → 양수라면 근은 오른쪽에, 음수라면 왼쪽에 있는 것
    - 해당 중간값과 구간의 끝값을 새로운 구간으로 설정
    - 반복
- `brentq` : 미분 없이 구간을 먼저 찾아 root를 찾는 방식
    - bisection과 거의 유사하나 반으로 쪼개지 않고 적절한 비율로 쪼갬 → 속도 향상
- `newton` : 미분 사용
    - 임의의 한 점에서 tailor expansion을 하고, 접선과 x축이 만나는 점을 구한다
    - 해당 점에서 다시 tailor expansion, 이후 과정 반복 → 근으로 수렴하도록
    - 구간 줄이기보다 속도 빠를 수 있으나 함수 형태에 따라 수렴하지 못하거나 속도가 느릴 수도 있음 → 적절한 상황에서 선택한다
    
    $x^3 - 2x + 3 = e^{\sqrt{x}}$ 
    

```python
from scipy.optimize import bisect, brentq, newton, root_scalar 
# root_scalar : 이 안에서 방식 지정 가능. 앞의 것들 전부 구현할 수 있는 알고리즘 

# 구간
bisect(F, 0, 1) # 최초의 구간 설정
brentq(F, 0, 1)

# newton
newton(F, 0.5) # 최초의 점 설정

# root_scalar
root_scalar(F, method='bisect', bracket=(0,1))
# 미리 도함수를 알려주면 더 효율적 
root_scalar(F, method='newton', x0=0.5, 
						fprime=(lambda x: 3*x**2 - 2 - 0.5/np.sqrt(x)*np.exp(np.sqrt(x)))
```

1. **Multi-demensional**
    
    Suppose that $G: R^2 \rightarrow R^2$ is given as
    
    $G_1(x_0, x_1) = \frac{1}{2} (x_0 - x_1)^3 + x_0 - 1$
    
    $G_2(x_0, x_1) = \frac{1}{2} (x_1 - x_0)^3 + x_1$
    

```python

def G(x):
    return np.array([0.5 * (x[0] - x[1])**3 + x[0] - 1.0,
            0.5 * (x[1] - x[0])**3 + x[1]])
 
# hybrid 사용   
from scipy.optimize import root    
res = root(G, [0,0], method='hybr')
res.x

# fsolve 사용 - scalar function에도 사용
from scipy.optimize import fsolve

fsolve(G, (0,0))

```

### Optimization

- 함수의 차원 파악 (스칼라-스칼라인지, 벡터-숫자인지 등)
- 미분 가능성 파악 (미분가능: 도함수 존재여부)
- convexity :
    - A function $f: X \to Y$ is convex if $X$ is a convex set and $\forall x, y \in X$ and $\forall t \in [0, 1]$, $f(t x + (1 − t)y) \le t f(x) + (1 − t)f(y)$.
    - globally non-convex이지만 locally convex한 형태도 있다 (두개 이상의 최솟값이 있는 형태의 경우)
    - scipy는 locally convex한 점을 찾기 때문에 함수의 모양을 모를 때는 minimum을 찾았다고 그것이 global minimum이라고 간주하면 안됨!
1. Univariate function minimization 
    - unconstrained / constrained
    - Uni-vari `minimize_scalar`
        - unconstrained
        
        ```python
        def f(x):
        	return x*2 + 10*np.sin(x) # local min이 2개 존재하는 형태 
        
        from scipy.optimize import minimize_scalar, minimize
        
        minimize_scalar(f, fethod='brent', bracket=(-3,-1,0)) # bracket 3개 : 가운데의 함수값이 양쪽의 함수값보다 작아야 함
        minimize_scalar(f, method='brent', bracket=(3,4,5)) 
        minimize_scalar(f) # 알아서 bracket을 넓게 잡아서 가져옴 
        ```
        
        - constrained
        
        ```python
        minimize_scalar(f, method='bounded', bounds=(-10,10)) 
        ```
        
2. Multivariate function minimization `minimize`
    
    ```python
    print(minimize(f, x0=0, method='BFGS') # 초기값을 0으로, newton이랑 비슷한 알고리즘 
    ```
    
    - Unconstrained
        
        Six-hump camel-back function  : 혹이 6개인 낙타처럼 생긴 유명한 함수임 
        
        $H(x_0, x_1) = \left(4 - 2.1x_0 + \frac{1}{3}x_0^4\right)x_0^2 + x_0 x_1 + (4x_1^2-4)x_1^2$
        
        ```python
        def sixhump(x):
        	return((4-2.1*x[0]**2 + x[0]**4 / 3.) * x[0]**2 + x[0] * x[1]
                  + (-4 + 4*x[1]**2) * x[1] **2)
        
        minimize(sixhump, x0=[0, 0.7], method='BFGS')
        minimize(sixhump, x0=[1.5, 0.6], method='Nelder-Mead') # 미분 사용하는 방식이 잘 맞지 않는 경우 사용 
        ```
        
    - Constrained
        
        Rosenbrock Function
        
        $\min 100\left(x_1 - x_0^2\right)^2 + (1-x_0)^2$
        
        subject to:
        $x_0 + 2x_1 \le 1$
        
        $x_0^2 + x_1 \le 1$
        
        $x_0^2 - x_1 \le 1$
        
        $2x_0 + x_1 = 1$
        
        $0 \le x_0 \le 1$
        
        $-0.5 \le x_1 \le 2$
        
        - trust-constr ,SLSQP, COBYLA 알고리즘 : 하는 것은 비슷한데 제약식을 알려주는 방식이 다르다
        - linear과 nonlinear 제약식을 써주는 방식이 다름
            - 1,4 : linear, 2,3 : nonlinear, 5,6: bound 구분해 리스트로 넣어준다
        
        ```python
        def rosenbrock(x):
            return 100 * (x[1]-x[0]**2)**2 + (1-x[0])**2
           
        from scipy.optimize import Bounds, LinearConstraint, NonlinearConstraint
        
        # 1. trust-constr method
        bounds = Bounds(lb=[0, -0.5], ub=[1.0, 2.0]) #X0의 바운드, X1의 바운드 순서(5,6식을 vector form으로 합친것)
        
        linear_constraint = LinearConstraint([[1, 2], [2, 1]], [-np.inf, 1], [1, 1])
        nonlinear_constraint = NonlinearConstraint(lambda x: [x[0]**2 + x[1], x[0]**2 - x[1]], [-np.inf,-np.inf], [1,1]) # low bound가 설정되지 않았다면 inf로 적어줘야! 
        
        minimize(rosenbrock, [0.5, 0], method='trust-constr', bounds=bounds, constraints=(linear_constraint, nonlinear_constraint))
        
        # 2. SLSQP method : 제약을 딕셔너리 형태로 넣기, inequality conditon 과 equality conditon으로 넣어줌 
        ineq_cons = {'type': 'ineq',
                     'fun' : lambda x: np.array([1 - x[0] - 2*x[1],
                                                 1 - x[0]**2 - x[1],
                                                 1 - x[0]**2 + x[1]])}
        eq_cons = {'type': 'eq',
                   'fun' : lambda x: np.array([2*x[0] + x[1] - 1])}
        
        minimize(rosenbrock, [0.5, 1], method='SLSQP', bounds=bounds, constraints=[eq_cons, ineq_cons])
        # 결과는 trust-constr과 같다 
        
        #3. COBYLA method : SLSQP와 같지만 inequality 만 accept
        minimize(rosenbrock, [0.5, 1], method='COBYLA', bounds=bounds, constraints=ineq_cons)
        # full 고려가 안되었기 때문에 결과가 조금 다름 (제약이 덜한 곳에서의 minimize이기 때문에 값이 같거나 더 작음)
        ```
        

### Interpolation

- 1-D Interpolation
    - 1차원은 numpy에 내장된 방법을 사용하는게 더 편리
    - scipy에 interp1d가 있지만 사용하지 않는걸 권장함 (곧 사라진다)
    
    ```python
    n = 9
    x = np.linsplace(0,10,num=1) # 함수는 모르고 0~10사이 1간격의 data point 10개만 알고 있다고 가정 
    y = np,cos(-x**2 / n) # 모른다고 가정!
    
    # 볼록한 구간에서는 오차가 크다 (approximation이 좋지 않음 )
    x_fine = np.linspace(0, 10, num=1001) # data point 사이 1000개의 점을 추론해서 그리기
    y_lin_interp = np.interp(x_fine, x, y)
    y_true = np.cos(-x_fine**2 / n) # n값에 따라서 모양이 많이 달라지고, 오차도 달라진다 
    
    # approximation 위험을 항상 가지고 있다 ! 
    ```
    
- 2D 이상