import base_types
import Max35Text
import Fee5
import ActiveCurrencyAndAmount
import Tax35

class TotalFeesAndTaxes42(base_types._BaseFieldType):

	__slots__ = ["_TtlOvrhdApld", "_IndvTax", "_IndvFee", "_ComrclAgrmtRef", "_TtlFees", "_TtlTaxs"]
	@property
	def TtlOvrhdApld(self):
		return self._TtlOvrhdApld

	@TtlOvrhdApld.setter
	def TtlOvrhdApld(self, value):
		self._TtlOvrhdApld = value if type(value) != auto else self.make_default("TtlOvrhdApld")

	@TtlOvrhdApld.deleter
	def TtlOvrhdApld(self):
		del self._TtlOvrhdApld
		self._TtlOvrhdApld = None

	@property
	def IndvTax(self):
		return self._IndvTax

	@IndvTax.setter
	def IndvTax(self, value):
		self._IndvTax = value if type(value) != auto else self.make_default("IndvTax")

	@IndvTax.deleter
	def IndvTax(self):
		del self._IndvTax
		self._IndvTax = None

	@property
	def IndvFee(self):
		return self._IndvFee

	@IndvFee.setter
	def IndvFee(self, value):
		self._IndvFee = value if type(value) != auto else self.make_default("IndvFee")

	@IndvFee.deleter
	def IndvFee(self):
		del self._IndvFee
		self._IndvFee = None

	@property
	def ComrclAgrmtRef(self):
		return self._ComrclAgrmtRef

	@ComrclAgrmtRef.setter
	def ComrclAgrmtRef(self, value):
		self._ComrclAgrmtRef = value if type(value) != auto else self.make_default("ComrclAgrmtRef")

	@ComrclAgrmtRef.deleter
	def ComrclAgrmtRef(self):
		del self._ComrclAgrmtRef
		self._ComrclAgrmtRef = None

	@property
	def TtlFees(self):
		return self._TtlFees

	@TtlFees.setter
	def TtlFees(self, value):
		self._TtlFees = value if type(value) != auto else self.make_default("TtlFees")

	@TtlFees.deleter
	def TtlFees(self):
		del self._TtlFees
		self._TtlFees = None

	@property
	def TtlTaxs(self):
		return self._TtlTaxs

	@TtlTaxs.setter
	def TtlTaxs(self, value):
		self._TtlTaxs = value if type(value) != auto else self.make_default("TtlTaxs")

	@TtlTaxs.deleter
	def TtlTaxs(self):
		del self._TtlTaxs
		self._TtlTaxs = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TtlOvrhdApld', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IndvTax', type=Tax35, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='IndvFee', type=Fee5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ComrclAgrmtRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlFees', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlTaxs', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))

