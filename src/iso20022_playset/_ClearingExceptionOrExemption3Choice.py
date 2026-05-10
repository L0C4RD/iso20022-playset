from . import base_types
from .ClearingExceptionOrExemption2 import ClearingExceptionOrExemption2
from .NoReasonCode import NoReasonCode

class ClearingExceptionOrExemption3Choice(base_types._BaseFieldType):

	__slots__ = ["_CtrPties", "_Rsn"]
	@property
	def CtrPties(self):
		return self._CtrPties

	@CtrPties.setter
	def CtrPties(self, value):
		self._CtrPties = value if type(value) != base_types.auto else self.make_default("CtrPties")

	@CtrPties.deleter
	def CtrPties(self):
		del self._CtrPties
		self._CtrPties = None

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
		base_types.FieldEntry(name='CtrPties', type=ClearingExceptionOrExemption2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rsn', type=NoReasonCode, min=0, max=1, mutex_group=1, array=False),
	))

