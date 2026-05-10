from . import base_types
from .Max35Text import Max35Text
from .ValidationStatusInformation1 import ValidationStatusInformation1
from .ISODate import ISODate
from .QualifiedDocumentInformation1 import QualifiedDocumentInformation1
from .Max350Text import Max350Text
from .Max2000Text import Max2000Text
from .QualifiedPartyIdentification1 import QualifiedPartyIdentification1
from .GovernanceRules2 import GovernanceRules2
from .QualifiedPartyAndXMLSignature1 import QualifiedPartyAndXMLSignature1
from .Priority3Code import Priority3Code

class BusinessLetter1(base_types._BaseFieldType):

	__slots__ = ["_GovngCtrct", "_AuthstnUsr", "_VldtnStsInf", "_InstrPrty", "_DgtlSgntr", "_OthrPty", "_CpyRcpt", "_Ntce", "_PmryRcpt", "_RltdMsg", "_AddtlInf", "_LglCntxt", "_Sndr", "_CnttIdr", "_ApplCntxt", "_AssoctdDoc", "_Orgtr", "_Dt", "_RltdLttr", "_RspnRcpt", "_LttrIdr"]
	@property
	def GovngCtrct(self):
		return self._GovngCtrct

	@GovngCtrct.setter
	def GovngCtrct(self, value):
		self._GovngCtrct = value if type(value) != auto else self.make_default("GovngCtrct")

	@GovngCtrct.deleter
	def GovngCtrct(self):
		del self._GovngCtrct
		self._GovngCtrct = None

	@property
	def AuthstnUsr(self):
		return self._AuthstnUsr

	@AuthstnUsr.setter
	def AuthstnUsr(self, value):
		self._AuthstnUsr = value if type(value) != auto else self.make_default("AuthstnUsr")

	@AuthstnUsr.deleter
	def AuthstnUsr(self):
		del self._AuthstnUsr
		self._AuthstnUsr = None

	@property
	def VldtnStsInf(self):
		return self._VldtnStsInf

	@VldtnStsInf.setter
	def VldtnStsInf(self, value):
		self._VldtnStsInf = value if type(value) != auto else self.make_default("VldtnStsInf")

	@VldtnStsInf.deleter
	def VldtnStsInf(self):
		del self._VldtnStsInf
		self._VldtnStsInf = None

	@property
	def InstrPrty(self):
		return self._InstrPrty

	@InstrPrty.setter
	def InstrPrty(self, value):
		self._InstrPrty = value if type(value) != auto else self.make_default("InstrPrty")

	@InstrPrty.deleter
	def InstrPrty(self):
		del self._InstrPrty
		self._InstrPrty = None

	@property
	def DgtlSgntr(self):
		return self._DgtlSgntr

	@DgtlSgntr.setter
	def DgtlSgntr(self, value):
		self._DgtlSgntr = value if type(value) != auto else self.make_default("DgtlSgntr")

	@DgtlSgntr.deleter
	def DgtlSgntr(self):
		del self._DgtlSgntr
		self._DgtlSgntr = None

	@property
	def OthrPty(self):
		return self._OthrPty

	@OthrPty.setter
	def OthrPty(self, value):
		self._OthrPty = value if type(value) != auto else self.make_default("OthrPty")

	@OthrPty.deleter
	def OthrPty(self):
		del self._OthrPty
		self._OthrPty = None

	@property
	def CpyRcpt(self):
		return self._CpyRcpt

	@CpyRcpt.setter
	def CpyRcpt(self, value):
		self._CpyRcpt = value if type(value) != auto else self.make_default("CpyRcpt")

	@CpyRcpt.deleter
	def CpyRcpt(self):
		del self._CpyRcpt
		self._CpyRcpt = None

	@property
	def Ntce(self):
		return self._Ntce

	@Ntce.setter
	def Ntce(self, value):
		self._Ntce = value if type(value) != auto else self.make_default("Ntce")

	@Ntce.deleter
	def Ntce(self):
		del self._Ntce
		self._Ntce = None

	@property
	def PmryRcpt(self):
		return self._PmryRcpt

	@PmryRcpt.setter
	def PmryRcpt(self, value):
		self._PmryRcpt = value if type(value) != auto else self.make_default("PmryRcpt")

	@PmryRcpt.deleter
	def PmryRcpt(self):
		del self._PmryRcpt
		self._PmryRcpt = None

	@property
	def RltdMsg(self):
		return self._RltdMsg

	@RltdMsg.setter
	def RltdMsg(self, value):
		self._RltdMsg = value if type(value) != auto else self.make_default("RltdMsg")

	@RltdMsg.deleter
	def RltdMsg(self):
		del self._RltdMsg
		self._RltdMsg = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def LglCntxt(self):
		return self._LglCntxt

	@LglCntxt.setter
	def LglCntxt(self, value):
		self._LglCntxt = value if type(value) != auto else self.make_default("LglCntxt")

	@LglCntxt.deleter
	def LglCntxt(self):
		del self._LglCntxt
		self._LglCntxt = None

	@property
	def Sndr(self):
		return self._Sndr

	@Sndr.setter
	def Sndr(self, value):
		self._Sndr = value if type(value) != auto else self.make_default("Sndr")

	@Sndr.deleter
	def Sndr(self):
		del self._Sndr
		self._Sndr = None

	@property
	def CnttIdr(self):
		return self._CnttIdr

	@CnttIdr.setter
	def CnttIdr(self, value):
		self._CnttIdr = value if type(value) != auto else self.make_default("CnttIdr")

	@CnttIdr.deleter
	def CnttIdr(self):
		del self._CnttIdr
		self._CnttIdr = None

	@property
	def ApplCntxt(self):
		return self._ApplCntxt

	@ApplCntxt.setter
	def ApplCntxt(self, value):
		self._ApplCntxt = value if type(value) != auto else self.make_default("ApplCntxt")

	@ApplCntxt.deleter
	def ApplCntxt(self):
		del self._ApplCntxt
		self._ApplCntxt = None

	@property
	def AssoctdDoc(self):
		return self._AssoctdDoc

	@AssoctdDoc.setter
	def AssoctdDoc(self, value):
		self._AssoctdDoc = value if type(value) != auto else self.make_default("AssoctdDoc")

	@AssoctdDoc.deleter
	def AssoctdDoc(self):
		del self._AssoctdDoc
		self._AssoctdDoc = None

	@property
	def Orgtr(self):
		return self._Orgtr

	@Orgtr.setter
	def Orgtr(self, value):
		self._Orgtr = value if type(value) != auto else self.make_default("Orgtr")

	@Orgtr.deleter
	def Orgtr(self):
		del self._Orgtr
		self._Orgtr = None

	@property
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if type(value) != auto else self.make_default("Dt")

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = None

	@property
	def RltdLttr(self):
		return self._RltdLttr

	@RltdLttr.setter
	def RltdLttr(self, value):
		self._RltdLttr = value if type(value) != auto else self.make_default("RltdLttr")

	@RltdLttr.deleter
	def RltdLttr(self):
		del self._RltdLttr
		self._RltdLttr = None

	@property
	def RspnRcpt(self):
		return self._RspnRcpt

	@RspnRcpt.setter
	def RspnRcpt(self, value):
		self._RspnRcpt = value if type(value) != auto else self.make_default("RspnRcpt")

	@RspnRcpt.deleter
	def RspnRcpt(self):
		del self._RspnRcpt
		self._RspnRcpt = None

	@property
	def LttrIdr(self):
		return self._LttrIdr

	@LttrIdr.setter
	def LttrIdr(self, value):
		self._LttrIdr = value if type(value) != auto else self.make_default("LttrIdr")

	@LttrIdr.deleter
	def LttrIdr(self):
		del self._LttrIdr
		self._LttrIdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='GovngCtrct', type=QualifiedDocumentInformation1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AuthstnUsr', type=QualifiedPartyIdentification1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='VldtnStsInf', type=ValidationStatusInformation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrPrty', type=Priority3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DgtlSgntr', type=QualifiedPartyAndXMLSignature1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OthrPty', type=QualifiedPartyIdentification1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CpyRcpt', type=QualifiedPartyIdentification1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Ntce', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmryRcpt', type=QualifiedPartyIdentification1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RltdMsg', type=QualifiedDocumentInformation1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlInf', type=Max2000Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LglCntxt', type=GovernanceRules2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sndr', type=QualifiedPartyIdentification1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CnttIdr', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ApplCntxt', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AssoctdDoc', type=QualifiedDocumentInformation1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Orgtr', type=QualifiedPartyIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdLttr', type=QualifiedDocumentInformation1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RspnRcpt', type=QualifiedPartyIdentification1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='LttrIdr', type=QualifiedDocumentInformation1, min=1, max=1, mutex_group=None, array=False),
	))

