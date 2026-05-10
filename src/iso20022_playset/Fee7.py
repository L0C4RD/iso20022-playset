from . import base_types
from .ChargeBearer1Code import ChargeBearer1Code
from .ChargeOrCommissionDiscount2 import ChargeOrCommissionDiscount2
from .ChargeBasis2Choice import ChargeBasis2Choice
from .ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from .ChargeType6Choice import ChargeType6Choice
from .PartyIdentification139 import PartyIdentification139

class Fee7(base_types._BaseFieldType):

	__slots__ = ["_DscntDtls", "_Bsis", "_ChrgBr", "_Tp", "_Amt", "_RcptId"]
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
	def ChrgBr(self):
		return self._ChrgBr

	@ChrgBr.setter
	def ChrgBr(self, value):
		self._ChrgBr = value if type(value) != base_types.auto else self.make_default("ChrgBr")

	@ChrgBr.deleter
	def ChrgBr(self):
		del self._ChrgBr
		self._ChrgBr = None

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
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != base_types.auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='DscntDtls', type=ChargeOrCommissionDiscount2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Bsis', type=ChargeBasis2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgBr', type=ChargeBearer1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=ChargeType6Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcptId', type=PartyIdentification139, min=0, max=1, mutex_group=None, array=False),
	))

