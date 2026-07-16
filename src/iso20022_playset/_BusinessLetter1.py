# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GovernanceRules2
from . import ISODate
from . import Max2000Text
from . import Max350Text
from . import Max35Text
from . import Priority3Code
from . import QualifiedDocumentInformation1
from . import QualifiedPartyAndXMLSignature1
from . import QualifiedPartyIdentification1
from . import ValidationStatusInformation1

class BusinessLetter1(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_ApplCntxt", "_AssoctdDoc", "_AuthstnUsr", "_CnttIdr", "_CpyRcpt", "_DgtlSgntr", "_Dt", "_GovngCtrct", "_InstrPrty", "_LglCntxt", "_LttrIdr", "_Ntce", "_Orgtr", "_OthrPty", "_PmryRcpt", "_RltdLttr", "_RltdMsg", "_RspnRcpt", "_Sndr", "_VldtnStsInf"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', Max2000Text, False)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', Max2000Text, False)

	@property
	def ApplCntxt(self):
		return self._ApplCntxt

	@ApplCntxt.setter
	def ApplCntxt(self, value):
		self._ApplCntxt = value if value is not None else base_types.UninitialisedField(self, 'ApplCntxt', Max35Text, False)

	@ApplCntxt.deleter
	def ApplCntxt(self):
		del self._ApplCntxt
		self._ApplCntxt = base_types.UninitialisedField(self, 'ApplCntxt', Max35Text, False)

	@property
	def AssoctdDoc(self):
		return self._AssoctdDoc

	@AssoctdDoc.setter
	def AssoctdDoc(self, value):
		self._AssoctdDoc = value if value is not None else base_types.UninitialisedField(self, 'AssoctdDoc', QualifiedDocumentInformation1, True)

	@AssoctdDoc.deleter
	def AssoctdDoc(self):
		del self._AssoctdDoc
		self._AssoctdDoc = base_types.UninitialisedField(self, 'AssoctdDoc', QualifiedDocumentInformation1, True)

	@property
	def AuthstnUsr(self):
		return self._AuthstnUsr

	@AuthstnUsr.setter
	def AuthstnUsr(self, value):
		self._AuthstnUsr = value if value is not None else base_types.UninitialisedField(self, 'AuthstnUsr', QualifiedPartyIdentification1, True)

	@AuthstnUsr.deleter
	def AuthstnUsr(self):
		del self._AuthstnUsr
		self._AuthstnUsr = base_types.UninitialisedField(self, 'AuthstnUsr', QualifiedPartyIdentification1, True)

	@property
	def CnttIdr(self):
		return self._CnttIdr

	@CnttIdr.setter
	def CnttIdr(self, value):
		self._CnttIdr = value if value is not None else base_types.UninitialisedField(self, 'CnttIdr', Max35Text, True)

	@CnttIdr.deleter
	def CnttIdr(self):
		del self._CnttIdr
		self._CnttIdr = base_types.UninitialisedField(self, 'CnttIdr', Max35Text, True)

	@property
	def CpyRcpt(self):
		return self._CpyRcpt

	@CpyRcpt.setter
	def CpyRcpt(self, value):
		self._CpyRcpt = value if value is not None else base_types.UninitialisedField(self, 'CpyRcpt', QualifiedPartyIdentification1, True)

	@CpyRcpt.deleter
	def CpyRcpt(self):
		del self._CpyRcpt
		self._CpyRcpt = base_types.UninitialisedField(self, 'CpyRcpt', QualifiedPartyIdentification1, True)

	@property
	def DgtlSgntr(self):
		return self._DgtlSgntr

	@DgtlSgntr.setter
	def DgtlSgntr(self, value):
		self._DgtlSgntr = value if value is not None else base_types.UninitialisedField(self, 'DgtlSgntr', QualifiedPartyAndXMLSignature1, True)

	@DgtlSgntr.deleter
	def DgtlSgntr(self):
		del self._DgtlSgntr
		self._DgtlSgntr = base_types.UninitialisedField(self, 'DgtlSgntr', QualifiedPartyAndXMLSignature1, True)

	@property
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if value is not None else base_types.UninitialisedField(self, 'Dt', ISODate, False)

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = base_types.UninitialisedField(self, 'Dt', ISODate, False)

	@property
	def GovngCtrct(self):
		return self._GovngCtrct

	@GovngCtrct.setter
	def GovngCtrct(self, value):
		self._GovngCtrct = value if value is not None else base_types.UninitialisedField(self, 'GovngCtrct', QualifiedDocumentInformation1, True)

	@GovngCtrct.deleter
	def GovngCtrct(self):
		del self._GovngCtrct
		self._GovngCtrct = base_types.UninitialisedField(self, 'GovngCtrct', QualifiedDocumentInformation1, True)

	@property
	def InstrPrty(self):
		return self._InstrPrty

	@InstrPrty.setter
	def InstrPrty(self, value):
		self._InstrPrty = value if value is not None else base_types.UninitialisedField(self, 'InstrPrty', Priority3Code, False)

	@InstrPrty.deleter
	def InstrPrty(self):
		del self._InstrPrty
		self._InstrPrty = base_types.UninitialisedField(self, 'InstrPrty', Priority3Code, False)

	@property
	def LglCntxt(self):
		return self._LglCntxt

	@LglCntxt.setter
	def LglCntxt(self, value):
		self._LglCntxt = value if value is not None else base_types.UninitialisedField(self, 'LglCntxt', GovernanceRules2, True)

	@LglCntxt.deleter
	def LglCntxt(self):
		del self._LglCntxt
		self._LglCntxt = base_types.UninitialisedField(self, 'LglCntxt', GovernanceRules2, True)

	@property
	def LttrIdr(self):
		return self._LttrIdr

	@LttrIdr.setter
	def LttrIdr(self, value):
		self._LttrIdr = value if value is not None else base_types.UninitialisedField(self, 'LttrIdr', QualifiedDocumentInformation1, False)

	@LttrIdr.deleter
	def LttrIdr(self):
		del self._LttrIdr
		self._LttrIdr = base_types.UninitialisedField(self, 'LttrIdr', QualifiedDocumentInformation1, False)

	@property
	def Ntce(self):
		return self._Ntce

	@Ntce.setter
	def Ntce(self, value):
		self._Ntce = value if value is not None else base_types.UninitialisedField(self, 'Ntce', Max350Text, False)

	@Ntce.deleter
	def Ntce(self):
		del self._Ntce
		self._Ntce = base_types.UninitialisedField(self, 'Ntce', Max350Text, False)

	@property
	def Orgtr(self):
		return self._Orgtr

	@Orgtr.setter
	def Orgtr(self, value):
		self._Orgtr = value if value is not None else base_types.UninitialisedField(self, 'Orgtr', QualifiedPartyIdentification1, False)

	@Orgtr.deleter
	def Orgtr(self):
		del self._Orgtr
		self._Orgtr = base_types.UninitialisedField(self, 'Orgtr', QualifiedPartyIdentification1, False)

	@property
	def OthrPty(self):
		return self._OthrPty

	@OthrPty.setter
	def OthrPty(self, value):
		self._OthrPty = value if value is not None else base_types.UninitialisedField(self, 'OthrPty', QualifiedPartyIdentification1, True)

	@OthrPty.deleter
	def OthrPty(self):
		del self._OthrPty
		self._OthrPty = base_types.UninitialisedField(self, 'OthrPty', QualifiedPartyIdentification1, True)

	@property
	def PmryRcpt(self):
		return self._PmryRcpt

	@PmryRcpt.setter
	def PmryRcpt(self, value):
		self._PmryRcpt = value if value is not None else base_types.UninitialisedField(self, 'PmryRcpt', QualifiedPartyIdentification1, True)

	@PmryRcpt.deleter
	def PmryRcpt(self):
		del self._PmryRcpt
		self._PmryRcpt = base_types.UninitialisedField(self, 'PmryRcpt', QualifiedPartyIdentification1, True)

	@property
	def RltdLttr(self):
		return self._RltdLttr

	@RltdLttr.setter
	def RltdLttr(self, value):
		self._RltdLttr = value if value is not None else base_types.UninitialisedField(self, 'RltdLttr', QualifiedDocumentInformation1, True)

	@RltdLttr.deleter
	def RltdLttr(self):
		del self._RltdLttr
		self._RltdLttr = base_types.UninitialisedField(self, 'RltdLttr', QualifiedDocumentInformation1, True)

	@property
	def RltdMsg(self):
		return self._RltdMsg

	@RltdMsg.setter
	def RltdMsg(self, value):
		self._RltdMsg = value if value is not None else base_types.UninitialisedField(self, 'RltdMsg', QualifiedDocumentInformation1, True)

	@RltdMsg.deleter
	def RltdMsg(self):
		del self._RltdMsg
		self._RltdMsg = base_types.UninitialisedField(self, 'RltdMsg', QualifiedDocumentInformation1, True)

	@property
	def RspnRcpt(self):
		return self._RspnRcpt

	@RspnRcpt.setter
	def RspnRcpt(self, value):
		self._RspnRcpt = value if value is not None else base_types.UninitialisedField(self, 'RspnRcpt', QualifiedPartyIdentification1, True)

	@RspnRcpt.deleter
	def RspnRcpt(self):
		del self._RspnRcpt
		self._RspnRcpt = base_types.UninitialisedField(self, 'RspnRcpt', QualifiedPartyIdentification1, True)

	@property
	def Sndr(self):
		return self._Sndr

	@Sndr.setter
	def Sndr(self, value):
		self._Sndr = value if value is not None else base_types.UninitialisedField(self, 'Sndr', QualifiedPartyIdentification1, True)

	@Sndr.deleter
	def Sndr(self):
		del self._Sndr
		self._Sndr = base_types.UninitialisedField(self, 'Sndr', QualifiedPartyIdentification1, True)

	@property
	def VldtnStsInf(self):
		return self._VldtnStsInf

	@VldtnStsInf.setter
	def VldtnStsInf(self, value):
		self._VldtnStsInf = value if value is not None else base_types.UninitialisedField(self, 'VldtnStsInf', ValidationStatusInformation1, False)

	@VldtnStsInf.deleter
	def VldtnStsInf(self):
		del self._VldtnStsInf
		self._VldtnStsInf = base_types.UninitialisedField(self, 'VldtnStsInf', ValidationStatusInformation1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max2000Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ApplCntxt', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AssoctdDoc', type=QualifiedDocumentInformation1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AuthstnUsr', type=QualifiedPartyIdentification1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CnttIdr', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CpyRcpt', type=QualifiedPartyIdentification1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DgtlSgntr', type=QualifiedPartyAndXMLSignature1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Dt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GovngCtrct', type=QualifiedDocumentInformation1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InstrPrty', type=Priority3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LglCntxt', type=GovernanceRules2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='LttrIdr', type=QualifiedDocumentInformation1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ntce', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Orgtr', type=QualifiedPartyIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrPty', type=QualifiedPartyIdentification1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PmryRcpt', type=QualifiedPartyIdentification1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RltdLttr', type=QualifiedDocumentInformation1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RltdMsg', type=QualifiedDocumentInformation1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RspnRcpt', type=QualifiedPartyIdentification1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sndr', type=QualifiedPartyIdentification1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='VldtnStsInf', type=ValidationStatusInformation1, min=0, max=1, mutex_group=None, array=False),
	))