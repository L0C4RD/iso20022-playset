import base_types
import ActiveOrHistoricCurrencyAnd20DecimalAmount

class PostedMarginOrCollateral6(base_types._BaseFieldType):

	__slots__ = ["_VartnMrgnPstdPstHrcut", "_InitlMrgnPstdPstHrcut", "_XcssCollPstd", "_InitlMrgnPstdPreHrcut", "_VartnMrgnPstdPreHrcut"]
	@property
	def VartnMrgnPstdPstHrcut(self):
		return self._VartnMrgnPstdPstHrcut

	@VartnMrgnPstdPstHrcut.setter
	def VartnMrgnPstdPstHrcut(self, value):
		self._VartnMrgnPstdPstHrcut = value if type(value) != auto else self.make_default("VartnMrgnPstdPstHrcut")

	@VartnMrgnPstdPstHrcut.deleter
	def VartnMrgnPstdPstHrcut(self):
		del self._VartnMrgnPstdPstHrcut
		self._VartnMrgnPstdPstHrcut = None

	@property
	def InitlMrgnPstdPstHrcut(self):
		return self._InitlMrgnPstdPstHrcut

	@InitlMrgnPstdPstHrcut.setter
	def InitlMrgnPstdPstHrcut(self, value):
		self._InitlMrgnPstdPstHrcut = value if type(value) != auto else self.make_default("InitlMrgnPstdPstHrcut")

	@InitlMrgnPstdPstHrcut.deleter
	def InitlMrgnPstdPstHrcut(self):
		del self._InitlMrgnPstdPstHrcut
		self._InitlMrgnPstdPstHrcut = None

	@property
	def XcssCollPstd(self):
		return self._XcssCollPstd

	@XcssCollPstd.setter
	def XcssCollPstd(self, value):
		self._XcssCollPstd = value if type(value) != auto else self.make_default("XcssCollPstd")

	@XcssCollPstd.deleter
	def XcssCollPstd(self):
		del self._XcssCollPstd
		self._XcssCollPstd = None

	@property
	def InitlMrgnPstdPreHrcut(self):
		return self._InitlMrgnPstdPreHrcut

	@InitlMrgnPstdPreHrcut.setter
	def InitlMrgnPstdPreHrcut(self, value):
		self._InitlMrgnPstdPreHrcut = value if type(value) != auto else self.make_default("InitlMrgnPstdPreHrcut")

	@InitlMrgnPstdPreHrcut.deleter
	def InitlMrgnPstdPreHrcut(self):
		del self._InitlMrgnPstdPreHrcut
		self._InitlMrgnPstdPreHrcut = None

	@property
	def VartnMrgnPstdPreHrcut(self):
		return self._VartnMrgnPstdPreHrcut

	@VartnMrgnPstdPreHrcut.setter
	def VartnMrgnPstdPreHrcut(self, value):
		self._VartnMrgnPstdPreHrcut = value if type(value) != auto else self.make_default("VartnMrgnPstdPreHrcut")

	@VartnMrgnPstdPreHrcut.deleter
	def VartnMrgnPstdPreHrcut(self):
		del self._VartnMrgnPstdPreHrcut
		self._VartnMrgnPstdPreHrcut = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='VartnMrgnPstdPstHrcut', type=ActiveOrHistoricCurrencyAnd20DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InitlMrgnPstdPstHrcut', type=ActiveOrHistoricCurrencyAnd20DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XcssCollPstd', type=ActiveOrHistoricCurrencyAnd20DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InitlMrgnPstdPreHrcut', type=ActiveOrHistoricCurrencyAnd20DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VartnMrgnPstdPreHrcut', type=ActiveOrHistoricCurrencyAnd20DecimalAmount, min=0, max=1, mutex_group=None, array=False),
	))

