# encoding: utf-8
import datetime,time;

INVS_REPAY_BY_MONTH = 1
INVS_REPAY_BY_DAYS 	= 2

class RepayMent(object):
	
	def __init__(self,repayDate,repayTerm,repayAmout)
		self.repayDate = repayDate
		self.repayTerm = repayTerm     # when INVS_REPAY_BY_MONTH,set -1
		self.repayAmout = repayAmout
	
class Investment(object):

	def __init__(self,invsDate,invsAmout,invsRatio,invsTerm,invsRepayWay):
		self.invsDate = invsDate
		self.invsAmout = invsAmout
		self.invsRatio = invsRatio
		self.invsTerm = invsTerm
		self.invsRepayWay = invsRepayWay
		
		## 还款计划表,默认为空
		self.invsRepayList = [];
		
		## Calculate the investment's end-time & totalRepayAmout
		if self.invsRepayWay == INVS_REPAY_BY_MONTH:
			if invsDate.month + invsTerm > 12:
				self.invsFiniDate = datetime.date(invsDate.year+1, invsDate.Month+invsTerm-12, invsDate.day)
			else:
				self.invsFiniDate = datetime.date(invsDate.year, invsDate.Month+invsTerm, invsDate.day)
			
			self.totalRepayAmout = invsAmout * invsRatio * invsTerm / 12
		else:
			self.invsFiniDate = self.invsDate + datetime.timedelta(invsTerm)
			self.totalRepayAmout = invsAmout * invsRatio * invsTerm / 365
		
	## 生产还款计划表
	def GenRepayList(self):

		if self.invsRepayWay == INVS_REPAY_BY_MONTH:
			if invsDate.month = 12:
				self.f1RepayDate = datetime.date(invsDate.year+1, 1, invsDate.day)
			else:
				self.f1RepayDate = datetime.date(invsDate.year, invsDate.Month+1, invsDate.day)
			
			for x in range(invsTerm):
			
				if f1RepayDate.month+x <=12:
					repayDate = datetime.date(f1RepayDate.year,f1RepayDate.month+x, invsDate.day)
				else:
					repayDate = datetime.date(f1RepayDate.year+1,f1RepayDate.month+x-12, invsDate.day)
				
				# self.totalRepayAmout = invsAmout * invsRatio * invsTerm / 12
				repayAmout = totalRepayAmout / invsTerm
				self.invsRepayList.append(RepayMent(repayDate, -1, repayAmout))	
			
		else:
			if invsDate.month = 12:
				self.f1RepayDate = datetime.date(invsDate.year+1, 1, 20)
			else:
				self.f1RepayDate = datetime.date(invsDate.year, invsDate.Month+1, 20)

			## 判断是否一次性派息
			payTimes = (invsFiniDate.year - f1RepayDate.year)*12 + invsFiniDate.month - f1RepayDate.month + 1
			if payTimes == 1:
				#结构化业务数据后放入容器中，便于迭代遍历
				self.invsRepayList.append(RepayMent(invsFiniDate, invsTerm, totalRepayAmout))
				print '一次性派息,派息日: ', invsFiniDate, ',计息天数:', invsTerm, ',利息：', totalRepayAmout
			else:
				#print payTimes,'程序猿哥哥看片去了...'
				lastPayDate = invsDate  
				for x in range(payTimes-1):
					# 计算派息日&派息金额

					# timedelta可以查看：天数(days)，秒数 (seconds)
					#repayDate = f1RepayDate + datetime.timedelta(months=x)
					if f1RepayDate.month+x <=12:
						repayDate = datetime.date(f1RepayDate.year, f1RepayDate.month+x, 20)
					else:
						repayDate = datetime.date(f1RepayDate.year+1, f1RepayDate.month+x-12, 20)
					repayDays = (repayDate - lastPayDate).days
					repayAmout = invsAmout * invsRatio * repayDays / 365
					self.invsRepayList.append(RepayMent(repayDate, repayDays, repayAmout))
					#print x, repayDate, repayAmout
					lastPayDate = repayDate
					
				# 最后一期派息
				repayDays = (invsFiniDate - lastPayDate).days
				repayAmout = invsAmout * invsRatio * repayDays / 365
				self.invsRepayList.append(RepayMent(invsFiniDate, repayDays, repayAmout))

		len = len(invsRepayList)
		n = 0
		while n<len:
			print n, '多次派息,派息日: ', invsRepayList[n].repayDate, ',计息天数:', invsRepayList[n].repayTerm, ',利息：', invsRepayList[n].repayAmout
			n = n + 1
		print '投资本金:', invsAmout, ';累计总收益:',  totalRepayAmout
	
