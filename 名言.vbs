dim students(12)
students(0)="曾经有一份真诚的爱情放在我面前，我没有珍惜，"&chr(10)&"等我失去的时候，我才后悔莫及，"&chr(10)&"人世间最痛苦的事莫过于此。"
students(1)="有一味绝境     非历十方生死"
students(2)="大丈夫身居天地之间，岂能郁郁久居人下？"
students(3)="我们永远无法还清犯下的……"
students(4)="大丈夫之志，应如长江东奔大海。何苦怀念温柔之乡？"
students(5)="出身寒微，不是耻辱，能屈能伸，方为丈夫。"
students(6)="大丈夫处世，碌碌无为，与朽木腐草何异？"
students(7)="年纪轻轻一遇挫折，便松散懈怠。日后怎成大器？"
students(8)="为人者，有大度成大器也！"
students(9)="大丈夫行于乱世，当光明磊落。"&chr(10)&"即使处于逆境，也当屈身受分，以待天时，不可与命抗争也。"
students(10)="天不亡我，我必逆天！"
students(11)="我命由我不由天！"
students(12)="偷偷地看你"&chr(10)&"偷偷地想你"&chr(10)&"偷偷地爱你"&chr(10)&"最后……"&chr(10)&"偷偷地哭了"
randomize
index=int((ubound(students)-lbound(students)+1)*rnd+lbound(students))
msgbox students(index)