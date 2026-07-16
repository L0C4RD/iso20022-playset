# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyAnd20DecimalAmount

class PostedMarginOrCollateral6(base_types._BaseFieldType):

	__slots__ = ["_InitlMrgnPstdPreHrcut", "_InitlMrgnPstdPstHrcut", "_VartnMrgnPstdPreHrcut", "_VartnMrgnPstdPstHrcut", "_XcssCollPstd"]
	@property
	def InitlMrgnPstdPreHrcut(self):
		return self._InitlMrgnPstdPreHrcut

	@InitlMrgnPstdPreHrcut.setter
	def InitlMrgnPstdPreHrcut(self, value):
		self._InitlMrgnPstdPreHrcut = value if value is not None else base_types.UninitialisedField(self, 'InitlMrgnPstdPreHrcut', ActiveOrHistoricCurrencyAnd20DecimalAmount, False)

	@InitlMrgnPstdPreHrcut.deleter
	def InitlMrgnPstdPreHrcut(self):
		del self._InitlMrgnPstdPreHrcut
		self._InitlMrgnPstdPreHrcut = base_types.UninitialisedField(self, 'InitlMrgnPstdPreHrcut', ActiveOrHistoricCurrencyAnd20DecimalAmount, False)

	@property
	def InitlMrgnPstdPstHrcut(self):
		return self._InitlMrgnPstdPstHrcut

	@InitlMrgnPstdPstHrcut.setter
	def InitlMrgnPstdPstHrcut(self, value):
		self._InitlMrgnPstdPstHrcut = value if value is not None else base_types.UninitialisedField(self, 'InitlMrgnPstdPstHrcut', ActiveOrHistoricCurrencyAnd20DecimalAmount, False)

	@InitlMrgnPstdPstHrcut.deleter
	def InitlMrgnPstdPstHrcut(self):
		del self._InitlMrgnPstdPstHrcut
		self._InitlMrgnPstdPstHrcut = base_types.UninitialisedField(self, 'InitlMrgnPstdPstHrcut', ActiveOrHistoricCurrencyAnd20DecimalAmount, False)

	@property
	def VartnMrgnPstdPreHrcut(self):
		return self._VartnMrgnPstdPreHrcut

	@VartnMrgnPstdPreHrcut.setter
	def VartnMrgnPstdPreHrcut(self, value):
		self._VartnMrgnPstdPreHrcut = value if value is not None else base_types.UninitialisedField(self, 'VartnMrgnPstdPreHrcut', ActiveOrHistoricCurrencyAnd20DecimalAmount, False)

	@VartnMrgnPstdPreHrcut.deleter
	def VartnMrgnPstdPreHrcut(self):
		del self._VartnMrgnPstdPreHrcut
		self._VartnMrgnPstdPreHrcut = base_types.UninitialisedField(self, 'VartnMrgnPstdPreHrcut', ActiveOrHistoricCurrencyAnd20DecimalAmount, False)

	@property
	def VartnMrgnPstdPstHrcut(self):
		return self._VartnMrgnPstdPstHrcut

	@VartnMrgnPstdPstHrcut.setter
	def VartnMrgnPstdPstHrcut(self, value):
		self._VartnMrgnPstdPstHrcut = value if value is not None else base_types.UninitialisedField(self, 'VartnMrgnPstdPstHrcut', ActiveOrHistoricCurrencyAnd20DecimalAmount, False)

	@VartnMrgnPstdPstHrcut.deleter
	def VartnMrgnPstdPstHrcut(self):
		del self._VartnMrgnPstdPstHrcut
		self._VartnMrgnPstdPstHrcut = base_types.UninitialisedField(self, 'VartnMrgnPstdPstHrcut', ActiveOrHistoricCurrencyAnd20DecimalAmount, False)

	@property
	def XcssCollPstd(self):
		return self._XcssCollPstd

	@XcssCollPstd.setter
	def XcssCollPstd(self, value):
		self._XcssCollPstd = value if value is not None else base_types.UninitialisedField(self, 'XcssCollPstd', ActiveOrHistoricCurrencyAnd20DecimalAmount, False)

	@XcssCollPstd.deleter
	def XcssCollPstd(self):
		del self._XcssCollPstd
		self._XcssCollPstd = base_types.UninitialisedField(self, 'XcssCollPstd', ActiveOrHistoricCurrencyAnd20DecimalAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='InitlMrgnPstdPreHrcut', type=ActiveOrHistoricCurrencyAnd20DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InitlMrgnPstdPstHrcut', type=ActiveOrHistoricCurrencyAnd20DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VartnMrgnPstdPreHrcut', type=ActiveOrHistoricCurrencyAnd20DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VartnMrgnPstdPstHrcut', type=ActiveOrHistoricCurrencyAnd20DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XcssCollPstd', type=ActiveOrHistoricCurrencyAnd20DecimalAmount, min=0, max=1, mutex_group=None, array=False),
	))