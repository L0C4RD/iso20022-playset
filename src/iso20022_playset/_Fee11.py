from . import base_types
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._ChargeBasis2Choice import ChargeBasis2Choice
from ._ChargeOrCommissionDiscount1 import ChargeOrCommissionDiscount1
from ._ChargeType10Choice import ChargeType10Choice
from ._Max35Text import Max35Text
from ._PartyIdentification139 import PartyIdentification139
from ._PercentageRate import PercentageRate
from ._YesNoIndicator import YesNoIndicator

class Fee11(base_types._BaseFieldType):

	__slots__ = ["_ApldAmt", "_ApldRate", "_Bsis", "_DscntDtls", "_InftvInd", "_NonStdSLARef", "_RcptId", "_StdAmt", "_StdRate", "_Tp"]
	@property
	def ApldAmt(self):
		return self._ApldAmt

	@ApldAmt.setter
	def ApldAmt(self, value):
		self._ApldAmt = value if type(value) != base_types.auto else self.make_default("ApldAmt")

	@ApldAmt.deleter
	def ApldAmt(self):
		del self._ApldAmt
		self._ApldAmt = None

	@property
	def ApldRate(self):
		return self._ApldRate

	@ApldRate.setter
	def ApldRate(self, value):
		self._ApldRate = value if type(value) != base_types.auto else self.make_default("ApldRate")

	@ApldRate.deleter
	def ApldRate(self):
		del self._ApldRate
		self._ApldRate = None

	@property
	def Bsis(self):
		return self._Bsis

	@Bsis.setter
	def Bsis(self, value):
		self._Bsis = value if type(value) != base_types.auto else self.make_default("Bsis")

	@Bsis.deleter
	def Bsis(self):
		del self._Bsis
		self._Bsis = None

	@property
	def DscntDtls(self):
		return self._DscntDtls

	@DscntDtls.setter
	def DscntDtls(self, value):
		self._DscntDtls = value if type(value) != base_types.auto else self.make_default("DscntDtls")

	@DscntDtls.deleter
	def DscntDtls(self):
		del self._DscntDtls
		self._DscntDtls = None

	@property
	def InftvInd(self):
		return self._InftvInd

	@InftvInd.setter
	def InftvInd(self, value):
		self._InftvInd = value if type(value) != base_types.auto else self.make_default("InftvInd")

	@InftvInd.deleter
	def InftvInd(self):
		del self._InftvInd
		self._InftvInd = None

	@property
	def NonStdSLARef(self):
		return self._NonStdSLARef

	@NonStdSLARef.setter
	def NonStdSLARef(self, value):
		self._NonStdSLARef = value if type(value) != base_types.auto else self.make_default("NonStdSLARef")

	@NonStdSLARef.deleter
	def NonStdSLARef(self):
		del self._NonStdSLARef
		self._NonStdSLARef = None

	@property
	def RcptId(self):
		return self._RcptId

	@RcptId.setter
	def RcptId(self, value):
		self._RcptId = value if type(value) != base_types.auto else self.make_default("RcptId")

	@RcptId.deleter
	def RcptId(self):
		del self._RcptId
		self._RcptId = None

	@property
	def StdAmt(self):
		return self._StdAmt

	@StdAmt.setter
	def StdAmt(self, value):
		self._StdAmt = value if type(value) != base_types.auto else self.make_default("StdAmt")

	@StdAmt.deleter
	def StdAmt(self):
		del self._StdAmt
		self._StdAmt = None

	@property
	def StdRate(self):
		return self._StdRate

	@StdRate.setter
	def StdRate(self, value):
		self._StdRate = value if type(value) != base_types.auto else self.make_default("StdRate")

	@StdRate.deleter
	def StdRate(self):
		del self._StdRate
		self._StdRate = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ApldAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ApldRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Bsis', type=ChargeBasis2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DscntDtls', type=ChargeOrCommissionDiscount1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InftvInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonStdSLARef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcptId', type=PartyIdentification139, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StdAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StdRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=ChargeType10Choice, min=1, max=1, mutex_group=None, array=False),
	))

