from . import base_types
from .CashAccountIdentification1Choice import CashAccountIdentification1Choice
from .BICIdentifier import BICIdentifier
from .PartyIdentification2Choice import PartyIdentification2Choice
from .ActiveCurrencyCode import ActiveCurrencyCode

class CashAccount17(base_types._BaseFieldType):

	__slots__ = ["_PmtCcy", "_AcctOwnrId", "_AcctId", "_CrspdtBkId"]
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
	def CrspdtBkId(self):
		return self._CrspdtBkId

	@CrspdtBkId.setter
	def CrspdtBkId(self, value):
		self._CrspdtBkId = value if type(value) != base_types.auto else self.make_default("CrspdtBkId")

	@CrspdtBkId.deleter
	def CrspdtBkId(self):
		del self._CrspdtBkId
		self._CrspdtBkId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PmtCcy', type=ActiveCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctOwnrId', type=PartyIdentification2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctId', type=CashAccountIdentification1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrspdtBkId', type=BICIdentifier, min=1, max=1, mutex_group=None, array=False),
	))

