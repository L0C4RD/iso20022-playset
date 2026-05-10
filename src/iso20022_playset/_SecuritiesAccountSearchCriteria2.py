from . import base_types
from .Max35Text import Max35Text
from .SystemSecuritiesAccountType1Choice import SystemSecuritiesAccountType1Choice
from .Exact4AlphaNumericText import Exact4AlphaNumericText
from .PartyIdentification136 import PartyIdentification136
from .SystemPartyType1Choice import SystemPartyType1Choice
from .DatePeriodSearch1Choice import DatePeriodSearch1Choice
from .SystemPartyIdentification8 import SystemPartyIdentification8

class SecuritiesAccountSearchCriteria2(base_types._BaseFieldType):

	__slots__ = ["_AcctSvcr", "_AcctTp", "_PtyTp", "_OpngDt", "_PricgSchme", "_AcctId", "_EndInvstrFlg", "_ClsgDt", "_AcctOwnr"]
	@property
	def AcctSvcr(self):
		return self._AcctSvcr

	@AcctSvcr.setter
	def AcctSvcr(self, value):
		self._AcctSvcr = value if type(value) != base_types.auto else self.make_default("AcctSvcr")

	@AcctSvcr.deleter
	def AcctSvcr(self):
		del self._AcctSvcr
		self._AcctSvcr = None

	@property
	def AcctTp(self):
		return self._AcctTp

	@AcctTp.setter
	def AcctTp(self, value):
		self._AcctTp = value if type(value) != base_types.auto else self.make_default("AcctTp")

	@AcctTp.deleter
	def AcctTp(self):
		del self._AcctTp
		self._AcctTp = None

	@property
	def PtyTp(self):
		return self._PtyTp

	@PtyTp.setter
	def PtyTp(self, value):
		self._PtyTp = value if type(value) != base_types.auto else self.make_default("PtyTp")

	@PtyTp.deleter
	def PtyTp(self):
		del self._PtyTp
		self._PtyTp = None

	@property
	def OpngDt(self):
		return self._OpngDt

	@OpngDt.setter
	def OpngDt(self, value):
		self._OpngDt = value if type(value) != base_types.auto else self.make_default("OpngDt")

	@OpngDt.deleter
	def OpngDt(self):
		del self._OpngDt
		self._OpngDt = None

	@property
	def PricgSchme(self):
		return self._PricgSchme

	@PricgSchme.setter
	def PricgSchme(self, value):
		self._PricgSchme = value if type(value) != base_types.auto else self.make_default("PricgSchme")

	@PricgSchme.deleter
	def PricgSchme(self):
		del self._PricgSchme
		self._PricgSchme = None

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
	def EndInvstrFlg(self):
		return self._EndInvstrFlg

	@EndInvstrFlg.setter
	def EndInvstrFlg(self, value):
		self._EndInvstrFlg = value if type(value) != base_types.auto else self.make_default("EndInvstrFlg")

	@EndInvstrFlg.deleter
	def EndInvstrFlg(self):
		del self._EndInvstrFlg
		self._EndInvstrFlg = None

	@property
	def ClsgDt(self):
		return self._ClsgDt

	@ClsgDt.setter
	def ClsgDt(self, value):
		self._ClsgDt = value if type(value) != base_types.auto else self.make_default("ClsgDt")

	@ClsgDt.deleter
	def ClsgDt(self):
		del self._ClsgDt
		self._ClsgDt = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctSvcr', type=PartyIdentification136, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctTp', type=SystemSecuritiesAccountType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyTp', type=SystemPartyType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OpngDt', type=DatePeriodSearch1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricgSchme', type=Exact4AlphaNumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EndInvstrFlg', type=Exact4AlphaNumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClsgDt', type=DatePeriodSearch1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctOwnr', type=SystemPartyIdentification8, min=0, max=1, mutex_group=None, array=False),
	))

