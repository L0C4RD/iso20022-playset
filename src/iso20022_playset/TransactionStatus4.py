from . import base_types
from .BaselineStatus3Code import BaselineStatus3Code

class TransactionStatus4(base_types._BaseFieldType):

	__slots__ = ["_Sts"]
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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Sts', type=BaselineStatus3Code, min=1, max=1, mutex_group=None, array=False),
	))

