# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountOwner3Choice
from . import FinancialInstrument55
from . import Intermediary47
from . import Max350Text
from . import Max35Text
from . import PartyIdentification125Choice

class InvestmentAccount76(base_types._BaseFieldType):

	__slots__ = ["_AcctOwnr", "_AcctSvcr", "_Dsgnt", "_FndFmlyNm", "_FndTp", "_Intrmy", "_Nm", "_SctyDtls"]
	@property
	def AcctOwnr(self):
		return self._AcctOwnr

	@AcctOwnr.setter
	def AcctOwnr(self, value):
		self._AcctOwnr = value if value is not None else base_types.UninitialisedField(self, 'AcctOwnr', AccountOwner3Choice, False)

	@AcctOwnr.deleter
	def AcctOwnr(self):
		del self._AcctOwnr
		self._AcctOwnr = base_types.UninitialisedField(self, 'AcctOwnr', AccountOwner3Choice, False)

	@property
	def AcctSvcr(self):
		return self._AcctSvcr

	@AcctSvcr.setter
	def AcctSvcr(self, value):
		self._AcctSvcr = value if value is not None else base_types.UninitialisedField(self, 'AcctSvcr', PartyIdentification125Choice, False)

	@AcctSvcr.deleter
	def AcctSvcr(self):
		del self._AcctSvcr
		self._AcctSvcr = base_types.UninitialisedField(self, 'AcctSvcr', PartyIdentification125Choice, False)

	@property
	def Dsgnt(self):
		return self._Dsgnt

	@Dsgnt.setter
	def Dsgnt(self, value):
		self._Dsgnt = value if value is not None else base_types.UninitialisedField(self, 'Dsgnt', Max35Text, False)

	@Dsgnt.deleter
	def Dsgnt(self):
		del self._Dsgnt
		self._Dsgnt = base_types.UninitialisedField(self, 'Dsgnt', Max35Text, False)

	@property
	def FndFmlyNm(self):
		return self._FndFmlyNm

	@FndFmlyNm.setter
	def FndFmlyNm(self, value):
		self._FndFmlyNm = value if value is not None else base_types.UninitialisedField(self, 'FndFmlyNm', Max350Text, False)

	@FndFmlyNm.deleter
	def FndFmlyNm(self):
		del self._FndFmlyNm
		self._FndFmlyNm = base_types.UninitialisedField(self, 'FndFmlyNm', Max350Text, False)

	@property
	def FndTp(self):
		return self._FndTp

	@FndTp.setter
	def FndTp(self, value):
		self._FndTp = value if value is not None else base_types.UninitialisedField(self, 'FndTp', Max35Text, False)

	@FndTp.deleter
	def FndTp(self):
		del self._FndTp
		self._FndTp = base_types.UninitialisedField(self, 'FndTp', Max35Text, False)

	@property
	def Intrmy(self):
		return self._Intrmy

	@Intrmy.setter
	def Intrmy(self, value):
		self._Intrmy = value if value is not None else base_types.UninitialisedField(self, 'Intrmy', Intermediary47, True)

	@Intrmy.deleter
	def Intrmy(self):
		del self._Intrmy
		self._Intrmy = base_types.UninitialisedField(self, 'Intrmy', Intermediary47, True)

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if value is not None else base_types.UninitialisedField(self, 'Nm', Max35Text, False)

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = base_types.UninitialisedField(self, 'Nm', Max35Text, False)

	@property
	def SctyDtls(self):
		return self._SctyDtls

	@SctyDtls.setter
	def SctyDtls(self, value):
		self._SctyDtls = value if value is not None else base_types.UninitialisedField(self, 'SctyDtls', FinancialInstrument55, False)

	@SctyDtls.deleter
	def SctyDtls(self):
		del self._SctyDtls
		self._SctyDtls = base_types.UninitialisedField(self, 'SctyDtls', FinancialInstrument55, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctOwnr', type=AccountOwner3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctSvcr', type=PartyIdentification125Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dsgnt', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FndFmlyNm', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FndTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Intrmy', type=Intermediary47, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Nm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyDtls', type=FinancialInstrument55, min=0, max=1, mutex_group=None, array=False),
	))