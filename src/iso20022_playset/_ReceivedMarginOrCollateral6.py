from . import base_types
from ._ActiveOrHistoricCurrencyAnd20DecimalAmount import ActiveOrHistoricCurrencyAnd20DecimalAmount

class ReceivedMarginOrCollateral6(base_types._BaseFieldType):

	__slots__ = ["_InitlMrgnRcvdPreHrcut", "_InitlMrgnRcvdPstHrcut", "_XcssCollRcvd", "_VartnMrgnRcvdPstHrcut", "_VartnMrgnRcvdPreHrcut"]
	@property
	def InitlMrgnRcvdPreHrcut(self):
		return self._InitlMrgnRcvdPreHrcut

	@InitlMrgnRcvdPreHrcut.setter
	def InitlMrgnRcvdPreHrcut(self, value):
		self._InitlMrgnRcvdPreHrcut = value if type(value) != base_types.auto else self.make_default("InitlMrgnRcvdPreHrcut")

	@InitlMrgnRcvdPreHrcut.deleter
	def InitlMrgnRcvdPreHrcut(self):
		del self._InitlMrgnRcvdPreHrcut
		self._InitlMrgnRcvdPreHrcut = None

	@property
	def InitlMrgnRcvdPstHrcut(self):
		return self._InitlMrgnRcvdPstHrcut

	@InitlMrgnRcvdPstHrcut.setter
	def InitlMrgnRcvdPstHrcut(self, value):
		self._InitlMrgnRcvdPstHrcut = value if type(value) != base_types.auto else self.make_default("InitlMrgnRcvdPstHrcut")

	@InitlMrgnRcvdPstHrcut.deleter
	def InitlMrgnRcvdPstHrcut(self):
		del self._InitlMrgnRcvdPstHrcut
		self._InitlMrgnRcvdPstHrcut = None

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
	def VartnMrgnRcvdPstHrcut(self):
		return self._VartnMrgnRcvdPstHrcut

	@VartnMrgnRcvdPstHrcut.setter
	def VartnMrgnRcvdPstHrcut(self, value):
		self._VartnMrgnRcvdPstHrcut = value if type(value) != base_types.auto else self.make_default("VartnMrgnRcvdPstHrcut")

	@VartnMrgnRcvdPstHrcut.deleter
	def VartnMrgnRcvdPstHrcut(self):
		del self._VartnMrgnRcvdPstHrcut
		self._VartnMrgnRcvdPstHrcut = None

	@property
	def VartnMrgnRcvdPreHrcut(self):
		return self._VartnMrgnRcvdPreHrcut

	@VartnMrgnRcvdPreHrcut.setter
	def VartnMrgnRcvdPreHrcut(self, value):
		self._VartnMrgnRcvdPreHrcut = value if type(value) != base_types.auto else self.make_default("VartnMrgnRcvdPreHrcut")

	@VartnMrgnRcvdPreHrcut.deleter
	def VartnMrgnRcvdPreHrcut(self):
		del self._VartnMrgnRcvdPreHrcut
		self._VartnMrgnRcvdPreHrcut = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='InitlMrgnRcvdPreHrcut', type=ActiveOrHistoricCurrencyAnd20DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InitlMrgnRcvdPstHrcut', type=ActiveOrHistoricCurrencyAnd20DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XcssCollRcvd', type=ActiveOrHistoricCurrencyAnd20DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VartnMrgnRcvdPstHrcut', type=ActiveOrHistoricCurrencyAnd20DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VartnMrgnRcvdPreHrcut', type=ActiveOrHistoricCurrencyAnd20DecimalAmount, min=0, max=1, mutex_group=None, array=False),
	))

