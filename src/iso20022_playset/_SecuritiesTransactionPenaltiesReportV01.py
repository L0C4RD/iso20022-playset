# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Pagination1
from . import PartyIdentification136
from . import Penalty4
from . import PenaltyReport1
from . import SecuritiesAccount19
from . import SupplementaryData1

class SecuritiesTransactionPenaltiesReportV01(base_types._BaseFieldType):

	__slots__ = ["_AcctOwnr", "_AcctSvcr", "_Pnlty", "_RptGnlDtls", "_RptPgntn", "_SfkpgAcct", "_SplmtryData"]
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
	def Pnlty(self):
		return self._Pnlty

	@Pnlty.setter
	def Pnlty(self, value):
		self._Pnlty = value if value is not None else base_types.UninitialisedField(self, 'Pnlty', Penalty4, True)

	@Pnlty.deleter
	def Pnlty(self):
		del self._Pnlty
		self._Pnlty = base_types.UninitialisedField(self, 'Pnlty', Penalty4, True)

	@property
	def RptGnlDtls(self):
		return self._RptGnlDtls

	@RptGnlDtls.setter
	def RptGnlDtls(self, value):
		self._RptGnlDtls = value if value is not None else base_types.UninitialisedField(self, 'RptGnlDtls', PenaltyReport1, False)

	@RptGnlDtls.deleter
	def RptGnlDtls(self):
		del self._RptGnlDtls
		self._RptGnlDtls = base_types.UninitialisedField(self, 'RptGnlDtls', PenaltyReport1, False)

	@property
	def RptPgntn(self):
		return self._RptPgntn

	@RptPgntn.setter
	def RptPgntn(self, value):
		self._RptPgntn = value if value is not None else base_types.UninitialisedField(self, 'RptPgntn', Pagination1, False)

	@RptPgntn.deleter
	def RptPgntn(self):
		del self._RptPgntn
		self._RptPgntn = base_types.UninitialisedField(self, 'RptPgntn', Pagination1, False)

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctOwnr', type=PartyIdentification136, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctSvcr', type=PartyIdentification136, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pnlty', type=Penalty4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RptGnlDtls', type=PenaltyReport1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptPgntn', type=Pagination1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgAcct', type=SecuritiesAccount19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))