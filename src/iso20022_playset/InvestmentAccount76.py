from . import base_types
import Max350Text
import PartyIdentification125Choice
import Intermediary47
import AccountOwner3Choice
import Max35Text
import FinancialInstrument55

class InvestmentAccount76(base_types._BaseFieldType):

	__slots__ = ["_AcctSvcr", "_SctyDtls", "_Nm", "_FndTp", "_AcctOwnr", "_Dsgnt", "_FndFmlyNm", "_Intrmy"]
	@property
	def AcctSvcr(self):
		return self._AcctSvcr

	@AcctSvcr.setter
	def AcctSvcr(self, value):
		self._AcctSvcr = value if type(value) != auto else self.make_default("AcctSvcr")

	@AcctSvcr.deleter
	def AcctSvcr(self):
		del self._AcctSvcr
		self._AcctSvcr = None

	@property
	def SctyDtls(self):
		return self._SctyDtls

	@SctyDtls.setter
	def SctyDtls(self, value):
		self._SctyDtls = value if type(value) != auto else self.make_default("SctyDtls")

	@SctyDtls.deleter
	def SctyDtls(self):
		del self._SctyDtls
		self._SctyDtls = None

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if type(value) != auto else self.make_default("Nm")

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = None

	@property
	def FndTp(self):
		return self._FndTp

	@FndTp.setter
	def FndTp(self, value):
		self._FndTp = value if type(value) != auto else self.make_default("FndTp")

	@FndTp.deleter
	def FndTp(self):
		del self._FndTp
		self._FndTp = None

	@property
	def AcctOwnr(self):
		return self._AcctOwnr

	@AcctOwnr.setter
	def AcctOwnr(self, value):
		self._AcctOwnr = value if type(value) != auto else self.make_default("AcctOwnr")

	@AcctOwnr.deleter
	def AcctOwnr(self):
		del self._AcctOwnr
		self._AcctOwnr = None

	@property
	def Dsgnt(self):
		return self._Dsgnt

	@Dsgnt.setter
	def Dsgnt(self, value):
		self._Dsgnt = value if type(value) != auto else self.make_default("Dsgnt")

	@Dsgnt.deleter
	def Dsgnt(self):
		del self._Dsgnt
		self._Dsgnt = None

	@property
	def FndFmlyNm(self):
		return self._FndFmlyNm

	@FndFmlyNm.setter
	def FndFmlyNm(self, value):
		self._FndFmlyNm = value if type(value) != auto else self.make_default("FndFmlyNm")

	@FndFmlyNm.deleter
	def FndFmlyNm(self):
		del self._FndFmlyNm
		self._FndFmlyNm = None

	@property
	def Intrmy(self):
		return self._Intrmy

	@Intrmy.setter
	def Intrmy(self, value):
		self._Intrmy = value if type(value) != auto else self.make_default("Intrmy")

	@Intrmy.deleter
	def Intrmy(self):
		del self._Intrmy
		self._Intrmy = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctSvcr', type=PartyIdentification125Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyDtls', type=FinancialInstrument55, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FndTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctOwnr', type=AccountOwner3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dsgnt', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FndFmlyNm', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Intrmy', type=Intermediary47, min=0, max=None, mutex_group=None, array=True),
	))

