from . import base_types
from ._Max140Text import Max140Text
from ._SecurityIdentification19 import SecurityIdentification19
from ._StatusReason7Choice import StatusReason7Choice

class StatusReasonInformation13(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_FinInstrm", "_Rsn"]
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

	@property
	def FinInstrm(self):
		return self._FinInstrm

	@FinInstrm.setter
	def FinInstrm(self, value):
		self._FinInstrm = value if type(value) != base_types.auto else self.make_default("FinInstrm")

	@FinInstrm.deleter
	def FinInstrm(self):
		del self._FinInstrm
		self._FinInstrm = None

	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if type(value) != base_types.auto else self.make_default("Rsn")

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrm', type=SecurityIdentification19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rsn', type=StatusReason7Choice, min=1, max=1, mutex_group=None, array=False),
	))

