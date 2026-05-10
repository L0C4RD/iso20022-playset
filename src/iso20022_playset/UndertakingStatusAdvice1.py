import base_types
import Undertaking8
import Document9
import StatusReasonInformation8
import ExternalUndertakingStatusCategory1Code
import Number
import ReportedAmount1
import OriginalMessage1
import Max35Text
import Max2000Text
import UndertakingStatus3Code
import PartyIdentification43

class UndertakingStatusAdvice1(base_types._BaseFieldType):

	__slots__ = ["_AmdmntSeqNb", "_OrgnlMsgDtls", "_AdvsgPtyRefNb", "_StsCtgy", "_StsRsn", "_AddtlInf", "_UdrtkgId", "_RptdAmt", "_NclsdFile", "_InitgPty", "_CnfrmrRefNb", "_Sts"]
	@property
	def AmdmntSeqNb(self):
		return self._AmdmntSeqNb

	@AmdmntSeqNb.setter
	def AmdmntSeqNb(self, value):
		self._AmdmntSeqNb = value if type(value) != auto else self.make_default("AmdmntSeqNb")

	@AmdmntSeqNb.deleter
	def AmdmntSeqNb(self):
		del self._AmdmntSeqNb
		self._AmdmntSeqNb = None

	@property
	def OrgnlMsgDtls(self):
		return self._OrgnlMsgDtls

	@OrgnlMsgDtls.setter
	def OrgnlMsgDtls(self, value):
		self._OrgnlMsgDtls = value if type(value) != auto else self.make_default("OrgnlMsgDtls")

	@OrgnlMsgDtls.deleter
	def OrgnlMsgDtls(self):
		del self._OrgnlMsgDtls
		self._OrgnlMsgDtls = None

	@property
	def AdvsgPtyRefNb(self):
		return self._AdvsgPtyRefNb

	@AdvsgPtyRefNb.setter
	def AdvsgPtyRefNb(self, value):
		self._AdvsgPtyRefNb = value if type(value) != auto else self.make_default("AdvsgPtyRefNb")

	@AdvsgPtyRefNb.deleter
	def AdvsgPtyRefNb(self):
		del self._AdvsgPtyRefNb
		self._AdvsgPtyRefNb = None

	@property
	def StsCtgy(self):
		return self._StsCtgy

	@StsCtgy.setter
	def StsCtgy(self, value):
		self._StsCtgy = value if type(value) != auto else self.make_default("StsCtgy")

	@StsCtgy.deleter
	def StsCtgy(self):
		del self._StsCtgy
		self._StsCtgy = None

	@property
	def StsRsn(self):
		return self._StsRsn

	@StsRsn.setter
	def StsRsn(self, value):
		self._StsRsn = value if type(value) != auto else self.make_default("StsRsn")

	@StsRsn.deleter
	def StsRsn(self):
		del self._StsRsn
		self._StsRsn = None

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
	def UdrtkgId(self):
		return self._UdrtkgId

	@UdrtkgId.setter
	def UdrtkgId(self, value):
		self._UdrtkgId = value if type(value) != auto else self.make_default("UdrtkgId")

	@UdrtkgId.deleter
	def UdrtkgId(self):
		del self._UdrtkgId
		self._UdrtkgId = None

	@property
	def RptdAmt(self):
		return self._RptdAmt

	@RptdAmt.setter
	def RptdAmt(self, value):
		self._RptdAmt = value if type(value) != auto else self.make_default("RptdAmt")

	@RptdAmt.deleter
	def RptdAmt(self):
		del self._RptdAmt
		self._RptdAmt = None

	@property
	def NclsdFile(self):
		return self._NclsdFile

	@NclsdFile.setter
	def NclsdFile(self, value):
		self._NclsdFile = value if type(value) != auto else self.make_default("NclsdFile")

	@NclsdFile.deleter
	def NclsdFile(self):
		del self._NclsdFile
		self._NclsdFile = None

	@property
	def InitgPty(self):
		return self._InitgPty

	@InitgPty.setter
	def InitgPty(self, value):
		self._InitgPty = value if type(value) != auto else self.make_default("InitgPty")

	@InitgPty.deleter
	def InitgPty(self):
		del self._InitgPty
		self._InitgPty = None

	@property
	def CnfrmrRefNb(self):
		return self._CnfrmrRefNb

	@CnfrmrRefNb.setter
	def CnfrmrRefNb(self, value):
		self._CnfrmrRefNb = value if type(value) != auto else self.make_default("CnfrmrRefNb")

	@CnfrmrRefNb.deleter
	def CnfrmrRefNb(self):
		del self._CnfrmrRefNb
		self._CnfrmrRefNb = None

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if type(value) != auto else self.make_default("Sts")

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AmdmntSeqNb', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlMsgDtls', type=OriginalMessage1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AdvsgPtyRefNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsCtgy', type=ExternalUndertakingStatusCategory1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsRsn', type=StatusReasonInformation8, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlInf', type=Max2000Text, min=0, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='UdrtkgId', type=Undertaking8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptdAmt', type=ReportedAmount1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NclsdFile', type=Document9, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InitgPty', type=PartyIdentification43, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CnfrmrRefNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sts', type=UndertakingStatus3Code, min=1, max=1, mutex_group=None, array=False),
	))

