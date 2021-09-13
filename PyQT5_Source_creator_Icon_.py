# auto-generated source-code file PyQT5_Source_creator_Icon.py with Pycture
# Pycture developed by
#    ____             _             _ _     ____  _  _
#   / __ \  __ _ _ __| |_ _ __ ___ (_) |__ |___ \| || |
#  / / _` |/ _` | '__| __| '_ ` _ \| | '_ \  __) | || |_
# | | (_| | (_| | |  | |_| | | | | | | | | |/ __/|__   _|
#  \ \__,_|\__,_|_|   \__|_| |_| |_|_|_| |_|_____|  |_|
#   \____/

from PyQt5 import QtGui
import base64
import os

def Get_icon(image_str):
    ImageStr = base64.b64decode(image_str)
    with open("icon.ico", "wb") as icon_text:
        icon_text.write(ImageStr)
    icon_text.close()
    qi = QtGui.QIcon("icon.ico")
    os.remove("icon.ico")
    return(qi)
        
icon_str = "AAABAAcAEBAAAAAAIABKBAAAdgAAABgYAAAAACAAXgQAAMAEAAAgIAAAAAAgAHgEAAAeCQAAMDAAAAAAIACfBAAAlg0AAEBAAAAAACAAzgQAADUSAACAgAAAAAAgAHwFAAADFwAA//8AAAAAIABNBwAAfxwAAIlQTkcNChoKAAAADUlIRFIAAAAQAAAAEAgDAAAAKC0PUwAAAwBQTFRFAAAAfMHzAID/c73ye8HzarjyRqfuRafuZ7fxbrvyRKbubLnygMP0QqbubbryTKrvSqnvSKnvhsb0V6/wTqvvdL3zfcLzYrXxXbLwUKzvS6rvQqXuSanvZLbxV7Dwicf0esDzaLfxVK7wiMf0dr7za7nyQ6buY7XxaLjygsT0Al/5ia7fdaDaa5rXXpDUU4nRSoPOQHzMAk3IAlXflbbjXZDUM3PIY5TVLW/Hc5/aLG7Gk7XiNXTJkbPhMXHIiq7gPnrLgqndS4PPLnDHJ2vFJGnEJmrFLG/HMnLIRoDNK23GWY3TfKXceKPbAGzOAITmWbn/KGzFgandVovSJWnEfabcRX/Nj7LhbZrYV4vSP3vMKmzG//IAOqz/Qa//iooArq4AIF+9LGfBN2/EQ3jIGFm6ToDLZ5LSiqvdGVq7O3LFd3cAd53WGlm7Q3fHi6vcGVm6Tn/KIV+9faHYHl28c5rVHFu7cFcBgWQBupEB/8kOL2jBUoHLIV69bpbUPnPFKWS+I1+8HVu7GVi5HVq6iWoBJGC9K2W/RHfGe5/XJmG9XYnONWzCh6jbIV28i6rcj63dLGW+bJTSIV27XYnNJWC8kq/eV4TLKmO+hKXZb5bTZI7QVYLLS3vIQHPFNmzBto0BlKnOgJnEkqjNgZrFeJPBepTCVHawboq8PWOmd5LAfpfDh5/IhJzGmKzQg5zGAAAAsbGxsrKys7OztLS0tbW1tra2t7e3uLi4ubm5urq6u7u7vLy8vb29vr6+v7+/wMDAwcHBwsLCw8PDxMTExcXFxsbGx8fHyMjIycnJysrKy8vLzMzMzc3Nzs7Oz8/P0NDQ0dHR0tLS09PT1NTU1dXV1tbW19fX2NjY2dnZ2tra29vb3Nzc3d3d3t7e39/f4ODg4eHh4uLi4+Pj5OTk5eXl5ubm5+fn6Ojo6enp6urq6+vr7Ozs7e3t7u7u7+/v8PDw8fHx8vLy8/Pz9PT09fX19vb29/f3+Pj4+fn5+vr6+/v7/Pz8/f39/v7+////9L0oXgAAALF0Uk5T//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////8A1/RcZAAAAEhJREFUeJxj2IAGGEAEExIgQsAICvwCIIDBKCbGKMbIKAZJACKEIgASQtEC0hMfAwEgFWgCUIBbAOSwVhCoggCwQBUSwC6ADABDflz2+CX+dQAAAABJRU5ErkJggolQTkcNChoKAAAADUlIRFIAAAAYAAAAGAgDAAAA16nNygAAAwBQTFRFAAAAfMHzAID/c73ye8HzarjyRqfuRafuZ7fxbrvyRKbubLnygMP0QqbubbryTKrvSqnvSKnvhsb0V6/wTqvvdL3zfcLzYrXxXbLwUKzvS6rvQqXuSanvZLbxV7Dwicf0esDzaLfxVK7wiMf0dr7za7nyQ6buY7XxaLjygsT0Al/5ia7fdaDaa5rXXpDUU4nRSoPOQHzMAk3IAlXflbbjXZDUM3PIY5TVLW/Hc5/aLG7Gk7XiNXTJkbPhMXHIiq7gPnrLgqndS4PPLnDHJ2vFJGnEJmrFLG/HMnLIRoDNK23GWY3TfKXceKPbAGzOAITmWbn/KGzFgandVovSJWnEfabcRX/Nj7LhbZrYV4vSP3vMKmzG//IAOqz/Qa//iooArq4AIF+9LGfBN2/EQ3jIGFm6ToDLZ5LSiqvdGVq7O3LFd3cAd53WGlm7Q3fHi6vcGVm6Tn/KIV+9faHYHl28c5rVHFu7cFcBgWQBupEB/8kOL2jBUoHLIV69bpbUPnPFKWS+I1+8HVu7GVi5HVq6iWoBJGC9K2W/RHfGe5/XJmG9XYnONWzCh6jbIV28i6rcj63dLGW+bJTSIV27XYnNJWC8kq/eV4TLKmO+hKXZb5bTZI7QVYLLS3vIQHPFNmzBto0BlKnOgJnEkqjNgZrFeJPBepTCVHawboq8PWOmd5LAfpfDh5/IhJzGmKzQg5zGAAAAsbGxsrKys7OztLS0tbW1tra2t7e3uLi4ubm5urq6u7u7vLy8vb29vr6+v7+/wMDAwcHBwsLCw8PDxMTExcXFxsbGx8fHyMjIycnJysrKy8vLzMzMzc3Nzs7Oz8/P0NDQ0dHR0tLS09PT1NTU1dXV1tbW19fX2NjY2dnZ2tra29vb3Nzc3d3d3t7e39/f4ODg4eHh4uLi4+Pj5OTk5eXl5ubm5+fn6Ojo6enp6urq6+vr7Ozs7e3t7u7u7+/v8PDw8fHx8vLy8/Pz9PT09fX19vb29/f3+Pj4+fn5+vr6+/v7/Pz8/f39/v7+////9L0oXgAAALF0Uk5T//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////8A1/RcZAAAAFxJREFUeJxj2IADMEAoJgxAfQktCECWMEICfgEIgEciBgiAhJFRDBYJqBy6BATFYDMKpwTQYhARH4MAYKNAAEQSKYEEKJSABGI5GLRWIQBUYgEEYEpUYQCyJTABAON6y4itO6WEAAAAAElFTkSuQmCCiVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAADAFBMVEUAAAB8wfMAgP9zvfJ7wfNquPJGp+5Fp+5nt/Fuu/JEpu5sufKAw/RCpu5tuvJMqu9Kqe9Iqe+GxvRXr/BOq+90vfN9wvNitfFdsvBQrO9Lqu9Cpe5Jqe9ktvFXsPCJx/R6wPNot/FUrvCIx/R2vvNrufJDpu5jtfFouPKCxPQCX/mJrt91oNprmtdekNRTidFKg85AfMwCTcgCVd+VtuNdkNQzc8hjlNUtb8dzn9osbsaTteI1dMmRs+ExcciKruA+esuCqd1Lg88ucMcna8UkacQmasUsb8cycshGgM0rbcZZjdN8pdx4o9sAbM4AhOZZuf8obMWBqd1Wi9IlacR9ptxFf82PsuFtmthXi9I/e8wqbMb/8gA6rP9Br/+KigCurgAgX70sZ8E3b8RDeMgYWbpOgMtnktKKq90ZWrs7csV3dwB3ndYaWbtDd8eLq9wZWbpOf8ohX719odgeXbxzmtUcW7twVwGBZAG6kQH/yQ4vaMFSgcshXr1ultQ+c8UpZL4jX7wdW7sZWLkdWrqJagEkYL0rZb9Ed8Z7n9cmYb1dic41bMKHqNshXbyLqtyPrd0sZb5slNIhXbtdic0lYLySr95XhMsqY76EpdlvltNkjtBVgstLe8hAc8U2bMG2jQGUqc6AmcSSqM2BmsV4k8F6lMJUdrBuirw9Y6Z3ksB+l8OHn8iEnMaYrNCDnMYAAACxsbGysrKzs7O0tLS1tbW2tra3t7e4uLi5ubm6urq7u7u8vLy9vb2+vr6/v7/AwMDBwcHCwsLDw8PExMTFxcXGxsbHx8fIyMjJycnKysrLy8vMzMzNzc3Ozs7Pz8/Q0NDR0dHS0tLT09PU1NTV1dXW1tbX19fY2NjZ2dna2trb29vc3Nzd3d3e3t7f39/g4ODh4eHi4uLj4+Pk5OTl5eXm5ubn5+fo6Ojp6enq6urr6+vs7Ozt7e3u7u7v7+/w8PDx8fHy8vLz8/P09PT19fX29vb39/f4+Pj5+fn6+vr7+/v8/Pz9/f3+/v7////0vSheAAAAsXRSTlP//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////wDX9FxkAAAAdklEQVR4nGPYQAAwwBhMOAADAflBpUALAdAUGKEBY0IK/PwDUAAxCmJAAEgagZg4FYBVxOBSYGQEU4DDCqiCGJwKIFJgArcjYQriE2JQANQKMBhABaiAcgUVlVUoAJZgymEAl4JWOKjCrqAKF6CjApwq4ApwAQDk6lgOhGgTVgAAAABJRU5ErkJggolQTkcNChoKAAAADUlIRFIAAAAwAAAAMAgDAAAAYNwJtQAAAwBQTFRFAAAAfMHzAID/c73ye8HzarjyRqfuRafuZ7fxbrvyRKbubLnygMP0QqbubbryTKrvSqnvSKnvhsb0V6/wTqvvdL3zfcLzYrXxXbLwUKzvS6rvQqXuSanvZLbxV7Dwicf0esDzaLfxVK7wiMf0dr7za7nyQ6buY7XxaLjygsT0Al/5ia7fdaDaa5rXXpDUU4nRSoPOQHzMAk3IAlXflbbjXZDUM3PIY5TVLW/Hc5/aLG7Gk7XiNXTJkbPhMXHIiq7gPnrLgqndS4PPLnDHJ2vFJGnEJmrFLG/HMnLIRoDNK23GWY3TfKXceKPbAGzOAITmWbn/KGzFgandVovSJWnEfabcRX/Nj7LhbZrYV4vSP3vMKmzG//IAOqz/Qa//iooArq4AIF+9LGfBN2/EQ3jIGFm6ToDLZ5LSiqvdGVq7O3LFd3cAd53WGlm7Q3fHi6vcGVm6Tn/KIV+9faHYHl28c5rVHFu7cFcBgWQBupEB/8kOL2jBUoHLIV69bpbUPnPFKWS+I1+8HVu7GVi5HVq6iWoBJGC9K2W/RHfGe5/XJmG9XYnONWzCh6jbIV28i6rcj63dLGW+bJTSIV27XYnNJWC8kq/eV4TLKmO+hKXZb5bTZI7QVYLLS3vIQHPFNmzBto0BlKnOgJnEkqjNgZrFeJPBepTCVHawboq8PWOmd5LAfpfDh5/IhJzGmKzQg5zGAAAAsbGxsrKys7OztLS0tbW1tra2t7e3uLi4ubm5urq6u7u7vLy8vb29vr6+v7+/wMDAwcHBwsLCw8PDxMTExcXFxsbGx8fHyMjIycnJysrKy8vLzMzMzc3Nzs7Oz8/P0NDQ0dHR0tLS09PT1NTU1dXV1tbW19fX2NjY2dnZ2tra29vb3Nzc3d3d3t7e39/f4ODg4eHh4uLi4+Pj5OTk5eXl5ubm5+fn6Ojo6enp6urq6+vr7Ozs7e3t7u7u7+/v8PDw8fHx8vLy8/Pz9PT09fX19vb29/f3+Pj4+fn5+vr6+/v7/Pz8/f39/v7+////9L0oXgAAALF0Uk5T//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////8A1/RcZAAAAJ1JREFUeJzt1MkJgDAQheFgOR7HPtQCBO3C5Z4+LCElKtFgRmbIBIng8l/08D5wQ2UiU5dAJkhF7n+QHuSnaABMRSyAsqqpbgHNFtgzu7XHIFhHyEkAiIG7DqfE4FApgXtUgpveb1gOAIG2a6g8AMdLCwLvi/gIYHoQMMy+H8aJyv+R9X6DDgONI/cIzCh6zwNmjwC3eTUQCQQkRYMFgOEc3T06j/gAAAAASUVORK5CYIKJUE5HDQoaCgAAAA1JSERSAAAAQAAAAEAIAwAAAJ23gewAAAMAUExURQAAAHzB8wCA/3O98nvB82q48kan7kWn7me38W678kSm7my58oDD9EKm7m268kyq70qp70ip74bG9Fev8E6r73S9833C82K18V2y8FCs70uq70Kl7kmp72S28Vew8InH9HrA82i38VSu8IjH9Ha+82u58kOm7mO18Wi48oLE9AJf+Ymu33Wg2mua116Q1FOJ0UqDzkB8zAJNyAJV35W2412Q1DNzyGOU1S1vx3Of2ixuxpO14jV0yZGz4TFxyIqu4D56y4Kp3UuDzy5wxydrxSRpxCZqxSxvxzJyyEaAzSttxlmN03yl3Hij2wBszgCE5lm5/yhsxYGp3VaL0iVpxH2m3EV/zY+y4W2a2FeL0j97zCpsxv/yADqs/0Gv/4qKAK6uACBfvSxnwTdvxEN4yBhZuk6Ay2eS0oqr3RlauztyxXd3AHed1hpZu0N3x4ur3BlZuk5/yiFfvX2h2B5dvHOa1Rxbu3BXAYFkAbqRAf/JDi9owVKByyFevW6W1D5zxSlkviNfvB1buxlYuR1auolqASRgvStlv0R3xnuf1yZhvV2JzjVswoeo2yFdvIuq3I+t3SxlvmyU0iFdu12JzSVgvJKv3leEyypjvoSl2W+W02SO0FWCy0t7yEBzxTZswbaNAZSpzoCZxJKozYGaxXiTwXqUwlR2sG6KvD1jpneSwH6Xw4efyIScxpis0IOcxgAAALGxsbKysrOzs7S0tLW1tba2tre3t7i4uLm5ubq6uru7u7y8vL29vb6+vr+/v8DAwMHBwcLCwsPDw8TExMXFxcbGxsfHx8jIyMnJycrKysvLy8zMzM3Nzc7Ozs/Pz9DQ0NHR0dLS0tPT09TU1NXV1dbW1tfX19jY2NnZ2dra2tvb29zc3N3d3d7e3t/f3+Dg4OHh4eLi4uPj4+Tk5OXl5ebm5ufn5+jo6Onp6erq6uvr6+zs7O3t7e7u7u/v7/Dw8PHx8fLy8vPz8/T09PX19fb29vf39/j4+Pn5+fr6+vv7+/z8/P39/f7+/v////S9KF4AAACxdFJOU///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////ANf0XGQAAADMSURBVHic7dfRDYMgEAZgwjh9xD1qByCpW4h9dw9H6IiNERU4c3icmsbc/6Ik/l+MQFT1ZUYdDmhaAEDsay2AAP8JPDZyNmDwVBUuqEzfmGddv5AIMAF2iR9MTX9GAsbGInCB+VgEWDoQ3HTssADKLISPLZwUFkBaB3O/GIhKBwF+Kb+bxiJJALOu4gJg3UDhaCcQ70ABrgfwCHABkHu9t67rPkjSD4w2jWMCzvU0oIdB+wAYYND+DgDvAyBzuQD3BDb+nWn9E36+qfkBl6Rw3h/8DpsAAAAASUVORK5CYIKJUE5HDQoaCgAAAA1JSERSAAAAgAAAAIAIAwAAAPTgkfkAAAMAUExURQAAAHzB8wCA/3O98nvB82q48kan7kWn7me38W678kSm7my58oDD9EKm7m268kyq70qp70ip74bG9Fev8E6r73S9833C82K18V2y8FCs70uq70Kl7kmp72S28Vew8InH9HrA82i38VSu8IjH9Ha+82u58kOm7mO18Wi48oLE9AJf+Ymu33Wg2mua116Q1FOJ0UqDzkB8zAJNyAJV35W2412Q1DNzyGOU1S1vx3Of2ixuxpO14jV0yZGz4TFxyIqu4D56y4Kp3UuDzy5wxydrxSRpxCZqxSxvxzJyyEaAzSttxlmN03yl3Hij2wBszgCE5lm5/yhsxYGp3VaL0iVpxH2m3EV/zY+y4W2a2FeL0j97zCpsxv/yADqs/0Gv/4qKAK6uACBfvSxnwTdvxEN4yBhZuk6Ay2eS0oqr3RlauztyxXd3AHed1hpZu0N3x4ur3BlZuk5/yiFfvX2h2B5dvHOa1Rxbu3BXAYFkAbqRAf/JDi9owVKByyFevW6W1D5zxSlkviNfvB1buxlYuR1auolqASRgvStlv0R3xnuf1yZhvV2JzjVswoeo2yFdvIuq3I+t3SxlvmyU0iFdu12JzSVgvJKv3leEyypjvoSl2W+W02SO0FWCy0t7yEBzxTZswbaNAZSpzoCZxJKozYGaxXiTwXqUwlR2sG6KvD1jpneSwH6Xw4efyIScxpis0IOcxgAAALGxsbKysrOzs7S0tLW1tba2tre3t7i4uLm5ubq6uru7u7y8vL29vb6+vr+/v8DAwMHBwcLCwsPDw8TExMXFxcbGxsfHx8jIyMnJycrKysvLy8zMzM3Nzc7Ozs/Pz9DQ0NHR0dLS0tPT09TU1NXV1dbW1tfX19jY2NnZ2dra2tvb29zc3N3d3d7e3t/f3+Dg4OHh4eLi4uPj4+Tk5OXl5ebm5ufn5+jo6Onp6erq6uvr6+zs7O3t7e7u7u/v7/Dw8PHx8fLy8vPz8/T09PX19fb29vf39/j4+Pn5+fr6+vv7+/z8/P39/f7+/v////S9KF4AAACxdFJOU///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////ANf0XGQAAAF6SURBVHic7dtNDoIwEAVg43FcDvcAD2ACtwDccw5dufaI4l+EFijpdDpV31u2hPcxBDaEzVU5GwC+ALAVyyqAXP2T4ALI9vcCB0C6Xx+wBQAAAAAAAAAAAAAgdcBuVdQBHEIggL/gDiD/ZFnGBzD6PwQGgNf/FvgDuP2U53lRFHvfAAAAAACkAjhMxNgZdI7W5ADP8y8BhCfwKrAB431JwKPCHsF4QRxgjcAQyQKmRpAMQOYxnLrP403zUDUAxQMsaCIDJp9KLQDFBAy2rQO1ABQXYL8n/g5gCkgMMHeliQEoGuDTkxRg2E9lWVZVNTtCV5YBwyINACkDaAZAcQBkJg7AqrUBxjIAAAAAAAAAhAEwAgAAAAAAABfA/nasDaibpmnb9ugb7uf7OgCgz8m7PhBgNrUzfX+nCbj3KwIe9aKAblUY/YEA/v1BAGdGvwtwXhNOfwgAq98F4J0cAAAAAAAAAAAIALhI9zt/+VQHyAqu3/HfMQA/DrgBjA68XA2O8ZsAAAAASUVORK5CYIKJUE5HDQoaCgAAAA1JSERSAAAA/wAAAP8IAwAAAAnW8PgAAAMAUExURQAAAHzB8wCA/3O98nvB82q48kan7kWn7me38W678kSm7my58oDD9EKm7m268kyq70qp70ip74bG9Fev8E6r73S9833C82K18V2y8FCs70uq70Kl7kmp72S28Vew8InH9HrA82i38VSu8IjH9Ha+82u58kOm7mO18Wi48oLE9AJf+Ymu33Wg2mua116Q1FOJ0UqDzkB8zAJNyAJV35W2412Q1DNzyGOU1S1vx3Of2ixuxpO14jV0yZGz4TFxyIqu4D56y4Kp3UuDzy5wxydrxSRpxCZqxSxvxzJyyEaAzSttxlmN03yl3Hij2wBszgCE5lm5/yhsxYGp3VaL0iVpxH2m3EV/zY+y4W2a2FeL0j97zCpsxv/yADqs/0Gv/4qKAK6uACBfvSxnwTdvxEN4yBhZuk6Ay2eS0oqr3RlauztyxXd3AHed1hpZu0N3x4ur3BlZuk5/yiFfvX2h2B5dvHOa1Rxbu3BXAYFkAbqRAf/JDi9owVKByyFevW6W1D5zxSlkviNfvB1buxlYuR1auolqASRgvStlv0R3xnuf1yZhvV2JzjVswoeo2yFdvIuq3I+t3SxlvmyU0iFdu12JzSVgvJKv3leEyypjvoSl2W+W02SO0FWCy0t7yEBzxTZswbaNAZSpzoCZxJKozYGaxXiTwXqUwlR2sG6KvD1jpneSwH6Xw4efyIScxpis0IOcxgAAALGxsbKysrOzs7S0tLW1tba2tre3t7i4uLm5ubq6uru7u7y8vL29vb6+vr+/v8DAwMHBwcLCwsPDw8TExMXFxcbGxsfHx8jIyMnJycrKysvLy8zMzM3Nzc7Ozs/Pz9DQ0NHR0dLS0tPT09TU1NXV1dbW1tfX19jY2NnZ2dra2tvb29zc3N3d3d7e3t/f3+Dg4OHh4eLi4uPj4+Tk5OXl5ebm5ufn5+jo6Onp6erq6uvr6+zs7O3t7e7u7u/v7/Dw8PHx8fLy8vPz8/T09PX19fb29vf39/j4+Pn5+fr6+vv7+/z8/P39/f7+/v////S9KF4AAACxdFJOU///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////ANf0XGQAAANLSURBVHic7d07bhRBFIXhkrfhHRAOG0AsAFhAS5CQkrZN7n04ISBBs0SkHjyGflXVVNGnbt3/hHZ163zHrZFf0oSz7wR1AXGCuoA4QV1AnKAuIE5QFxAnqAuIE9QFxAlV7nJnLFX9asxtqeVXO25PFb8aUZL7cr+aUJZivxpQGu/+uzK/un15vPvvS/zq8jWCHz9+/Pjx48ePHz9+/Pjx48ePHz9+/Pjx48ePHz9+/Pjxq7vXCH78+PHjx48/L28qxrtftUA7fs0CLfkVA+BvyC8Y4MV/EuTtJdIBLv53Cv51AblfpD8tHwGJX8dfDKDwK/nzAQR+LX/2GuDQf/ow5eOUT0cnvFfzxX61Hj9+/Pjx48ePHz9+/Pjx48eP/0j/kJJZ+9jn4+eM+WdCh/5/jIn+nWMG/X/XTxugN/+QIuvZP2xflMe36t8eAH+U34M/Y4DdE2b9Q4ou+uXv0J/3PaJdf+oD4Nwf+bR9f0TYrz/pAdierXn/aZZkf85PSIb8ixMpVzr3R2/ag3/nUuf++D278Ke/NOL35I/fshP/xsXO/YsP9utfvTqBj79X/5D2u/Fe/CuXO/cn8fvxxwfA37U/NsAqH78df+xAb/5oogPF+W78G3zL/oXFu3/vFs79W3zD/jVNvv/zlC9TchsUp8b/P+BPuMkm36x/g5N32q5/i5N32qx/25N53KZ/x5N53KR/z7N2m778u/ru/RF92h89bPij1MQB8OPHjx8/fvz48ePHjx8/fvz48ePHjx//0cGPHz9+YfDjx48fP378+PHjx48fP378+PHj/5/+r8796mj939R8sV///qfO/ePDlMcp34+O/P2P9X7tAKPerxxgbMGvG2Bswy9aYByb8d+SsUou/Cf8Pv1/+F79L3yn/ivfpf9Vb9L/VDMaflv+4/n4G/IL+A35Ffp2/M8afpH/uWJEfPxt+FX8RvwyfhN+nb4Fv1Jf5tc2rxP8+PHjx48fP378+PHjx48fP378+PHjx48fP378+HsawLn/XOT/oa5fnDK/+QfgXOg3PsDPYr/tAc7lfssDnGv4zQ5waV/ut7jBr2vzOn67CeoC4gR1AXGCuoA4QV1AnKAuIE5QFxAnqAuIE9QFxPkNIdpWd4D38T0AAAAASUVORK5CYII="