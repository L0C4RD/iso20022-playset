from . import base_types
from ._Max2048Text import Max2048Text

class SettlementFailureReason2(base_types._BaseFieldType):

	__slots__ = ["_EffcncyImprvmt", "_MainRsns"]
	@property
	def EffcncyImprvmt(self):
		return self._EffcncyImprvmt

	@EffcncyImprvmt.setter
	def EffcncyImprvmt(self, value):
		self._EffcncyImprvmt = value if type(value) != base_types.auto else self.make_default("EffcncyImprvmt")

	@EffcncyImprvmt.deleter
	def EffcncyImprvmt(self):
		del self._EffcncyImprvmt
		self._EffcncyImprvmt = None

	@property
	def MainRsns(self):
		return self._MainRsns

	@MainRsns.setter
	def MainRsns(self, value):
		self._MainRsns = value if type(value) != base_types.auto else self.make_default("MainRsns")

	@MainRsns.deleter
	def MainRsns(self):
		del self._MainRsns
		self._MainRsns = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='EffcncyImprvmt', type=Max2048Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MainRsns', type=Max2048Text, min=1, max=1, mutex_group=None, array=False),
	))

