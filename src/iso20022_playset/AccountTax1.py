from . import base_types
from .Max40Text import Max40Text
from .ResidenceLocation1Choice import ResidenceLocation1Choice
from .BillingTaxCalculationMethod1Code import BillingTaxCalculationMethod1Code

class AccountTax1(base_types._BaseFieldType):

	__slots__ = ["_NonResCtry", "_ClctnMtd", "_Rgn"]
	@property
	def NonResCtry(self):
		return self._NonResCtry

	@NonResCtry.setter
	def NonResCtry(self, value):
		self._NonResCtry = value if type(value) != base_types.auto else self.make_default("NonResCtry")

	@NonResCtry.deleter
	def NonResCtry(self):
		del self._NonResCtry
		self._NonResCtry = None

	@property
	def ClctnMtd(self):
		return self._ClctnMtd

	@ClctnMtd.setter
	def ClctnMtd(self, value):
		self._ClctnMtd = value if type(value) != base_types.auto else self.make_default("ClctnMtd")

	@ClctnMtd.deleter
	def ClctnMtd(self):
		del self._ClctnMtd
		self._ClctnMtd = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='NonResCtry', type=ResidenceLocation1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClctnMtd', type=BillingTaxCalculationMethod1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rgn', type=Max40Text, min=0, max=1, mutex_group=None, array=False),
	))

