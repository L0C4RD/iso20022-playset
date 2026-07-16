# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyAndAmount

class PostedMarginOrCollateral4(base_types._BaseFieldType):

	__slots__ = ["_InitlMrgnPstd", "_VartnMrgnPstd", "_XcssCollPstd"]
	@property
	def InitlMrgnPstd(self):
		return self._InitlMrgnPstd

	@InitlMrgnPstd.setter
	def InitlMrgnPstd(self, value):
		self._InitlMrgnPstd = value if value is not None else base_types.UninitialisedField(self, 'InitlMrgnPstd', ActiveOrHistoricCurrencyAndAmount, False)

	@InitlMrgnPstd.deleter
	def InitlMrgnPstd(self):
		del self._InitlMrgnPstd
		self._InitlMrgnPstd = base_types.UninitialisedField(self, 'InitlMrgnPstd', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def VartnMrgnPstd(self):
		return self._VartnMrgnPstd

	@VartnMrgnPstd.setter
	def VartnMrgnPstd(self, value):
		self._VartnMrgnPstd = value if value is not None else base_types.UninitialisedField(self, 'VartnMrgnPstd', ActiveOrHistoricCurrencyAndAmount, False)

	@VartnMrgnPstd.deleter
	def VartnMrgnPstd(self):
		del self._VartnMrgnPstd
		self._VartnMrgnPstd = base_types.UninitialisedField(self, 'VartnMrgnPstd', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def XcssCollPstd(self):
		return self._XcssCollPstd

	@XcssCollPstd.setter
	def XcssCollPstd(self, value):
		self._XcssCollPstd = value if value is not None else base_types.UninitialisedField(self, 'XcssCollPstd', ActiveOrHistoricCurrencyAndAmount, False)

	@XcssCollPstd.deleter
	def XcssCollPstd(self):
		del self._XcssCollPstd
		self._XcssCollPstd = base_types.UninitialisedField(self, 'XcssCollPstd', ActiveOrHistoricCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='InitlMrgnPstd', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VartnMrgnPstd', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XcssCollPstd', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))