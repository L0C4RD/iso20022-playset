from . import base_types
from ._Max350Text import Max350Text

class TransferCancellationPendingStatus1(base_types._BaseFieldType):

	__slots__ = ["_Rsn"]
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
		base_types.FieldEntry(name='Rsn', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
	))

