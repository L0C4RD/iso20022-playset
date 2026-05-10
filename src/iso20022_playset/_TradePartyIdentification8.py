from . import base_types
from ._FundIdentification5 import FundIdentification5
from ._PartyIdentification242Choice import PartyIdentification242Choice

class TradePartyIdentification8(base_types._BaseFieldType):

	__slots__ = ["_FndId", "_SubmitgPty", "_TradPty"]
	@property
	def FndId(self):
		return self._FndId

	@FndId.setter
	def FndId(self, value):
		self._FndId = value if type(value) != base_types.auto else self.make_default("FndId")

	@FndId.deleter
	def FndId(self):
		del self._FndId
		self._FndId = None

	@property
	def SubmitgPty(self):
		return self._SubmitgPty

	@SubmitgPty.setter
	def SubmitgPty(self, value):
		self._SubmitgPty = value if type(value) != base_types.auto else self.make_default("SubmitgPty")

	@SubmitgPty.deleter
	def SubmitgPty(self):
		del self._SubmitgPty
		self._SubmitgPty = None

	@property
	def TradPty(self):
		return self._TradPty

	@TradPty.setter
	def TradPty(self, value):
		self._TradPty = value if type(value) != base_types.auto else self.make_default("TradPty")

	@TradPty.deleter
	def TradPty(self):
		del self._TradPty
		self._TradPty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FndId', type=FundIdentification5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SubmitgPty', type=PartyIdentification242Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradPty', type=PartyIdentification242Choice, min=0, max=1, mutex_group=None, array=False),
	))

