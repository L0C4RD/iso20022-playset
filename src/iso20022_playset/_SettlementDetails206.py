# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CollateralOwnership4
from . import ISODateTime
from . import SettlementParties36Choice

class SettlementDetails206(base_types._BaseFieldType):

	__slots__ = ["_CollOwnrsh", "_SttlmPties", "_TradDt"]
	@property
	def CollOwnrsh(self):
		return self._CollOwnrsh

	@CollOwnrsh.setter
	def CollOwnrsh(self, value):
		self._CollOwnrsh = value if value is not None else base_types.UninitialisedField(self, 'CollOwnrsh', CollateralOwnership4, False)

	@CollOwnrsh.deleter
	def CollOwnrsh(self):
		del self._CollOwnrsh
		self._CollOwnrsh = base_types.UninitialisedField(self, 'CollOwnrsh', CollateralOwnership4, False)

	@property
	def SttlmPties(self):
		return self._SttlmPties

	@SttlmPties.setter
	def SttlmPties(self, value):
		self._SttlmPties = value if value is not None else base_types.UninitialisedField(self, 'SttlmPties', SettlementParties36Choice, False)

	@SttlmPties.deleter
	def SttlmPties(self):
		del self._SttlmPties
		self._SttlmPties = base_types.UninitialisedField(self, 'SttlmPties', SettlementParties36Choice, False)

	@property
	def TradDt(self):
		return self._TradDt

	@TradDt.setter
	def TradDt(self, value):
		self._TradDt = value if value is not None else base_types.UninitialisedField(self, 'TradDt', ISODateTime, False)

	@TradDt.deleter
	def TradDt(self):
		del self._TradDt
		self._TradDt = base_types.UninitialisedField(self, 'TradDt', ISODateTime, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollOwnrsh', type=CollateralOwnership4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmPties', type=SettlementParties36Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDt', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
	))