from . import base_types
from .ChequePartyRole1Code import ChequePartyRole1Code
from .Max140Text import Max140Text
from .ChequeCancellationReason1Choice import ChequeCancellationReason1Choice

class ChequeCancellationReason1(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_Rsn", "_Orgtr"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if type(value) != auto else self.make_default("Rsn")

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = None

	@property
	def Orgtr(self):
		return self._Orgtr

	@Orgtr.setter
	def Orgtr(self, value):
		self._Orgtr = value if type(value) != auto else self.make_default("Orgtr")

	@Orgtr.deleter
	def Orgtr(self):
		del self._Orgtr
		self._Orgtr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rsn', type=ChequeCancellationReason1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Orgtr', type=ChequePartyRole1Code, min=0, max=1, mutex_group=None, array=False),
	))

