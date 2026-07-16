# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import ServiceTaxDesignation1Code
from . import TaxReason1

class ServiceTaxDesignation1(base_types._BaseFieldType):

	__slots__ = ["_Cd", "_Rgn", "_TaxRsn"]
	@property
	def Cd(self):
		return self._Cd

	@Cd.setter
	def Cd(self, value):
		self._Cd = value if value is not None else base_types.UninitialisedField(self, 'Cd', ServiceTaxDesignation1Code, False)

	@Cd.deleter
	def Cd(self):
		del self._Cd
		self._Cd = base_types.UninitialisedField(self, 'Cd', ServiceTaxDesignation1Code, False)

	@property
	def Rgn(self):
		return self._Rgn

	@Rgn.setter
	def Rgn(self, value):
		self._Rgn = value if value is not None else base_types.UninitialisedField(self, 'Rgn', Max35Text, False)

	@Rgn.deleter
	def Rgn(self):
		del self._Rgn
		self._Rgn = base_types.UninitialisedField(self, 'Rgn', Max35Text, False)

	@property
	def TaxRsn(self):
		return self._TaxRsn

	@TaxRsn.setter
	def TaxRsn(self, value):
		self._TaxRsn = value if value is not None else base_types.UninitialisedField(self, 'TaxRsn', TaxReason1, True)

	@TaxRsn.deleter
	def TaxRsn(self):
		del self._TaxRsn
		self._TaxRsn = base_types.UninitialisedField(self, 'TaxRsn', TaxReason1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cd', type=ServiceTaxDesignation1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rgn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxRsn', type=TaxReason1, min=0, max=None, mutex_group=None, array=True),
	))