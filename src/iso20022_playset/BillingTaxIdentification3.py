from . import base_types
from .Contact13 import Contact13
from .Max35Text import Max35Text

class BillingTaxIdentification3(base_types._BaseFieldType):

	__slots__ = ["_TaxRegnNb", "_VATRegnNb", "_TaxCtct"]
	@property
	def TaxRegnNb(self):
		return self._TaxRegnNb

	@TaxRegnNb.setter
	def TaxRegnNb(self, value):
		self._TaxRegnNb = value if type(value) != base_types.auto else self.make_default("TaxRegnNb")

	@TaxRegnNb.deleter
	def TaxRegnNb(self):
		del self._TaxRegnNb
		self._TaxRegnNb = None

	@property
	def VATRegnNb(self):
		return self._VATRegnNb

	@VATRegnNb.setter
	def VATRegnNb(self, value):
		self._VATRegnNb = value if type(value) != base_types.auto else self.make_default("VATRegnNb")

	@VATRegnNb.deleter
	def VATRegnNb(self):
		del self._VATRegnNb
		self._VATRegnNb = None

	@property
	def TaxCtct(self):
		return self._TaxCtct

	@TaxCtct.setter
	def TaxCtct(self, value):
		self._TaxCtct = value if type(value) != base_types.auto else self.make_default("TaxCtct")

	@TaxCtct.deleter
	def TaxCtct(self):
		del self._TaxCtct
		self._TaxCtct = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TaxRegnNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VATRegnNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxCtct', type=Contact13, min=0, max=1, mutex_group=None, array=False),
	))

