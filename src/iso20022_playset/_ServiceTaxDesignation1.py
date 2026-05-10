from . import base_types
from .Max35Text import Max35Text
from .ServiceTaxDesignation1Code import ServiceTaxDesignation1Code
from .TaxReason1 import TaxReason1

class ServiceTaxDesignation1(base_types._BaseFieldType):

	__slots__ = ["_Cd", "_Rgn", "_TaxRsn"]
	@property
	def Cd(self):
		return self._Cd

	@Cd.setter
	def Cd(self, value):
		self._Cd = value if type(value) != base_types.auto else self.make_default("Cd")

	@Cd.deleter
	def Cd(self):
		del self._Cd
		self._Cd = None

	@property
	def Rgn(self):
		return self._Rgn

	@Rgn.setter
	def Rgn(self, value):
		self._Rgn = value if type(value) != base_types.auto else self.make_default("Rgn")

	@Rgn.deleter
	def Rgn(self):
		del self._Rgn
		self._Rgn = None

	@property
	def TaxRsn(self):
		return self._TaxRsn

	@TaxRsn.setter
	def TaxRsn(self, value):
		self._TaxRsn = value if type(value) != base_types.auto else self.make_default("TaxRsn")

	@TaxRsn.deleter
	def TaxRsn(self):
		del self._TaxRsn
		self._TaxRsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cd', type=ServiceTaxDesignation1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rgn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxRsn', type=TaxReason1, min=0, max=None, mutex_group=None, array=True),
	))

