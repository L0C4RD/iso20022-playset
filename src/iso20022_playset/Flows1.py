from . import base_types
from .AmountAndDirection102 import AmountAndDirection102

class Flows1(base_types._BaseFieldType):

	__slots__ = ["_InvstmtFlows", "_PmtBkFlows"]
	@property
	def InvstmtFlows(self):
		return self._InvstmtFlows

	@InvstmtFlows.setter
	def InvstmtFlows(self, value):
		self._InvstmtFlows = value if type(value) != base_types.auto else self.make_default("InvstmtFlows")

	@InvstmtFlows.deleter
	def InvstmtFlows(self):
		del self._InvstmtFlows
		self._InvstmtFlows = None

	@property
	def PmtBkFlows(self):
		return self._PmtBkFlows

	@PmtBkFlows.setter
	def PmtBkFlows(self, value):
		self._PmtBkFlows = value if type(value) != base_types.auto else self.make_default("PmtBkFlows")

	@PmtBkFlows.deleter
	def PmtBkFlows(self):
		del self._PmtBkFlows
		self._PmtBkFlows = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='InvstmtFlows', type=AmountAndDirection102, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtBkFlows', type=AmountAndDirection102, min=1, max=1, mutex_group=None, array=False),
	))

