# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import Fee2
from . import Max35Text
from . import Tax31

class TotalFeesAndTaxes40(base_types._BaseFieldType):

	__slots__ = ["_ComrclAgrmtRef", "_IndvFee", "_IndvTax", "_TtlFees", "_TtlOvrhdApld", "_TtlTaxs"]
	@property
	def ComrclAgrmtRef(self):
		return self._ComrclAgrmtRef

	@ComrclAgrmtRef.setter
	def ComrclAgrmtRef(self, value):
		self._ComrclAgrmtRef = value if value is not None else base_types.UninitialisedField(self, 'ComrclAgrmtRef', Max35Text, False)

	@ComrclAgrmtRef.deleter
	def ComrclAgrmtRef(self):
		del self._ComrclAgrmtRef
		self._ComrclAgrmtRef = base_types.UninitialisedField(self, 'ComrclAgrmtRef', Max35Text, False)

	@property
	def IndvFee(self):
		return self._IndvFee

	@IndvFee.setter
	def IndvFee(self, value):
		self._IndvFee = value if value is not None else base_types.UninitialisedField(self, 'IndvFee', Fee2, True)

	@IndvFee.deleter
	def IndvFee(self):
		del self._IndvFee
		self._IndvFee = base_types.UninitialisedField(self, 'IndvFee', Fee2, True)

	@property
	def IndvTax(self):
		return self._IndvTax

	@IndvTax.setter
	def IndvTax(self, value):
		self._IndvTax = value if value is not None else base_types.UninitialisedField(self, 'IndvTax', Tax31, True)

	@IndvTax.deleter
	def IndvTax(self):
		del self._IndvTax
		self._IndvTax = base_types.UninitialisedField(self, 'IndvTax', Tax31, True)

	@property
	def TtlFees(self):
		return self._TtlFees

	@TtlFees.setter
	def TtlFees(self, value):
		self._TtlFees = value if value is not None else base_types.UninitialisedField(self, 'TtlFees', ActiveCurrencyAndAmount, False)

	@TtlFees.deleter
	def TtlFees(self):
		del self._TtlFees
		self._TtlFees = base_types.UninitialisedField(self, 'TtlFees', ActiveCurrencyAndAmount, False)

	@property
	def TtlOvrhdApld(self):
		return self._TtlOvrhdApld

	@TtlOvrhdApld.setter
	def TtlOvrhdApld(self, value):
		self._TtlOvrhdApld = value if value is not None else base_types.UninitialisedField(self, 'TtlOvrhdApld', ActiveCurrencyAndAmount, False)

	@TtlOvrhdApld.deleter
	def TtlOvrhdApld(self):
		del self._TtlOvrhdApld
		self._TtlOvrhdApld = base_types.UninitialisedField(self, 'TtlOvrhdApld', ActiveCurrencyAndAmount, False)

	@property
	def TtlTaxs(self):
		return self._TtlTaxs

	@TtlTaxs.setter
	def TtlTaxs(self, value):
		self._TtlTaxs = value if value is not None else base_types.UninitialisedField(self, 'TtlTaxs', ActiveCurrencyAndAmount, False)

	@TtlTaxs.deleter
	def TtlTaxs(self):
		del self._TtlTaxs
		self._TtlTaxs = base_types.UninitialisedField(self, 'TtlTaxs', ActiveCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ComrclAgrmtRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IndvFee', type=Fee2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='IndvTax', type=Tax31, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TtlFees', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlOvrhdApld', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlTaxs', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))