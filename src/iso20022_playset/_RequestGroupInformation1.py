# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import AdditionalInformation1
from . import AgreementClauses1
from . import CurrencyCode
from . import FinancialInstitutionIdentification6
from . import ISODateTime
from . import Max128Text
from . import Max15NumericText
from . import Max350Text
from . import Max35Text
from . import PartyIdentificationAndAccount6

class RequestGroupInformation1(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_AgrmtClauses", "_Authstn", "_Ccy", "_CreDtTm", "_FincgAgrmt", "_FincgRqstr", "_FrstAgt", "_GrpId", "_IntrmyAgt", "_NbOfInvcReqs", "_TtlBlkInvcAmt"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', AdditionalInformation1, True)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', AdditionalInformation1, True)

	@property
	def AgrmtClauses(self):
		return self._AgrmtClauses

	@AgrmtClauses.setter
	def AgrmtClauses(self, value):
		self._AgrmtClauses = value if value is not None else base_types.UninitialisedField(self, 'AgrmtClauses', AgreementClauses1, True)

	@AgrmtClauses.deleter
	def AgrmtClauses(self):
		del self._AgrmtClauses
		self._AgrmtClauses = base_types.UninitialisedField(self, 'AgrmtClauses', AgreementClauses1, True)

	@property
	def Authstn(self):
		return self._Authstn

	@Authstn.setter
	def Authstn(self, value):
		self._Authstn = value if value is not None else base_types.UninitialisedField(self, 'Authstn', Max128Text, True)

	@Authstn.deleter
	def Authstn(self):
		del self._Authstn
		self._Authstn = base_types.UninitialisedField(self, 'Authstn', Max128Text, True)

	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if value is not None else base_types.UninitialisedField(self, 'Ccy', CurrencyCode, False)

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = base_types.UninitialisedField(self, 'Ccy', CurrencyCode, False)

	@property
	def CreDtTm(self):
		return self._CreDtTm

	@CreDtTm.setter
	def CreDtTm(self, value):
		self._CreDtTm = value if value is not None else base_types.UninitialisedField(self, 'CreDtTm', ISODateTime, False)

	@CreDtTm.deleter
	def CreDtTm(self):
		del self._CreDtTm
		self._CreDtTm = base_types.UninitialisedField(self, 'CreDtTm', ISODateTime, False)

	@property
	def FincgAgrmt(self):
		return self._FincgAgrmt

	@FincgAgrmt.setter
	def FincgAgrmt(self, value):
		self._FincgAgrmt = value if value is not None else base_types.UninitialisedField(self, 'FincgAgrmt', Max350Text, False)

	@FincgAgrmt.deleter
	def FincgAgrmt(self):
		del self._FincgAgrmt
		self._FincgAgrmt = base_types.UninitialisedField(self, 'FincgAgrmt', Max350Text, False)

	@property
	def FincgRqstr(self):
		return self._FincgRqstr

	@FincgRqstr.setter
	def FincgRqstr(self, value):
		self._FincgRqstr = value if value is not None else base_types.UninitialisedField(self, 'FincgRqstr', PartyIdentificationAndAccount6, False)

	@FincgRqstr.deleter
	def FincgRqstr(self):
		del self._FincgRqstr
		self._FincgRqstr = base_types.UninitialisedField(self, 'FincgRqstr', PartyIdentificationAndAccount6, False)

	@property
	def FrstAgt(self):
		return self._FrstAgt

	@FrstAgt.setter
	def FrstAgt(self, value):
		self._FrstAgt = value if value is not None else base_types.UninitialisedField(self, 'FrstAgt', FinancialInstitutionIdentification6, False)

	@FrstAgt.deleter
	def FrstAgt(self):
		del self._FrstAgt
		self._FrstAgt = base_types.UninitialisedField(self, 'FrstAgt', FinancialInstitutionIdentification6, False)

	@property
	def GrpId(self):
		return self._GrpId

	@GrpId.setter
	def GrpId(self, value):
		self._GrpId = value if value is not None else base_types.UninitialisedField(self, 'GrpId', Max35Text, False)

	@GrpId.deleter
	def GrpId(self):
		del self._GrpId
		self._GrpId = base_types.UninitialisedField(self, 'GrpId', Max35Text, False)

	@property
	def IntrmyAgt(self):
		return self._IntrmyAgt

	@IntrmyAgt.setter
	def IntrmyAgt(self, value):
		self._IntrmyAgt = value if value is not None else base_types.UninitialisedField(self, 'IntrmyAgt', FinancialInstitutionIdentification6, False)

	@IntrmyAgt.deleter
	def IntrmyAgt(self):
		del self._IntrmyAgt
		self._IntrmyAgt = base_types.UninitialisedField(self, 'IntrmyAgt', FinancialInstitutionIdentification6, False)

	@property
	def NbOfInvcReqs(self):
		return self._NbOfInvcReqs

	@NbOfInvcReqs.setter
	def NbOfInvcReqs(self, value):
		self._NbOfInvcReqs = value if value is not None else base_types.UninitialisedField(self, 'NbOfInvcReqs', Max15NumericText, False)

	@NbOfInvcReqs.deleter
	def NbOfInvcReqs(self):
		del self._NbOfInvcReqs
		self._NbOfInvcReqs = base_types.UninitialisedField(self, 'NbOfInvcReqs', Max15NumericText, False)

	@property
	def TtlBlkInvcAmt(self):
		return self._TtlBlkInvcAmt

	@TtlBlkInvcAmt.setter
	def TtlBlkInvcAmt(self, value):
		self._TtlBlkInvcAmt = value if value is not None else base_types.UninitialisedField(self, 'TtlBlkInvcAmt', ActiveCurrencyAndAmount, False)

	@TtlBlkInvcAmt.deleter
	def TtlBlkInvcAmt(self):
		del self._TtlBlkInvcAmt
		self._TtlBlkInvcAmt = base_types.UninitialisedField(self, 'TtlBlkInvcAmt', ActiveCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AgrmtClauses', type=AgreementClauses1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Authstn', type=Max128Text, min=0, max=2, mutex_group=None, array=True),
		base_types.FieldEntry(name='Ccy', type=CurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CreDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FincgAgrmt', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FincgRqstr', type=PartyIdentificationAndAccount6, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrstAgt', type=FinancialInstitutionIdentification6, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrpId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmyAgt', type=FinancialInstitutionIdentification6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfInvcReqs', type=Max15NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlBlkInvcAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))