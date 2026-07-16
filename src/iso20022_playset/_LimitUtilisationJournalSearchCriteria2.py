# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountIdentification4Choice
from . import ActiveCurrencyCode
from . import ISODate
from . import LimitType4Code
from . import PartyIdentification136
from . import SystemPartyIdentification8

class LimitUtilisationJournalSearchCriteria2(base_types._BaseFieldType):

	__slots__ = ["_AcctId", "_AcctOwnr", "_BilLmtCtrPtyId", "_JrnlActvtyDt", "_LmtCcy", "_LmtTp"]
	@property
	def AcctId(self):
		return self._AcctId

	@AcctId.setter
	def AcctId(self, value):
		self._AcctId = value if value is not None else base_types.UninitialisedField(self, 'AcctId', AccountIdentification4Choice, False)

	@AcctId.deleter
	def AcctId(self):
		del self._AcctId
		self._AcctId = base_types.UninitialisedField(self, 'AcctId', AccountIdentification4Choice, False)

	@property
	def AcctOwnr(self):
		return self._AcctOwnr

	@AcctOwnr.setter
	def AcctOwnr(self, value):
		self._AcctOwnr = value if value is not None else base_types.UninitialisedField(self, 'AcctOwnr', PartyIdentification136, False)

	@AcctOwnr.deleter
	def AcctOwnr(self):
		del self._AcctOwnr
		self._AcctOwnr = base_types.UninitialisedField(self, 'AcctOwnr', PartyIdentification136, False)

	@property
	def BilLmtCtrPtyId(self):
		return self._BilLmtCtrPtyId

	@BilLmtCtrPtyId.setter
	def BilLmtCtrPtyId(self, value):
		self._BilLmtCtrPtyId = value if value is not None else base_types.UninitialisedField(self, 'BilLmtCtrPtyId', SystemPartyIdentification8, False)

	@BilLmtCtrPtyId.deleter
	def BilLmtCtrPtyId(self):
		del self._BilLmtCtrPtyId
		self._BilLmtCtrPtyId = base_types.UninitialisedField(self, 'BilLmtCtrPtyId', SystemPartyIdentification8, False)

	@property
	def JrnlActvtyDt(self):
		return self._JrnlActvtyDt

	@JrnlActvtyDt.setter
	def JrnlActvtyDt(self, value):
		self._JrnlActvtyDt = value if value is not None else base_types.UninitialisedField(self, 'JrnlActvtyDt', ISODate, False)

	@JrnlActvtyDt.deleter
	def JrnlActvtyDt(self):
		del self._JrnlActvtyDt
		self._JrnlActvtyDt = base_types.UninitialisedField(self, 'JrnlActvtyDt', ISODate, False)

	@property
	def LmtCcy(self):
		return self._LmtCcy

	@LmtCcy.setter
	def LmtCcy(self, value):
		self._LmtCcy = value if value is not None else base_types.UninitialisedField(self, 'LmtCcy', ActiveCurrencyCode, False)

	@LmtCcy.deleter
	def LmtCcy(self):
		del self._LmtCcy
		self._LmtCcy = base_types.UninitialisedField(self, 'LmtCcy', ActiveCurrencyCode, False)

	@property
	def LmtTp(self):
		return self._LmtTp

	@LmtTp.setter
	def LmtTp(self, value):
		self._LmtTp = value if value is not None else base_types.UninitialisedField(self, 'LmtTp', LimitType4Code, True)

	@LmtTp.deleter
	def LmtTp(self):
		del self._LmtTp
		self._LmtTp = base_types.UninitialisedField(self, 'LmtTp', LimitType4Code, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctId', type=AccountIdentification4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctOwnr', type=PartyIdentification136, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BilLmtCtrPtyId', type=SystemPartyIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='JrnlActvtyDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LmtCcy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LmtTp', type=LimitType4Code, min=0, max=None, mutex_group=None, array=True),
	))