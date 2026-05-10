from . import base_types
from .ActiveOrHistoricCurrencyAndAmount import ActiveOrHistoricCurrencyAndAmount

class ReceivedMarginOrCollateral4(base_types._BaseFieldType):

	__slots__ = ["_XcssCollRcvd", "_VartnMrgnRcvd", "_InitlMrgnRcvd"]
	@property
	def XcssCollRcvd(self):
		return self._XcssCollRcvd

	@XcssCollRcvd.setter
	def XcssCollRcvd(self, value):
		self._XcssCollRcvd = value if type(value) != base_types.auto else self.make_default("XcssCollRcvd")

	@XcssCollRcvd.deleter
	def XcssCollRcvd(self):
		del self._XcssCollRcvd
		self._XcssCollRcvd = None

	@property
	def VartnMrgnRcvd(self):
		return self._VartnMrgnRcvd

	@VartnMrgnRcvd.setter
	def VartnMrgnRcvd(self, value):
		self._VartnMrgnRcvd = value if type(value) != base_types.auto else self.make_default("VartnMrgnRcvd")

	@VartnMrgnRcvd.deleter
	def VartnMrgnRcvd(self):
		del self._VartnMrgnRcvd
		self._VartnMrgnRcvd = None

	@property
	def InitlMrgnRcvd(self):
		return self._InitlMrgnRcvd

	@InitlMrgnRcvd.setter
	def InitlMrgnRcvd(self, value):
		self._InitlMrgnRcvd = value if type(value) != base_types.auto else self.make_default("InitlMrgnRcvd")

	@InitlMrgnRcvd.deleter
	def InitlMrgnRcvd(self):
		del self._InitlMrgnRcvd
		self._InitlMrgnRcvd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='XcssCollRcvd', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VartnMrgnRcvd', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InitlMrgnRcvd', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))

