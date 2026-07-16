# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyAndAmount
from . import CollateralAmount4
from . import DateAndDateTime2Choice
from . import MarketIdentification89
from . import Number
from . import Price7
from . import ValuationFactorBreakdown1

class ValuationsDetails1(base_types._BaseFieldType):

	__slots__ = ["_AcrdIntrst", "_CleanPric", "_MktPric", "_NbOfDaysAcrd", "_QtnAge", "_SrcOfPric", "_SttlmDt", "_ValtnDtlsAmt", "_ValtnFctrBrkdwn"]
	@property
	def AcrdIntrst(self):
		return self._AcrdIntrst

	@AcrdIntrst.setter
	def AcrdIntrst(self, value):
		self._AcrdIntrst = value if value is not None else base_types.UninitialisedField(self, 'AcrdIntrst', ActiveOrHistoricCurrencyAndAmount, False)

	@AcrdIntrst.deleter
	def AcrdIntrst(self):
		del self._AcrdIntrst
		self._AcrdIntrst = base_types.UninitialisedField(self, 'AcrdIntrst', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def CleanPric(self):
		return self._CleanPric

	@CleanPric.setter
	def CleanPric(self, value):
		self._CleanPric = value if value is not None else base_types.UninitialisedField(self, 'CleanPric', ActiveOrHistoricCurrencyAndAmount, False)

	@CleanPric.deleter
	def CleanPric(self):
		del self._CleanPric
		self._CleanPric = base_types.UninitialisedField(self, 'CleanPric', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def MktPric(self):
		return self._MktPric

	@MktPric.setter
	def MktPric(self, value):
		self._MktPric = value if value is not None else base_types.UninitialisedField(self, 'MktPric', Price7, False)

	@MktPric.deleter
	def MktPric(self):
		del self._MktPric
		self._MktPric = base_types.UninitialisedField(self, 'MktPric', Price7, False)

	@property
	def NbOfDaysAcrd(self):
		return self._NbOfDaysAcrd

	@NbOfDaysAcrd.setter
	def NbOfDaysAcrd(self, value):
		self._NbOfDaysAcrd = value if value is not None else base_types.UninitialisedField(self, 'NbOfDaysAcrd', Number, False)

	@NbOfDaysAcrd.deleter
	def NbOfDaysAcrd(self):
		del self._NbOfDaysAcrd
		self._NbOfDaysAcrd = base_types.UninitialisedField(self, 'NbOfDaysAcrd', Number, False)

	@property
	def QtnAge(self):
		return self._QtnAge

	@QtnAge.setter
	def QtnAge(self, value):
		self._QtnAge = value if value is not None else base_types.UninitialisedField(self, 'QtnAge', Number, False)

	@QtnAge.deleter
	def QtnAge(self):
		del self._QtnAge
		self._QtnAge = base_types.UninitialisedField(self, 'QtnAge', Number, False)

	@property
	def SrcOfPric(self):
		return self._SrcOfPric

	@SrcOfPric.setter
	def SrcOfPric(self, value):
		self._SrcOfPric = value if value is not None else base_types.UninitialisedField(self, 'SrcOfPric', MarketIdentification89, False)

	@SrcOfPric.deleter
	def SrcOfPric(self):
		del self._SrcOfPric
		self._SrcOfPric = base_types.UninitialisedField(self, 'SrcOfPric', MarketIdentification89, False)

	@property
	def SttlmDt(self):
		return self._SttlmDt

	@SttlmDt.setter
	def SttlmDt(self, value):
		self._SttlmDt = value if value is not None else base_types.UninitialisedField(self, 'SttlmDt', DateAndDateTime2Choice, False)

	@SttlmDt.deleter
	def SttlmDt(self):
		del self._SttlmDt
		self._SttlmDt = base_types.UninitialisedField(self, 'SttlmDt', DateAndDateTime2Choice, False)

	@property
	def ValtnDtlsAmt(self):
		return self._ValtnDtlsAmt

	@ValtnDtlsAmt.setter
	def ValtnDtlsAmt(self, value):
		self._ValtnDtlsAmt = value if value is not None else base_types.UninitialisedField(self, 'ValtnDtlsAmt', CollateralAmount4, False)

	@ValtnDtlsAmt.deleter
	def ValtnDtlsAmt(self):
		del self._ValtnDtlsAmt
		self._ValtnDtlsAmt = base_types.UninitialisedField(self, 'ValtnDtlsAmt', CollateralAmount4, False)

	@property
	def ValtnFctrBrkdwn(self):
		return self._ValtnFctrBrkdwn

	@ValtnFctrBrkdwn.setter
	def ValtnFctrBrkdwn(self, value):
		self._ValtnFctrBrkdwn = value if value is not None else base_types.UninitialisedField(self, 'ValtnFctrBrkdwn', ValuationFactorBreakdown1, False)

	@ValtnFctrBrkdwn.deleter
	def ValtnFctrBrkdwn(self):
		del self._ValtnFctrBrkdwn
		self._ValtnFctrBrkdwn = base_types.UninitialisedField(self, 'ValtnFctrBrkdwn', ValuationFactorBreakdown1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcrdIntrst', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CleanPric', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktPric', type=Price7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfDaysAcrd', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QtnAge', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SrcOfPric', type=MarketIdentification89, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValtnDtlsAmt', type=CollateralAmount4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValtnFctrBrkdwn', type=ValuationFactorBreakdown1, min=1, max=1, mutex_group=None, array=False),
	))