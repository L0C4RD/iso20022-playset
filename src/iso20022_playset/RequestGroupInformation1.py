from . import base_types
from .Max350Text import Max350Text
from .FinancialInstitutionIdentification6 import FinancialInstitutionIdentification6
from .AgreementClauses1 import AgreementClauses1
from .ISODateTime import ISODateTime
from .PartyIdentificationAndAccount6 import PartyIdentificationAndAccount6
from .Max35Text import Max35Text
from .CurrencyCode import CurrencyCode
from .Max128Text import Max128Text
from .Max15NumericText import Max15NumericText
from .AdditionalInformation1 import AdditionalInformation1
from .ActiveCurrencyAndAmount import ActiveCurrencyAndAmount

class RequestGroupInformation1(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_GrpId", "_Ccy", "_TtlBlkInvcAmt", "_FincgAgrmt", "_Authstn", "_NbOfInvcReqs", "_IntrmyAgt", "_FrstAgt", "_FincgRqstr", "_AgrmtClauses", "_CreDtTm"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != base_types.auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def GrpId(self):
		return self._GrpId

	@GrpId.setter
	def GrpId(self, value):
		self._GrpId = value if type(value) != base_types.auto else self.make_default("GrpId")

	@GrpId.deleter
	def GrpId(self):
		del self._GrpId
		self._GrpId = None

	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if type(value) != base_types.auto else self.make_default("Ccy")

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = None

	@property
	def TtlBlkInvcAmt(self):
		return self._TtlBlkInvcAmt

	@TtlBlkInvcAmt.setter
	def TtlBlkInvcAmt(self, value):
		self._TtlBlkInvcAmt = value if type(value) != base_types.auto else self.make_default("TtlBlkInvcAmt")

	@TtlBlkInvcAmt.deleter
	def TtlBlkInvcAmt(self):
		del self._TtlBlkInvcAmt
		self._TtlBlkInvcAmt = None

	@property
	def FincgAgrmt(self):
		return self._FincgAgrmt

	@FincgAgrmt.setter
	def FincgAgrmt(self, value):
		self._FincgAgrmt = value if type(value) != base_types.auto else self.make_default("FincgAgrmt")

	@FincgAgrmt.deleter
	def FincgAgrmt(self):
		del self._FincgAgrmt
		self._FincgAgrmt = None

	@property
	def Authstn(self):
		return self._Authstn

	@Authstn.setter
	def Authstn(self, value):
		self._Authstn = value if type(value) != base_types.auto else self.make_default("Authstn")

	@Authstn.deleter
	def Authstn(self):
		del self._Authstn
		self._Authstn = None

	@property
	def NbOfInvcReqs(self):
		return self._NbOfInvcReqs

	@NbOfInvcReqs.setter
	def NbOfInvcReqs(self, value):
		self._NbOfInvcReqs = value if type(value) != base_types.auto else self.make_default("NbOfInvcReqs")

	@NbOfInvcReqs.deleter
	def NbOfInvcReqs(self):
		del self._NbOfInvcReqs
		self._NbOfInvcReqs = None

	@property
	def IntrmyAgt(self):
		return self._IntrmyAgt

	@IntrmyAgt.setter
	def IntrmyAgt(self, value):
		self._IntrmyAgt = value if type(value) != base_types.auto else self.make_default("IntrmyAgt")

	@IntrmyAgt.deleter
	def IntrmyAgt(self):
		del self._IntrmyAgt
		self._IntrmyAgt = None

	@property
	def FrstAgt(self):
		return self._FrstAgt

	@FrstAgt.setter
	def FrstAgt(self, value):
		self._FrstAgt = value if type(value) != base_types.auto else self.make_default("FrstAgt")

	@FrstAgt.deleter
	def FrstAgt(self):
		del self._FrstAgt
		self._FrstAgt = None

	@property
	def FincgRqstr(self):
		return self._FincgRqstr

	@FincgRqstr.setter
	def FincgRqstr(self, value):
		self._FincgRqstr = value if type(value) != base_types.auto else self.make_default("FincgRqstr")

	@FincgRqstr.deleter
	def FincgRqstr(self):
		del self._FincgRqstr
		self._FincgRqstr = None

	@property
	def AgrmtClauses(self):
		return self._AgrmtClauses

	@AgrmtClauses.setter
	def AgrmtClauses(self, value):
		self._AgrmtClauses = value if type(value) != base_types.auto else self.make_default("AgrmtClauses")

	@AgrmtClauses.deleter
	def AgrmtClauses(self):
		del self._AgrmtClauses
		self._AgrmtClauses = None

	@property
	def CreDtTm(self):
		return self._CreDtTm

	@CreDtTm.setter
	def CreDtTm(self, value):
		self._CreDtTm = value if type(value) != base_types.auto else self.make_default("CreDtTm")

	@CreDtTm.deleter
	def CreDtTm(self):
		del self._CreDtTm
		self._CreDtTm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='GrpId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=CurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlBlkInvcAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FincgAgrmt', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Authstn', type=Max128Text, min=0, max=2, mutex_group=None, array=True),
		base_types.FieldEntry(name='NbOfInvcReqs', type=Max15NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmyAgt', type=FinancialInstitutionIdentification6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrstAgt', type=FinancialInstitutionIdentification6, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FincgRqstr', type=PartyIdentificationAndAccount6, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AgrmtClauses', type=AgreementClauses1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CreDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
	))

