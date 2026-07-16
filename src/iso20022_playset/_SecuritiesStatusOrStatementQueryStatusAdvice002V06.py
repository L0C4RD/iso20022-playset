# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BlockChainAddressWallet7
from . import DocumentIdentification55
from . import PartyIdentification156
from . import ProcessingStatus95Choice
from . import SecuritiesAccount30
from . import StatusOrStatement12Choice
from . import SupplementaryData1

class SecuritiesStatusOrStatementQueryStatusAdvice002V06(base_types._BaseFieldType):

	__slots__ = ["_AcctOwnr", "_BlckChainAdrOrWllt", "_PrcgSts", "_QryDtls", "_SfkpgAcct", "_SplmtryData", "_StsOrStmtReqd"]
	@property
	def AcctOwnr(self):
		return self._AcctOwnr

	@AcctOwnr.setter
	def AcctOwnr(self, value):
		self._AcctOwnr = value if value is not None else base_types.UninitialisedField(self, 'AcctOwnr', PartyIdentification156, False)

	@AcctOwnr.deleter
	def AcctOwnr(self):
		del self._AcctOwnr
		self._AcctOwnr = base_types.UninitialisedField(self, 'AcctOwnr', PartyIdentification156, False)

	@property
	def BlckChainAdrOrWllt(self):
		return self._BlckChainAdrOrWllt

	@BlckChainAdrOrWllt.setter
	def BlckChainAdrOrWllt(self, value):
		self._BlckChainAdrOrWllt = value if value is not None else base_types.UninitialisedField(self, 'BlckChainAdrOrWllt', BlockChainAddressWallet7, False)

	@BlckChainAdrOrWllt.deleter
	def BlckChainAdrOrWllt(self):
		del self._BlckChainAdrOrWllt
		self._BlckChainAdrOrWllt = base_types.UninitialisedField(self, 'BlckChainAdrOrWllt', BlockChainAddressWallet7, False)

	@property
	def PrcgSts(self):
		return self._PrcgSts

	@PrcgSts.setter
	def PrcgSts(self, value):
		self._PrcgSts = value if value is not None else base_types.UninitialisedField(self, 'PrcgSts', ProcessingStatus95Choice, False)

	@PrcgSts.deleter
	def PrcgSts(self):
		del self._PrcgSts
		self._PrcgSts = base_types.UninitialisedField(self, 'PrcgSts', ProcessingStatus95Choice, False)

	@property
	def QryDtls(self):
		return self._QryDtls

	@QryDtls.setter
	def QryDtls(self, value):
		self._QryDtls = value if value is not None else base_types.UninitialisedField(self, 'QryDtls', DocumentIdentification55, False)

	@QryDtls.deleter
	def QryDtls(self):
		del self._QryDtls
		self._QryDtls = base_types.UninitialisedField(self, 'QryDtls', DocumentIdentification55, False)

	@property
	def SfkpgAcct(self):
		return self._SfkpgAcct

	@SfkpgAcct.setter
	def SfkpgAcct(self, value):
		self._SfkpgAcct = value if value is not None else base_types.UninitialisedField(self, 'SfkpgAcct', SecuritiesAccount30, False)

	@SfkpgAcct.deleter
	def SfkpgAcct(self):
		del self._SfkpgAcct
		self._SfkpgAcct = base_types.UninitialisedField(self, 'SfkpgAcct', SecuritiesAccount30, False)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@property
	def StsOrStmtReqd(self):
		return self._StsOrStmtReqd

	@StsOrStmtReqd.setter
	def StsOrStmtReqd(self, value):
		self._StsOrStmtReqd = value if value is not None else base_types.UninitialisedField(self, 'StsOrStmtReqd', StatusOrStatement12Choice, False)

	@StsOrStmtReqd.deleter
	def StsOrStmtReqd(self):
		del self._StsOrStmtReqd
		self._StsOrStmtReqd = base_types.UninitialisedField(self, 'StsOrStmtReqd', StatusOrStatement12Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctOwnr', type=PartyIdentification156, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BlckChainAdrOrWllt', type=BlockChainAddressWallet7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgSts', type=ProcessingStatus95Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryDtls', type=DocumentIdentification55, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgAcct', type=SecuritiesAccount30, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='StsOrStmtReqd', type=StatusOrStatement12Choice, min=0, max=1, mutex_group=None, array=False),
	))