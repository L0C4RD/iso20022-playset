# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalQueryParameters15
from . import BlockChainAddressWallet3
from . import DocumentNumber13
from . import PartyIdentification144
from . import SecuritiesAccount19
from . import Statement83
from . import SupplementaryData1

class SecuritiesStatementQueryV09(base_types._BaseFieldType):

	__slots__ = ["_AcctOwnr", "_AddtlQryParams", "_BlckChainAdrOrWllt", "_SfkpgAcct", "_SplmtryData", "_StmtGnlDtls", "_StmtReqd"]
	@property
	def AcctOwnr(self):
		return self._AcctOwnr

	@AcctOwnr.setter
	def AcctOwnr(self, value):
		self._AcctOwnr = value if value is not None else base_types.UninitialisedField(self, 'AcctOwnr', PartyIdentification144, False)

	@AcctOwnr.deleter
	def AcctOwnr(self):
		del self._AcctOwnr
		self._AcctOwnr = base_types.UninitialisedField(self, 'AcctOwnr', PartyIdentification144, False)

	@property
	def AddtlQryParams(self):
		return self._AddtlQryParams

	@AddtlQryParams.setter
	def AddtlQryParams(self, value):
		self._AddtlQryParams = value if value is not None else base_types.UninitialisedField(self, 'AddtlQryParams', AdditionalQueryParameters15, True)

	@AddtlQryParams.deleter
	def AddtlQryParams(self):
		del self._AddtlQryParams
		self._AddtlQryParams = base_types.UninitialisedField(self, 'AddtlQryParams', AdditionalQueryParameters15, True)

	@property
	def BlckChainAdrOrWllt(self):
		return self._BlckChainAdrOrWllt

	@BlckChainAdrOrWllt.setter
	def BlckChainAdrOrWllt(self, value):
		self._BlckChainAdrOrWllt = value if value is not None else base_types.UninitialisedField(self, 'BlckChainAdrOrWllt', BlockChainAddressWallet3, False)

	@BlckChainAdrOrWllt.deleter
	def BlckChainAdrOrWllt(self):
		del self._BlckChainAdrOrWllt
		self._BlckChainAdrOrWllt = base_types.UninitialisedField(self, 'BlckChainAdrOrWllt', BlockChainAddressWallet3, False)

	@property
	def SfkpgAcct(self):
		return self._SfkpgAcct

	@SfkpgAcct.setter
	def SfkpgAcct(self, value):
		self._SfkpgAcct = value if value is not None else base_types.UninitialisedField(self, 'SfkpgAcct', SecuritiesAccount19, False)

	@SfkpgAcct.deleter
	def SfkpgAcct(self):
		del self._SfkpgAcct
		self._SfkpgAcct = base_types.UninitialisedField(self, 'SfkpgAcct', SecuritiesAccount19, False)

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
	def StmtGnlDtls(self):
		return self._StmtGnlDtls

	@StmtGnlDtls.setter
	def StmtGnlDtls(self, value):
		self._StmtGnlDtls = value if value is not None else base_types.UninitialisedField(self, 'StmtGnlDtls', Statement83, False)

	@StmtGnlDtls.deleter
	def StmtGnlDtls(self):
		del self._StmtGnlDtls
		self._StmtGnlDtls = base_types.UninitialisedField(self, 'StmtGnlDtls', Statement83, False)

	@property
	def StmtReqd(self):
		return self._StmtReqd

	@StmtReqd.setter
	def StmtReqd(self, value):
		self._StmtReqd = value if value is not None else base_types.UninitialisedField(self, 'StmtReqd', DocumentNumber13, False)

	@StmtReqd.deleter
	def StmtReqd(self):
		del self._StmtReqd
		self._StmtReqd = base_types.UninitialisedField(self, 'StmtReqd', DocumentNumber13, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctOwnr', type=PartyIdentification144, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlQryParams', type=AdditionalQueryParameters15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BlckChainAdrOrWllt', type=BlockChainAddressWallet3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgAcct', type=SecuritiesAccount19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='StmtGnlDtls', type=Statement83, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmtReqd', type=DocumentNumber13, min=1, max=1, mutex_group=None, array=False),
	))