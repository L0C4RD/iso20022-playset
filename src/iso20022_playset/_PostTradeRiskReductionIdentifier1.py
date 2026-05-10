from . import base_types
from .Max52Text import Max52Text
from .LEIIdentifier import LEIIdentifier

class PostTradeRiskReductionIdentifier1(base_types._BaseFieldType):

	__slots__ = ["_Id", "_Strr"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def Strr(self):
		return self._Strr

	@Strr.setter
	def Strr(self, value):
		self._Strr = value if type(value) != base_types.auto else self.make_default("Strr")

	@Strr.deleter
	def Strr(self):
		del self._Strr
		self._Strr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=Max52Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Strr', type=LEIIdentifier, min=1, max=1, mutex_group=None, array=False),
	))

