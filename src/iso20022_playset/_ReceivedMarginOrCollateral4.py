# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyAndAmount

class ReceivedMarginOrCollateral4(base_types._BaseFieldType):

	__slots__ = ["_InitlMrgnRcvd", "_VartnMrgnRcvd", "_XcssCollRcvd"]
	@property
	def InitlMrgnRcvd(self):
		return self._InitlMrgnRcvd

	@InitlMrgnRcvd.setter
	def InitlMrgnRcvd(self, value):
		self._InitlMrgnRcvd = value if value is not None else base_types.UninitialisedField(self, 'InitlMrgnRcvd', ActiveOrHistoricCurrencyAndAmount, False)

	@InitlMrgnRcvd.deleter
	def InitlMrgnRcvd(self):
		del self._InitlMrgnRcvd
		self._InitlMrgnRcvd = base_types.UninitialisedField(self, 'InitlMrgnRcvd', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def VartnMrgnRcvd(self):
		return self._VartnMrgnRcvd

	@VartnMrgnRcvd.setter
	def VartnMrgnRcvd(self, value):
		self._VartnMrgnRcvd = value if value is not None else base_types.UninitialisedField(self, 'VartnMrgnRcvd', ActiveOrHistoricCurrencyAndAmount, False)

	@VartnMrgnRcvd.deleter
	def VartnMrgnRcvd(self):
		del self._VartnMrgnRcvd
		self._VartnMrgnRcvd = base_types.UninitialisedField(self, 'VartnMrgnRcvd', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def XcssCollRcvd(self):
		return self._XcssCollRcvd

	@XcssCollRcvd.setter
	def XcssCollRcvd(self, value):
		self._XcssCollRcvd = value if value is not None else base_types.UninitialisedField(self, 'XcssCollRcvd', ActiveOrHistoricCurrencyAndAmount, False)

	@XcssCollRcvd.deleter
	def XcssCollRcvd(self):
		del self._XcssCollRcvd
		self._XcssCollRcvd = base_types.UninitialisedField(self, 'XcssCollRcvd', ActiveOrHistoricCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='InitlMrgnRcvd', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VartnMrgnRcvd', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XcssCollRcvd', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))