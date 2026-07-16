# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DatePeriodSearch1Choice
from . import Exact4AlphaNumericText
from . import Max35Text
from . import PartyIdentification136
from . import SystemPartyIdentification8
from . import SystemPartyType1Choice
from . import SystemSecuritiesAccountType1Choice

class SecuritiesAccountSearchCriteria2(base_types._BaseFieldType):

	__slots__ = ["_AcctId", "_AcctOwnr", "_AcctSvcr", "_AcctTp", "_ClsgDt", "_EndInvstrFlg", "_OpngDt", "_PricgSchme", "_PtyTp"]
	@property
	def AcctId(self):
		return self._AcctId

	@AcctId.setter
	def AcctId(self, value):
		self._AcctId = value if value is not None else base_types.UninitialisedField(self, 'AcctId', Max35Text, False)

	@AcctId.deleter
	def AcctId(self):
		del self._AcctId
		self._AcctId = base_types.UninitialisedField(self, 'AcctId', Max35Text, False)

	@property
	def AcctOwnr(self):
		return self._AcctOwnr

	@AcctOwnr.setter
	def AcctOwnr(self, value):
		self._AcctOwnr = value if value is not None else base_types.UninitialisedField(self, 'AcctOwnr', SystemPartyIdentification8, False)

	@AcctOwnr.deleter
	def AcctOwnr(self):
		del self._AcctOwnr
		self._AcctOwnr = base_types.UninitialisedField(self, 'AcctOwnr', SystemPartyIdentification8, False)

	@property
	def AcctSvcr(self):
		return self._AcctSvcr

	@AcctSvcr.setter
	def AcctSvcr(self, value):
		self._AcctSvcr = value if value is not None else base_types.UninitialisedField(self, 'AcctSvcr', PartyIdentification136, False)

	@AcctSvcr.deleter
	def AcctSvcr(self):
		del self._AcctSvcr
		self._AcctSvcr = base_types.UninitialisedField(self, 'AcctSvcr', PartyIdentification136, False)

	@property
	def AcctTp(self):
		return self._AcctTp

	@AcctTp.setter
	def AcctTp(self, value):
		self._AcctTp = value if value is not None else base_types.UninitialisedField(self, 'AcctTp', SystemSecuritiesAccountType1Choice, False)

	@AcctTp.deleter
	def AcctTp(self):
		del self._AcctTp
		self._AcctTp = base_types.UninitialisedField(self, 'AcctTp', SystemSecuritiesAccountType1Choice, False)

	@property
	def ClsgDt(self):
		return self._ClsgDt

	@ClsgDt.setter
	def ClsgDt(self, value):
		self._ClsgDt = value if value is not None else base_types.UninitialisedField(self, 'ClsgDt', DatePeriodSearch1Choice, False)

	@ClsgDt.deleter
	def ClsgDt(self):
		del self._ClsgDt
		self._ClsgDt = base_types.UninitialisedField(self, 'ClsgDt', DatePeriodSearch1Choice, False)

	@property
	def EndInvstrFlg(self):
		return self._EndInvstrFlg

	@EndInvstrFlg.setter
	def EndInvstrFlg(self, value):
		self._EndInvstrFlg = value if value is not None else base_types.UninitialisedField(self, 'EndInvstrFlg', Exact4AlphaNumericText, False)

	@EndInvstrFlg.deleter
	def EndInvstrFlg(self):
		del self._EndInvstrFlg
		self._EndInvstrFlg = base_types.UninitialisedField(self, 'EndInvstrFlg', Exact4AlphaNumericText, False)

	@property
	def OpngDt(self):
		return self._OpngDt

	@OpngDt.setter
	def OpngDt(self, value):
		self._OpngDt = value if value is not None else base_types.UninitialisedField(self, 'OpngDt', DatePeriodSearch1Choice, False)

	@OpngDt.deleter
	def OpngDt(self):
		del self._OpngDt
		self._OpngDt = base_types.UninitialisedField(self, 'OpngDt', DatePeriodSearch1Choice, False)

	@property
	def PricgSchme(self):
		return self._PricgSchme

	@PricgSchme.setter
	def PricgSchme(self, value):
		self._PricgSchme = value if value is not None else base_types.UninitialisedField(self, 'PricgSchme', Exact4AlphaNumericText, False)

	@PricgSchme.deleter
	def PricgSchme(self):
		del self._PricgSchme
		self._PricgSchme = base_types.UninitialisedField(self, 'PricgSchme', Exact4AlphaNumericText, False)

	@property
	def PtyTp(self):
		return self._PtyTp

	@PtyTp.setter
	def PtyTp(self, value):
		self._PtyTp = value if value is not None else base_types.UninitialisedField(self, 'PtyTp', SystemPartyType1Choice, False)

	@PtyTp.deleter
	def PtyTp(self):
		del self._PtyTp
		self._PtyTp = base_types.UninitialisedField(self, 'PtyTp', SystemPartyType1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctOwnr', type=SystemPartyIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctSvcr', type=PartyIdentification136, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctTp', type=SystemSecuritiesAccountType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClsgDt', type=DatePeriodSearch1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EndInvstrFlg', type=Exact4AlphaNumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OpngDt', type=DatePeriodSearch1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricgSchme', type=Exact4AlphaNumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyTp', type=SystemPartyType1Choice, min=0, max=1, mutex_group=None, array=False),
	))