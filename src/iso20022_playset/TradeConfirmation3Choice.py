import base_types
import TradeConfirmation4
import TradeNonConfirmation1

class TradeConfirmation3Choice(base_types._BaseFieldType):

	__slots__ = ["_NonConfd", "_Confd"]
	@property
	def NonConfd(self):
		return self._NonConfd

	@NonConfd.setter
	def NonConfd(self, value):
		self._NonConfd = value if type(value) != auto else self.make_default("NonConfd")

	@NonConfd.deleter
	def NonConfd(self):
		del self._NonConfd
		self._NonConfd = None

	@property
	def Confd(self):
		return self._Confd

	@Confd.setter
	def Confd(self, value):
		self._Confd = value if type(value) != auto else self.make_default("Confd")

	@Confd.deleter
	def Confd(self):
		del self._Confd
		self._Confd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NonConfd', type=TradeNonConfirmation1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Confd', type=TradeConfirmation4, min=0, max=1, mutex_group=1, array=False),
	))

