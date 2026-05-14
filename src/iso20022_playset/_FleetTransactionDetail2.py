from . import base_types
from ._FleetPurchaseType1Code import FleetPurchaseType1Code
from ._ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount
from ._Max35Text import Max35Text
from ._Tax44 import Tax44

class FleetTransactionDetail2(base_types._BaseFieldType):

	__slots__ = ["_DscntTtlAmt", "_DscntTtlFuelAmt", "_DscntTtlNonFuelAmt", "_PurchsTp", "_SummryCmmdtyId", "_TaxTtl", "_TtlAmt"]
	@property
	def DscntTtlAmt(self):
		return self._DscntTtlAmt

	@DscntTtlAmt.setter
	def DscntTtlAmt(self, value):
		self._DscntTtlAmt = value if type(value) != base_types.auto else self.make_default("DscntTtlAmt")

	@DscntTtlAmt.deleter
	def DscntTtlAmt(self):
		del self._DscntTtlAmt
		self._DscntTtlAmt = None

	@property
	def DscntTtlFuelAmt(self):
		return self._DscntTtlFuelAmt

	@DscntTtlFuelAmt.setter
	def DscntTtlFuelAmt(self, value):
		self._DscntTtlFuelAmt = value if type(value) != base_types.auto else self.make_default("DscntTtlFuelAmt")

	@DscntTtlFuelAmt.deleter
	def DscntTtlFuelAmt(self):
		del self._DscntTtlFuelAmt
		self._DscntTtlFuelAmt = None

	@property
	def DscntTtlNonFuelAmt(self):
		return self._DscntTtlNonFuelAmt

	@DscntTtlNonFuelAmt.setter
	def DscntTtlNonFuelAmt(self, value):
		self._DscntTtlNonFuelAmt = value if type(value) != base_types.auto else self.make_default("DscntTtlNonFuelAmt")

	@DscntTtlNonFuelAmt.deleter
	def DscntTtlNonFuelAmt(self):
		del self._DscntTtlNonFuelAmt
		self._DscntTtlNonFuelAmt = None

	@property
	def PurchsTp(self):
		return self._PurchsTp

	@PurchsTp.setter
	def PurchsTp(self, value):
		self._PurchsTp = value if type(value) != base_types.auto else self.make_default("PurchsTp")

	@PurchsTp.deleter
	def PurchsTp(self):
		del self._PurchsTp
		self._PurchsTp = None

	@property
	def SummryCmmdtyId(self):
		return self._SummryCmmdtyId

	@SummryCmmdtyId.setter
	def SummryCmmdtyId(self, value):
		self._SummryCmmdtyId = value if type(value) != base_types.auto else self.make_default("SummryCmmdtyId")

	@SummryCmmdtyId.deleter
	def SummryCmmdtyId(self):
		del self._SummryCmmdtyId
		self._SummryCmmdtyId = None

	@property
	def TaxTtl(self):
		return self._TaxTtl

	@TaxTtl.setter
	def TaxTtl(self, value):
		self._TaxTtl = value if type(value) != base_types.auto else self.make_default("TaxTtl")

	@TaxTtl.deleter
	def TaxTtl(self):
		del self._TaxTtl
		self._TaxTtl = None

	@property
	def TtlAmt(self):
		return self._TtlAmt

	@TtlAmt.setter
	def TtlAmt(self, value):
		self._TtlAmt = value if type(value) != base_types.auto else self.make_default("TtlAmt")

	@TtlAmt.deleter
	def TtlAmt(self):
		del self._TtlAmt
		self._TtlAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DscntTtlAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DscntTtlFuelAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DscntTtlNonFuelAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PurchsTp', type=FleetPurchaseType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SummryCmmdtyId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxTtl', type=Tax44, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TtlAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))

