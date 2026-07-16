# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SettlementFailsSecurities1

class SettlementFailsSecuritiesRange1(base_types._BaseFieldType):

	__slots__ = ["_HghstInVal", "_HghstInVol"]
	@property
	def HghstInVal(self):
		return self._HghstInVal

	@HghstInVal.setter
	def HghstInVal(self, value):
		self._HghstInVal = value if value is not None else base_types.UninitialisedField(self, 'HghstInVal', SettlementFailsSecurities1, True)

	@HghstInVal.deleter
	def HghstInVal(self):
		del self._HghstInVal
		self._HghstInVal = base_types.UninitialisedField(self, 'HghstInVal', SettlementFailsSecurities1, True)

	@property
	def HghstInVol(self):
		return self._HghstInVol

	@HghstInVol.setter
	def HghstInVol(self, value):
		self._HghstInVol = value if value is not None else base_types.UninitialisedField(self, 'HghstInVol', SettlementFailsSecurities1, True)

	@HghstInVol.deleter
	def HghstInVol(self):
		del self._HghstInVol
		self._HghstInVol = base_types.UninitialisedField(self, 'HghstInVol', SettlementFailsSecurities1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='HghstInVal', type=SettlementFailsSecurities1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='HghstInVol', type=SettlementFailsSecurities1, min=1, max=None, mutex_group=None, array=True),
	))