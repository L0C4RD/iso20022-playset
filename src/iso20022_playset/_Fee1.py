from . import base_types
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._ChargeBasis2Choice import ChargeBasis2Choice
from ._ChargeOrCommissionDiscount1 import ChargeOrCommissionDiscount1
from ._ChargeType5Choice import ChargeType5Choice
from ._Max35Text import Max35Text
from ._PercentageRate import PercentageRate
from ._PartyIdentification113 import PartyIdentification113

class Fee1(base_types._BaseFieldType):

	__slots__ = ["_StdRate", "_StdAmt", "_ReqdAmt", "_Tp", "_RcptId", "_ReqdRate", "_DscntDtls", "_NonStdSLARef", "_Bsis"]
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
	def ReqdAmt(self):
		return self._ReqdAmt

	@ReqdAmt.setter
	def ReqdAmt(self, value):
		self._ReqdAmt = value if type(value) != base_types.auto else self.make_default("ReqdAmt")

	@ReqdAmt.deleter
	def ReqdAmt(self):
		del self._ReqdAmt
		self._ReqdAmt = None

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
	def ReqdRate(self):
		return self._ReqdRate

	@ReqdRate.setter
	def ReqdRate(self, value):
		self._ReqdRate = value if type(value) != base_types.auto else self.make_default("ReqdRate")

	@ReqdRate.deleter
	def ReqdRate(self):
		del self._ReqdRate
		self._ReqdRate = None

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
	def Bsis(self):
		return self._Bsis

	@Bsis.setter
	def Bsis(self, value):
		self._Bsis = value if type(value) != base_types.auto else self.make_default("Bsis")

	@Bsis.deleter
	def Bsis(self):
		del self._Bsis
		self._Bsis = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='StdRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StdAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=ChargeType5Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcptId', type=PartyIdentification113, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DscntDtls', type=ChargeOrCommissionDiscount1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonStdSLARef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Bsis', type=ChargeBasis2Choice, min=0, max=1, mutex_group=None, array=False),
	))

