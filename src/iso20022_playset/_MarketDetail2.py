from . import base_types
from ._MICIdentifier import MICIdentifier
from ._DecimalNumber import DecimalNumber

class MarketDetail2(base_types._BaseFieldType):

	__slots__ = ["_Id", "_AvrgDalyNbOfTxs"]
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
	def AvrgDalyNbOfTxs(self):
		return self._AvrgDalyNbOfTxs

	@AvrgDalyNbOfTxs.setter
	def AvrgDalyNbOfTxs(self, value):
		self._AvrgDalyNbOfTxs = value if type(value) != base_types.auto else self.make_default("AvrgDalyNbOfTxs")

	@AvrgDalyNbOfTxs.deleter
	def AvrgDalyNbOfTxs(self):
		del self._AvrgDalyNbOfTxs
		self._AvrgDalyNbOfTxs = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=MICIdentifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AvrgDalyNbOfTxs', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
	))

