# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import OrderOriginatorEligibility1Code
from . import PartyIdentification139
from . import SubAccount6

class InvestmentAccount78(base_types._BaseFieldType):

	__slots__ = ["_AcctDsgnt", "_AcctId", "_AcctNm", "_AcctSvcr", "_OrdrOrgtrElgblty", "_OwnrId", "_SubAcctDtls"]
	@property
	def AcctDsgnt(self):
		return self._AcctDsgnt

	@AcctDsgnt.setter
	def AcctDsgnt(self, value):
		self._AcctDsgnt = value if value is not None else base_types.UninitialisedField(self, 'AcctDsgnt', Max35Text, False)

	@AcctDsgnt.deleter
	def AcctDsgnt(self):
		del self._AcctDsgnt
		self._AcctDsgnt = base_types.UninitialisedField(self, 'AcctDsgnt', Max35Text, False)

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
	def AcctNm(self):
		return self._AcctNm

	@AcctNm.setter
	def AcctNm(self, value):
		self._AcctNm = value if value is not None else base_types.UninitialisedField(self, 'AcctNm', Max35Text, False)

	@AcctNm.deleter
	def AcctNm(self):
		del self._AcctNm
		self._AcctNm = base_types.UninitialisedField(self, 'AcctNm', Max35Text, False)

	@property
	def AcctSvcr(self):
		return self._AcctSvcr

	@AcctSvcr.setter
	def AcctSvcr(self, value):
		self._AcctSvcr = value if value is not None else base_types.UninitialisedField(self, 'AcctSvcr', PartyIdentification139, False)

	@AcctSvcr.deleter
	def AcctSvcr(self):
		del self._AcctSvcr
		self._AcctSvcr = base_types.UninitialisedField(self, 'AcctSvcr', PartyIdentification139, False)

	@property
	def OrdrOrgtrElgblty(self):
		return self._OrdrOrgtrElgblty

	@OrdrOrgtrElgblty.setter
	def OrdrOrgtrElgblty(self, value):
		self._OrdrOrgtrElgblty = value if value is not None else base_types.UninitialisedField(self, 'OrdrOrgtrElgblty', OrderOriginatorEligibility1Code, False)

	@OrdrOrgtrElgblty.deleter
	def OrdrOrgtrElgblty(self):
		del self._OrdrOrgtrElgblty
		self._OrdrOrgtrElgblty = base_types.UninitialisedField(self, 'OrdrOrgtrElgblty', OrderOriginatorEligibility1Code, False)

	@property
	def OwnrId(self):
		return self._OwnrId

	@OwnrId.setter
	def OwnrId(self, value):
		self._OwnrId = value if value is not None else base_types.UninitialisedField(self, 'OwnrId', PartyIdentification139, True)

	@OwnrId.deleter
	def OwnrId(self):
		del self._OwnrId
		self._OwnrId = base_types.UninitialisedField(self, 'OwnrId', PartyIdentification139, True)

	@property
	def SubAcctDtls(self):
		return self._SubAcctDtls

	@SubAcctDtls.setter
	def SubAcctDtls(self, value):
		self._SubAcctDtls = value if value is not None else base_types.UninitialisedField(self, 'SubAcctDtls', SubAccount6, False)

	@SubAcctDtls.deleter
	def SubAcctDtls(self):
		del self._SubAcctDtls
		self._SubAcctDtls = base_types.UninitialisedField(self, 'SubAcctDtls', SubAccount6, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctDsgnt', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctSvcr', type=PartyIdentification139, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrOrgtrElgblty', type=OrderOriginatorEligibility1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OwnrId', type=PartyIdentification139, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SubAcctDtls', type=SubAccount6, min=0, max=1, mutex_group=None, array=False),
	))