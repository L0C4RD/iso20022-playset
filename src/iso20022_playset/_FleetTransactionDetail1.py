# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FleetPurchaseType1Code
from . import ImpliedCurrencyAndAmount
from . import Max35Text
from . import Tax41

class FleetTransactionDetail1(base_types._BaseFieldType):

	__slots__ = ["_DscntTtlAmt", "_DscntTtlFuelAmt", "_DscntTtlNonFuelAmt", "_PurchsTp", "_SummryCmmdtyId", "_TaxTtl", "_TtlAmt"]
	@property
	def DscntTtlAmt(self):
		return self._DscntTtlAmt

	@DscntTtlAmt.setter
	def DscntTtlAmt(self, value):
		self._DscntTtlAmt = value if value is not None else base_types.UninitialisedField(self, 'DscntTtlAmt', ImpliedCurrencyAndAmount, False)

	@DscntTtlAmt.deleter
	def DscntTtlAmt(self):
		del self._DscntTtlAmt
		self._DscntTtlAmt = base_types.UninitialisedField(self, 'DscntTtlAmt', ImpliedCurrencyAndAmount, False)

	@property
	def DscntTtlFuelAmt(self):
		return self._DscntTtlFuelAmt

	@DscntTtlFuelAmt.setter
	def DscntTtlFuelAmt(self, value):
		self._DscntTtlFuelAmt = value if value is not None else base_types.UninitialisedField(self, 'DscntTtlFuelAmt', ImpliedCurrencyAndAmount, False)

	@DscntTtlFuelAmt.deleter
	def DscntTtlFuelAmt(self):
		del self._DscntTtlFuelAmt
		self._DscntTtlFuelAmt = base_types.UninitialisedField(self, 'DscntTtlFuelAmt', ImpliedCurrencyAndAmount, False)

	@property
	def DscntTtlNonFuelAmt(self):
		return self._DscntTtlNonFuelAmt

	@DscntTtlNonFuelAmt.setter
	def DscntTtlNonFuelAmt(self, value):
		self._DscntTtlNonFuelAmt = value if value is not None else base_types.UninitialisedField(self, 'DscntTtlNonFuelAmt', ImpliedCurrencyAndAmount, False)

	@DscntTtlNonFuelAmt.deleter
	def DscntTtlNonFuelAmt(self):
		del self._DscntTtlNonFuelAmt
		self._DscntTtlNonFuelAmt = base_types.UninitialisedField(self, 'DscntTtlNonFuelAmt', ImpliedCurrencyAndAmount, False)

	@property
	def PurchsTp(self):
		return self._PurchsTp

	@PurchsTp.setter
	def PurchsTp(self, value):
		self._PurchsTp = value if value is not None else base_types.UninitialisedField(self, 'PurchsTp', FleetPurchaseType1Code, False)

	@PurchsTp.deleter
	def PurchsTp(self):
		del self._PurchsTp
		self._PurchsTp = base_types.UninitialisedField(self, 'PurchsTp', FleetPurchaseType1Code, False)

	@property
	def SummryCmmdtyId(self):
		return self._SummryCmmdtyId

	@SummryCmmdtyId.setter
	def SummryCmmdtyId(self, value):
		self._SummryCmmdtyId = value if value is not None else base_types.UninitialisedField(self, 'SummryCmmdtyId', Max35Text, False)

	@SummryCmmdtyId.deleter
	def SummryCmmdtyId(self):
		del self._SummryCmmdtyId
		self._SummryCmmdtyId = base_types.UninitialisedField(self, 'SummryCmmdtyId', Max35Text, False)

	@property
	def TaxTtl(self):
		return self._TaxTtl

	@TaxTtl.setter
	def TaxTtl(self, value):
		self._TaxTtl = value if value is not None else base_types.UninitialisedField(self, 'TaxTtl', Tax41, True)

	@TaxTtl.deleter
	def TaxTtl(self):
		del self._TaxTtl
		self._TaxTtl = base_types.UninitialisedField(self, 'TaxTtl', Tax41, True)

	@property
	def TtlAmt(self):
		return self._TtlAmt

	@TtlAmt.setter
	def TtlAmt(self, value):
		self._TtlAmt = value if value is not None else base_types.UninitialisedField(self, 'TtlAmt', ImpliedCurrencyAndAmount, False)

	@TtlAmt.deleter
	def TtlAmt(self):
		del self._TtlAmt
		self._TtlAmt = base_types.UninitialisedField(self, 'TtlAmt', ImpliedCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DscntTtlAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DscntTtlFuelAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DscntTtlNonFuelAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PurchsTp', type=FleetPurchaseType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SummryCmmdtyId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxTtl', type=Tax41, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TtlAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))