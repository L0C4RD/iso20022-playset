# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CashParties24
from . import SettlementParties35

class SecuritiesOrCash1Choice(base_types._BaseFieldType):

	__slots__ = ["_CshPtiesDtls", "_SctiesDtls"]
	@property
	def CshPtiesDtls(self):
		return self._CshPtiesDtls

	@CshPtiesDtls.setter
	def CshPtiesDtls(self, value):
		self._CshPtiesDtls = value if value is not None else base_types.UninitialisedField(self, 'CshPtiesDtls', CashParties24, False)

	@CshPtiesDtls.deleter
	def CshPtiesDtls(self):
		del self._CshPtiesDtls
		self._CshPtiesDtls = base_types.UninitialisedField(self, 'CshPtiesDtls', CashParties24, False)

	@property
	def SctiesDtls(self):
		return self._SctiesDtls

	@SctiesDtls.setter
	def SctiesDtls(self, value):
		self._SctiesDtls = value if value is not None else base_types.UninitialisedField(self, 'SctiesDtls', SettlementParties35, False)

	@SctiesDtls.deleter
	def SctiesDtls(self):
		del self._SctiesDtls
		self._SctiesDtls = base_types.UninitialisedField(self, 'SctiesDtls', SettlementParties35, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CshPtiesDtls', type=CashParties24, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SctiesDtls', type=SettlementParties35, min=0, max=1, mutex_group=1, array=False),
	))