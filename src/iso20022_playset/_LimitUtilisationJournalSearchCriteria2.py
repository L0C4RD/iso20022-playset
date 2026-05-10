from . import base_types
from ._ISODate import ISODate
from ._ActiveCurrencyCode import ActiveCurrencyCode
from ._AccountIdentification4Choice import AccountIdentification4Choice
from ._SystemPartyIdentification8 import SystemPartyIdentification8
from ._PartyIdentification136 import PartyIdentification136
from ._LimitType4Code import LimitType4Code

class LimitUtilisationJournalSearchCriteria2(base_types._BaseFieldType):

	__slots__ = ["_LmtTp", "_AcctId", "_BilLmtCtrPtyId", "_AcctOwnr", "_JrnlActvtyDt", "_LmtCcy"]
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
	def AcctOwnr(self):
		return self._AcctOwnr

	@AcctOwnr.setter
	def AcctOwnr(self, value):
		self._AcctOwnr = value if type(value) != base_types.auto else self.make_default("AcctOwnr")

	@AcctOwnr.deleter
	def AcctOwnr(self):
		del self._AcctOwnr
		self._AcctOwnr = None

	@property
	def BilLmtCtrPtyId(self):
		return self._BilLmtCtrPtyId

	@BilLmtCtrPtyId.setter
	def BilLmtCtrPtyId(self, value):
		self._BilLmtCtrPtyId = value if type(value) != base_types.auto else self.make_default("BilLmtCtrPtyId")

	@BilLmtCtrPtyId.deleter
	def BilLmtCtrPtyId(self):
		del self._BilLmtCtrPtyId
		self._BilLmtCtrPtyId = None

	@property
	def JrnlActvtyDt(self):
		return self._JrnlActvtyDt

	@JrnlActvtyDt.setter
	def JrnlActvtyDt(self, value):
		self._JrnlActvtyDt = value if type(value) != base_types.auto else self.make_default("JrnlActvtyDt")

	@JrnlActvtyDt.deleter
	def JrnlActvtyDt(self):
		del self._JrnlActvtyDt
		self._JrnlActvtyDt = None

	@property
	def LmtCcy(self):
		return self._LmtCcy

	@LmtCcy.setter
	def LmtCcy(self, value):
		self._LmtCcy = value if type(value) != base_types.auto else self.make_default("LmtCcy")

	@LmtCcy.deleter
	def LmtCcy(self):
		del self._LmtCcy
		self._LmtCcy = None

	@property
	def LmtTp(self):
		return self._LmtTp

	@LmtTp.setter
	def LmtTp(self, value):
		self._LmtTp = value if type(value) != base_types.auto else self.make_default("LmtTp")

	@LmtTp.deleter
	def LmtTp(self):
		del self._LmtTp
		self._LmtTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctId', type=AccountIdentification4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctOwnr', type=PartyIdentification136, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BilLmtCtrPtyId', type=SystemPartyIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='JrnlActvtyDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LmtCcy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LmtTp', type=LimitType4Code, min=0, max=None, mutex_group=None, array=True),
	))

