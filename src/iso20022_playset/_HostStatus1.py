from . import base_types
from ._Max35Text import Max35Text
from ._TrueFalseIndicator import TrueFalseIndicator

class HostStatus1(base_types._BaseFieldType):

	__slots__ = ["_Rchbl", "_AcqrrId"]
	@property
	def Rchbl(self):
		return self._Rchbl

	@Rchbl.setter
	def Rchbl(self, value):
		self._Rchbl = value if type(value) != base_types.auto else self.make_default("Rchbl")

	@Rchbl.deleter
	def Rchbl(self):
		del self._Rchbl
		self._Rchbl = None

	@property
	def AcqrrId(self):
		return self._AcqrrId

	@AcqrrId.setter
	def AcqrrId(self, value):
		self._AcqrrId = value if type(value) != base_types.auto else self.make_default("AcqrrId")

	@AcqrrId.deleter
	def AcqrrId(self):
		del self._AcqrrId
		self._AcqrrId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Rchbl', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcqrrId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

