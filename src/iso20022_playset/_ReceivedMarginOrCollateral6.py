# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyAnd20DecimalAmount

class ReceivedMarginOrCollateral6(base_types._BaseFieldType):

	__slots__ = ["_InitlMrgnRcvdPreHrcut", "_InitlMrgnRcvdPstHrcut", "_VartnMrgnRcvdPreHrcut", "_VartnMrgnRcvdPstHrcut", "_XcssCollRcvd"]
	@property
	def InitlMrgnRcvdPreHrcut(self):
		return self._InitlMrgnRcvdPreHrcut

	@InitlMrgnRcvdPreHrcut.setter
	def InitlMrgnRcvdPreHrcut(self, value):
		self._InitlMrgnRcvdPreHrcut = value if value is not None else base_types.UninitialisedField(self, 'InitlMrgnRcvdPreHrcut', ActiveOrHistoricCurrencyAnd20DecimalAmount, False)

	@InitlMrgnRcvdPreHrcut.deleter
	def InitlMrgnRcvdPreHrcut(self):
		del self._InitlMrgnRcvdPreHrcut
		self._InitlMrgnRcvdPreHrcut = base_types.UninitialisedField(self, 'InitlMrgnRcvdPreHrcut', ActiveOrHistoricCurrencyAnd20DecimalAmount, False)

	@property
	def InitlMrgnRcvdPstHrcut(self):
		return self._InitlMrgnRcvdPstHrcut

	@InitlMrgnRcvdPstHrcut.setter
	def InitlMrgnRcvdPstHrcut(self, value):
		self._InitlMrgnRcvdPstHrcut = value if value is not None else base_types.UninitialisedField(self, 'InitlMrgnRcvdPstHrcut', ActiveOrHistoricCurrencyAnd20DecimalAmount, False)

	@InitlMrgnRcvdPstHrcut.deleter
	def InitlMrgnRcvdPstHrcut(self):
		del self._InitlMrgnRcvdPstHrcut
		self._InitlMrgnRcvdPstHrcut = base_types.UninitialisedField(self, 'InitlMrgnRcvdPstHrcut', ActiveOrHistoricCurrencyAnd20DecimalAmount, False)

	@property
	def VartnMrgnRcvdPreHrcut(self):
		return self._VartnMrgnRcvdPreHrcut

	@VartnMrgnRcvdPreHrcut.setter
	def VartnMrgnRcvdPreHrcut(self, value):
		self._VartnMrgnRcvdPreHrcut = value if value is not None else base_types.UninitialisedField(self, 'VartnMrgnRcvdPreHrcut', ActiveOrHistoricCurrencyAnd20DecimalAmount, False)

	@VartnMrgnRcvdPreHrcut.deleter
	def VartnMrgnRcvdPreHrcut(self):
		del self._VartnMrgnRcvdPreHrcut
		self._VartnMrgnRcvdPreHrcut = base_types.UninitialisedField(self, 'VartnMrgnRcvdPreHrcut', ActiveOrHistoricCurrencyAnd20DecimalAmount, False)

	@property
	def VartnMrgnRcvdPstHrcut(self):
		return self._VartnMrgnRcvdPstHrcut

	@VartnMrgnRcvdPstHrcut.setter
	def VartnMrgnRcvdPstHrcut(self, value):
		self._VartnMrgnRcvdPstHrcut = value if value is not None else base_types.UninitialisedField(self, 'VartnMrgnRcvdPstHrcut', ActiveOrHistoricCurrencyAnd20DecimalAmount, False)

	@VartnMrgnRcvdPstHrcut.deleter
	def VartnMrgnRcvdPstHrcut(self):
		del self._VartnMrgnRcvdPstHrcut
		self._VartnMrgnRcvdPstHrcut = base_types.UninitialisedField(self, 'VartnMrgnRcvdPstHrcut', ActiveOrHistoricCurrencyAnd20DecimalAmount, False)

	@property
	def XcssCollRcvd(self):
		return self._XcssCollRcvd

	@XcssCollRcvd.setter
	def XcssCollRcvd(self, value):
		self._XcssCollRcvd = value if value is not None else base_types.UninitialisedField(self, 'XcssCollRcvd', ActiveOrHistoricCurrencyAnd20DecimalAmount, False)

	@XcssCollRcvd.deleter
	def XcssCollRcvd(self):
		del self._XcssCollRcvd
		self._XcssCollRcvd = base_types.UninitialisedField(self, 'XcssCollRcvd', ActiveOrHistoricCurrencyAnd20DecimalAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='InitlMrgnRcvdPreHrcut', type=ActiveOrHistoricCurrencyAnd20DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InitlMrgnRcvdPstHrcut', type=ActiveOrHistoricCurrencyAnd20DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VartnMrgnRcvdPreHrcut', type=ActiveOrHistoricCurrencyAnd20DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VartnMrgnRcvdPstHrcut', type=ActiveOrHistoricCurrencyAnd20DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XcssCollRcvd', type=ActiveOrHistoricCurrencyAnd20DecimalAmount, min=0, max=1, mutex_group=None, array=False),
	))