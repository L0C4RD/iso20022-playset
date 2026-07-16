# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FundIdentification5
from . import PartyIdentification242Choice

class TradePartyIdentification8(base_types._BaseFieldType):

	__slots__ = ["_FndId", "_SubmitgPty", "_TradPty"]
	@property
	def FndId(self):
		return self._FndId

	@FndId.setter
	def FndId(self, value):
		self._FndId = value if value is not None else base_types.UninitialisedField(self, 'FndId', FundIdentification5, True)

	@FndId.deleter
	def FndId(self):
		del self._FndId
		self._FndId = base_types.UninitialisedField(self, 'FndId', FundIdentification5, True)

	@property
	def SubmitgPty(self):
		return self._SubmitgPty

	@SubmitgPty.setter
	def SubmitgPty(self, value):
		self._SubmitgPty = value if value is not None else base_types.UninitialisedField(self, 'SubmitgPty', PartyIdentification242Choice, False)

	@SubmitgPty.deleter
	def SubmitgPty(self):
		del self._SubmitgPty
		self._SubmitgPty = base_types.UninitialisedField(self, 'SubmitgPty', PartyIdentification242Choice, False)

	@property
	def TradPty(self):
		return self._TradPty

	@TradPty.setter
	def TradPty(self, value):
		self._TradPty = value if value is not None else base_types.UninitialisedField(self, 'TradPty', PartyIdentification242Choice, False)

	@TradPty.deleter
	def TradPty(self):
		del self._TradPty
		self._TradPty = base_types.UninitialisedField(self, 'TradPty', PartyIdentification242Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FndId', type=FundIdentification5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SubmitgPty', type=PartyIdentification242Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradPty', type=PartyIdentification242Choice, min=0, max=1, mutex_group=None, array=False),
	))