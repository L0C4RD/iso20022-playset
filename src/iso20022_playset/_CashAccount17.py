from . import base_types
from ._ActiveCurrencyCode import ActiveCurrencyCode
from ._PartyIdentification2Choice import PartyIdentification2Choice
from ._BICIdentifier import BICIdentifier
from ._CashAccountIdentification1Choice import CashAccountIdentification1Choice

class CashAccount17(base_types._BaseFieldType):

	__slots__ = ["_AcctOwnrId", "_CrspdtBkId", "_PmtCcy", "_AcctId"]
	@property
	def AcctId(self):
		return self._AcctId

	@AcctId.setter
	def AcctId(self, value):
		self._AcctId = value if type(value) != base_types.auto else self.make_default("AcctId")

	@AcctId.deleter
	def AcctId(self):
		del self._AcctId
		self._AcctId = None

	@property
	def AcctOwnrId(self):
		return self._AcctOwnrId

	@AcctOwnrId.setter
	def AcctOwnrId(self, value):
		self._AcctOwnrId = value if type(value) != base_types.auto else self.make_default("AcctOwnrId")

	@AcctOwnrId.deleter
	def AcctOwnrId(self):
		del self._AcctOwnrId
		self._AcctOwnrId = None

	@property
	def CrspdtBkId(self):
		return self._CrspdtBkId

	@CrspdtBkId.setter
	def CrspdtBkId(self, value):
		self._CrspdtBkId = value if type(value) != base_types.auto else self.make_default("CrspdtBkId")

	@CrspdtBkId.deleter
	def CrspdtBkId(self):
		del self._CrspdtBkId
		self._CrspdtBkId = None

	@property
	def PmtCcy(self):
		return self._PmtCcy

	@PmtCcy.setter
	def PmtCcy(self, value):
		self._PmtCcy = value if type(value) != base_types.auto else self.make_default("PmtCcy")

	@PmtCcy.deleter
	def PmtCcy(self):
		del self._PmtCcy
		self._PmtCcy = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctId', type=CashAccountIdentification1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctOwnrId', type=PartyIdentification2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrspdtBkId', type=BICIdentifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtCcy', type=ActiveCurrencyCode, min=1, max=1, mutex_group=None, array=False),
	))

