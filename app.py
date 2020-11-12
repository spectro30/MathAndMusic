import pyautogui, time, random

def make_pi():
    q, r, t, k, m, x = 1, 0, 1, 1, 3, 3
    for j in range(1000):
        if 4 * q + r - t < m * t:
            yield m
            q, r, t, k, m, x = 10*q, 10*(r-m*t), t, k, (10*(3*q+r))//t - 10*m, x
        else:
            q, r, t, k, m, x = q*k, (2*q+r)*x, t*x, k+1, (q*(7*k+2)+r*x)//(t*x), x+2


pi_digits = []

for i in make_pi():
    pi_digits.append(str(i))

keyMap = {
  '0': "c",
  '1': "v",
  '2': "b",
  '3': "n",
  '4': "m",
  '5': "g",
  '6': "h",
  '7': "j",
  '8': "k",
  '9': "l"
  
}

#print(len(pi_digits))

mx_size = 0
time.sleep(5)
n = 100


for digit in pi_digits:
    pyautogui.typewrite(keyMap[digit])
    sleepTime = random.random() * 2
    time.sleep(sleepTime)
    #print(sleepTime)
    mx_size = mx_size + 1
    if mx_size == n:
        break
