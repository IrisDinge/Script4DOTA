import re
import os

fn = open('/home/dingjin/tra_val_416.txt', 'r')
fn = fn.read()
fn = fn.replace(',',' ')
s = open('/home/dingjin/tra_val.txt', 'w+')

s = s.write(fn)


