# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Contact13
from . import Max35Text

class BillingTaxIdentification3(base_types._BaseFieldType):

	__slots__ = ["_TaxCtct", "_TaxRegnNb", "_VATRegnNb"]
	@property
	def TaxCtct(self):
		return self._TaxCtct

	@TaxCtct.setter
	def TaxCtct(self, value):
		self._TaxCtct = value if value is not None else base_types.UninitialisedField(self, 'TaxCtct', Contact13, False)

	@TaxCtct.deleter
	def TaxCtct(self):
		del self._TaxCtct
		self._TaxCtct = base_types.UninitialisedField(self, 'TaxCtct', Contact13, False)

	@property
	def TaxRegnNb(self):
		return self._TaxRegnNb

	@TaxRegnNb.setter
	def TaxRegnNb(self, value):
		self._TaxRegnNb = value if value is not None else base_types.UninitialisedField(self, 'TaxRegnNb', Max35Text, False)

	@TaxRegnNb.deleter
	def TaxRegnNb(self):
		del self._TaxRegnNb
		self._TaxRegnNb = base_types.UninitialisedField(self, 'TaxRegnNb', Max35Text, False)

	@property
	def VATRegnNb(self):
		return self._VATRegnNb

	@VATRegnNb.setter
	def VATRegnNb(self, value):
		self._VATRegnNb = value if value is not None else base_types.UninitialisedField(self, 'VATRegnNb', Max35Text, False)

	@VATRegnNb.deleter
	def VATRegnNb(self):
		del self._VATRegnNb
		self._VATRegnNb = base_types.UninitialisedField(self, 'VATRegnNb', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='TaxCtct', type=Contact13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxRegnNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VATRegnNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))