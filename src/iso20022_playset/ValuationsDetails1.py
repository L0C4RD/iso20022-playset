import base_types
import ValuationFactorBreakdown1
import CollateralAmount4
import MarketIdentification89
import ActiveOrHistoricCurrencyAndAmount
import Number
import DateAndDateTime2Choice
import Price7

class ValuationsDetails1(base_types._BaseFieldType):

	__slots__ = ["_SrcOfPric", "_SttlmDt", "_MktPric", "_QtnAge", "_ValtnDtlsAmt", "_ValtnFctrBrkdwn", "_CleanPric", "_NbOfDaysAcrd", "_AcrdIntrst"]
	@property
	def SrcOfPric(self):
		return self._SrcOfPric

	@SrcOfPric.setter
	def SrcOfPric(self, value):
		self._SrcOfPric = value if type(value) != auto else self.make_default("SrcOfPric")

	@SrcOfPric.deleter
	def SrcOfPric(self):
		del self._SrcOfPric
		self._SrcOfPric = None

	@property
	def SttlmDt(self):
		return self._SttlmDt

	@SttlmDt.setter
	def SttlmDt(self, value):
		self._SttlmDt = value if type(value) != auto else self.make_default("SttlmDt")

	@SttlmDt.deleter
	def SttlmDt(self):
		del self._SttlmDt
		self._SttlmDt = None

	@property
	def MktPric(self):
		return self._MktPric

	@MktPric.setter
	def MktPric(self, value):
		self._MktPric = value if type(value) != auto else self.make_default("MktPric")

	@MktPric.deleter
	def MktPric(self):
		del self._MktPric
		self._MktPric = None

	@property
	def QtnAge(self):
		return self._QtnAge

	@QtnAge.setter
	def QtnAge(self, value):
		self._QtnAge = value if type(value) != auto else self.make_default("QtnAge")

	@QtnAge.deleter
	def QtnAge(self):
		del self._QtnAge
		self._QtnAge = None

	@property
	def ValtnDtlsAmt(self):
		return self._ValtnDtlsAmt

	@ValtnDtlsAmt.setter
	def ValtnDtlsAmt(self, value):
		self._ValtnDtlsAmt = value if type(value) != auto else self.make_default("ValtnDtlsAmt")

	@ValtnDtlsAmt.deleter
	def ValtnDtlsAmt(self):
		del self._ValtnDtlsAmt
		self._ValtnDtlsAmt = None

	@property
	def ValtnFctrBrkdwn(self):
		return self._ValtnFctrBrkdwn

	@ValtnFctrBrkdwn.setter
	def ValtnFctrBrkdwn(self, value):
		self._ValtnFctrBrkdwn = value if type(value) != auto else self.make_default("ValtnFctrBrkdwn")

	@ValtnFctrBrkdwn.deleter
	def ValtnFctrBrkdwn(self):
		del self._ValtnFctrBrkdwn
		self._ValtnFctrBrkdwn = None

	@property
	def CleanPric(self):
		return self._CleanPric

	@CleanPric.setter
	def CleanPric(self, value):
		self._CleanPric = value if type(value) != auto else self.make_default("CleanPric")

	@CleanPric.deleter
	def CleanPric(self):
		del self._CleanPric
		self._CleanPric = None

	@property
	def NbOfDaysAcrd(self):
		return self._NbOfDaysAcrd

	@NbOfDaysAcrd.setter
	def NbOfDaysAcrd(self, value):
		self._NbOfDaysAcrd = value if type(value) != auto else self.make_default("NbOfDaysAcrd")

	@NbOfDaysAcrd.deleter
	def NbOfDaysAcrd(self):
		del self._NbOfDaysAcrd
		self._NbOfDaysAcrd = None

	@property
	def AcrdIntrst(self):
		return self._AcrdIntrst

	@AcrdIntrst.setter
	def AcrdIntrst(self, value):
		self._AcrdIntrst = value if type(value) != auto else self.make_default("AcrdIntrst")

	@AcrdIntrst.deleter
	def AcrdIntrst(self):
		del self._AcrdIntrst
		self._AcrdIntrst = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SrcOfPric', type=MarketIdentification89, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktPric', type=Price7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QtnAge', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValtnDtlsAmt', type=CollateralAmount4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValtnFctrBrkdwn', type=ValuationFactorBreakdown1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CleanPric', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfDaysAcrd', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcrdIntrst', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))

