x_ = int(input())
y_ = int(input())
upto_y_ = int(input())
per_over = int(input())
used = int(input())

on_x = used * x_
on_y = y_ if used <= upto_y_ else (used - upto_y_) * per_over + y_
print(min(on_x, on_y))
