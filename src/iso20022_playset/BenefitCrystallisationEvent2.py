import base_types
import Max35Text
import YesNoIndicator
import PercentageRate
import AdditionalInformation15
import ISODate
import ActiveCurrencyAnd13DecimalAmount

class BenefitCrystallisationEvent2(base_types._BaseFieldType):

	__slots__ = ["_LftmAllwncPrtcn", "_CrstllstnAmt", "_EvtTpNm", "_PctgOfAllwnc", "_EvtDt", "_AddtlInf", "_EvtTpNb"]
	@property
	def LftmAllwncPrtcn(self):
		return self._LftmAllwncPrtcn

	@LftmAllwncPrtcn.setter
	def LftmAllwncPrtcn(self, value):
		self._LftmAllwncPrtcn = value if type(value) != auto else self.make_default("LftmAllwncPrtcn")

	@LftmAllwncPrtcn.deleter
	def LftmAllwncPrtcn(self):
		del self._LftmAllwncPrtcn
		self._LftmAllwncPrtcn = None

	@property
	def CrstllstnAmt(self):
		return self._CrstllstnAmt

	@CrstllstnAmt.setter
	def CrstllstnAmt(self, value):
		self._CrstllstnAmt = value if type(value) != auto else self.make_default("CrstllstnAmt")

	@CrstllstnAmt.deleter
	def CrstllstnAmt(self):
		del self._CrstllstnAmt
		self._CrstllstnAmt = None

	@property
	def EvtTpNm(self):
		return self._EvtTpNm

	@EvtTpNm.setter
	def EvtTpNm(self, value):
		self._EvtTpNm = value if type(value) != auto else self.make_default("EvtTpNm")

	@EvtTpNm.deleter
	def EvtTpNm(self):
		del self._EvtTpNm
		self._EvtTpNm = None

	@property
	def PctgOfAllwnc(self):
		return self._PctgOfAllwnc

	@PctgOfAllwnc.setter
	def PctgOfAllwnc(self, value):
		self._PctgOfAllwnc = value if type(value) != auto else self.make_default("PctgOfAllwnc")

	@PctgOfAllwnc.deleter
	def PctgOfAllwnc(self):
		del self._PctgOfAllwnc
		self._PctgOfAllwnc = None

	@property
	def EvtDt(self):
		return self._EvtDt

	@EvtDt.setter
	def EvtDt(self, value):
		self._EvtDt = value if type(value) != auto else self.make_default("EvtDt")

	@EvtDt.deleter
	def EvtDt(self):
		del self._EvtDt
		self._EvtDt = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def EvtTpNb(self):
		return self._EvtTpNb

	@EvtTpNb.setter
	def EvtTpNb(self, value):
		self._EvtTpNb = value if type(value) != auto else self.make_default("EvtTpNb")

	@EvtTpNb.deleter
	def EvtTpNb(self):
		del self._EvtTpNb
		self._EvtTpNb = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='LftmAllwncPrtcn', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrstllstnAmt', type=ActiveCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtTpNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PctgOfAllwnc', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='EvtTpNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

