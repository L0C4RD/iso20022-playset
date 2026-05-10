import base_types
import SecurityIdentification25Choice
import RedemptionCompletion1Code
import ISODate
import Max350Text
import GateHoldBack1Code
import ActiveCurrencyAndAmount

class HoldBackInformation3(base_types._BaseFieldType):

	__slots__ = ["_RedCmpltn", "_FinInstrmNm", "_Amt", "_XpctdRlsDt", "_Tp", "_FinInstrmId"]
	@property
	def RedCmpltn(self):
		return self._RedCmpltn

	@RedCmpltn.setter
	def RedCmpltn(self, value):
		self._RedCmpltn = value if type(value) != auto else self.make_default("RedCmpltn")

	@RedCmpltn.deleter
	def RedCmpltn(self):
		del self._RedCmpltn
		self._RedCmpltn = None

	@property
	def FinInstrmNm(self):
		return self._FinInstrmNm

	@FinInstrmNm.setter
	def FinInstrmNm(self, value):
		self._FinInstrmNm = value if type(value) != auto else self.make_default("FinInstrmNm")

	@FinInstrmNm.deleter
	def FinInstrmNm(self):
		del self._FinInstrmNm
		self._FinInstrmNm = None

	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

	@property
	def XpctdRlsDt(self):
		return self._XpctdRlsDt

	@XpctdRlsDt.setter
	def XpctdRlsDt(self, value):
		self._XpctdRlsDt = value if type(value) != auto else self.make_default("XpctdRlsDt")

	@XpctdRlsDt.deleter
	def XpctdRlsDt(self):
		del self._XpctdRlsDt
		self._XpctdRlsDt = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if type(value) != auto else self.make_default("FinInstrmId")

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RedCmpltn', type=RedemptionCompletion1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmNm', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpctdRlsDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=GateHoldBack1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification25Choice, min=0, max=1, mutex_group=None, array=False),
	))

