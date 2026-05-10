from . import base_types
from .EmploymentDetails1 import EmploymentDetails1
from .AdditionalInformation15 import AdditionalInformation15

class Drawdown3(base_types._BaseFieldType):

	__slots__ = ["_MplymntDtls", "_AddtlInf"]
	@property
	def MplymntDtls(self):
		return self._MplymntDtls

	@MplymntDtls.setter
	def MplymntDtls(self, value):
		self._MplymntDtls = value if type(value) != base_types.auto else self.make_default("MplymntDtls")

	@MplymntDtls.deleter
	def MplymntDtls(self):
		del self._MplymntDtls
		self._MplymntDtls = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != base_types.auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MplymntDtls', type=EmploymentDetails1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=None, mutex_group=None, array=True),
	))

