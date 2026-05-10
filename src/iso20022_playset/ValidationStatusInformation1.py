from . import base_types
from .TechnicalValidationStatus1Code import TechnicalValidationStatus1Code
from .Max105Text import Max105Text
from .StatusReason4Choice import StatusReason4Choice

class ValidationStatusInformation1(base_types._BaseFieldType):

	__slots__ = ["_Sts", "_StsRsn", "_AddtlStsRsnInf"]
	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if type(value) != base_types.auto else self.make_default("Sts")

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = None

	@property
	def StsRsn(self):
		return self._StsRsn

	@StsRsn.setter
	def StsRsn(self, value):
		self._StsRsn = value if type(value) != base_types.auto else self.make_default("StsRsn")

	@StsRsn.deleter
	def StsRsn(self):
		del self._StsRsn
		self._StsRsn = None

	@property
	def AddtlStsRsnInf(self):
		return self._AddtlStsRsnInf

	@AddtlStsRsnInf.setter
	def AddtlStsRsnInf(self, value):
		self._AddtlStsRsnInf = value if type(value) != base_types.auto else self.make_default("AddtlStsRsnInf")

	@AddtlStsRsnInf.deleter
	def AddtlStsRsnInf(self):
		del self._AddtlStsRsnInf
		self._AddtlStsRsnInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Sts', type=TechnicalValidationStatus1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsRsn', type=StatusReason4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlStsRsnInf', type=Max105Text, min=0, max=None, mutex_group=None, array=True),
	))

