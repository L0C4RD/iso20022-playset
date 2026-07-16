# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Document9
from . import ExternalUndertakingStatusCategory1Code
from . import Max2000Text
from . import Max35Text
from . import Number
from . import OriginalMessage1
from . import PartyIdentification43
from . import ReportedAmount1
from . import StatusReasonInformation8
from . import Undertaking8
from . import UndertakingStatus3Code

class UndertakingStatusAdvice1(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_AdvsgPtyRefNb", "_AmdmntSeqNb", "_CnfrmrRefNb", "_InitgPty", "_NclsdFile", "_OrgnlMsgDtls", "_RptdAmt", "_Sts", "_StsCtgy", "_StsRsn", "_UdrtkgId"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', Max2000Text, True)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', Max2000Text, True)

	@property
	def AdvsgPtyRefNb(self):
		return self._AdvsgPtyRefNb

	@AdvsgPtyRefNb.setter
	def AdvsgPtyRefNb(self, value):
		self._AdvsgPtyRefNb = value if value is not None else base_types.UninitialisedField(self, 'AdvsgPtyRefNb', Max35Text, False)

	@AdvsgPtyRefNb.deleter
	def AdvsgPtyRefNb(self):
		del self._AdvsgPtyRefNb
		self._AdvsgPtyRefNb = base_types.UninitialisedField(self, 'AdvsgPtyRefNb', Max35Text, False)

	@property
	def AmdmntSeqNb(self):
		return self._AmdmntSeqNb

	@AmdmntSeqNb.setter
	def AmdmntSeqNb(self, value):
		self._AmdmntSeqNb = value if value is not None else base_types.UninitialisedField(self, 'AmdmntSeqNb', Number, False)

	@AmdmntSeqNb.deleter
	def AmdmntSeqNb(self):
		del self._AmdmntSeqNb
		self._AmdmntSeqNb = base_types.UninitialisedField(self, 'AmdmntSeqNb', Number, False)

	@property
	def CnfrmrRefNb(self):
		return self._CnfrmrRefNb

	@CnfrmrRefNb.setter
	def CnfrmrRefNb(self, value):
		self._CnfrmrRefNb = value if value is not None else base_types.UninitialisedField(self, 'CnfrmrRefNb', Max35Text, False)

	@CnfrmrRefNb.deleter
	def CnfrmrRefNb(self):
		del self._CnfrmrRefNb
		self._CnfrmrRefNb = base_types.UninitialisedField(self, 'CnfrmrRefNb', Max35Text, False)

	@property
	def InitgPty(self):
		return self._InitgPty

	@InitgPty.setter
	def InitgPty(self, value):
		self._InitgPty = value if value is not None else base_types.UninitialisedField(self, 'InitgPty', PartyIdentification43, False)

	@InitgPty.deleter
	def InitgPty(self):
		del self._InitgPty
		self._InitgPty = base_types.UninitialisedField(self, 'InitgPty', PartyIdentification43, False)

	@property
	def NclsdFile(self):
		return self._NclsdFile

	@NclsdFile.setter
	def NclsdFile(self, value):
		self._NclsdFile = value if value is not None else base_types.UninitialisedField(self, 'NclsdFile', Document9, True)

	@NclsdFile.deleter
	def NclsdFile(self):
		del self._NclsdFile
		self._NclsdFile = base_types.UninitialisedField(self, 'NclsdFile', Document9, True)

	@property
	def OrgnlMsgDtls(self):
		return self._OrgnlMsgDtls

	@OrgnlMsgDtls.setter
	def OrgnlMsgDtls(self, value):
		self._OrgnlMsgDtls = value if value is not None else base_types.UninitialisedField(self, 'OrgnlMsgDtls', OriginalMessage1, False)

	@OrgnlMsgDtls.deleter
	def OrgnlMsgDtls(self):
		del self._OrgnlMsgDtls
		self._OrgnlMsgDtls = base_types.UninitialisedField(self, 'OrgnlMsgDtls', OriginalMessage1, False)

	@property
	def RptdAmt(self):
		return self._RptdAmt

	@RptdAmt.setter
	def RptdAmt(self, value):
		self._RptdAmt = value if value is not None else base_types.UninitialisedField(self, 'RptdAmt', ReportedAmount1, True)

	@RptdAmt.deleter
	def RptdAmt(self):
		del self._RptdAmt
		self._RptdAmt = base_types.UninitialisedField(self, 'RptdAmt', ReportedAmount1, True)

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if value is not None else base_types.UninitialisedField(self, 'Sts', UndertakingStatus3Code, False)

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = base_types.UninitialisedField(self, 'Sts', UndertakingStatus3Code, False)

	@property
	def StsCtgy(self):
		return self._StsCtgy

	@StsCtgy.setter
	def StsCtgy(self, value):
		self._StsCtgy = value if value is not None else base_types.UninitialisedField(self, 'StsCtgy', ExternalUndertakingStatusCategory1Code, False)

	@StsCtgy.deleter
	def StsCtgy(self):
		del self._StsCtgy
		self._StsCtgy = base_types.UninitialisedField(self, 'StsCtgy', ExternalUndertakingStatusCategory1Code, False)

	@property
	def StsRsn(self):
		return self._StsRsn

	@StsRsn.setter
	def StsRsn(self, value):
		self._StsRsn = value if value is not None else base_types.UninitialisedField(self, 'StsRsn', StatusReasonInformation8, True)

	@StsRsn.deleter
	def StsRsn(self):
		del self._StsRsn
		self._StsRsn = base_types.UninitialisedField(self, 'StsRsn', StatusReasonInformation8, True)

	@property
	def UdrtkgId(self):
		return self._UdrtkgId

	@UdrtkgId.setter
	def UdrtkgId(self, value):
		self._UdrtkgId = value if value is not None else base_types.UninitialisedField(self, 'UdrtkgId', Undertaking8, False)

	@UdrtkgId.deleter
	def UdrtkgId(self):
		del self._UdrtkgId
		self._UdrtkgId = base_types.UninitialisedField(self, 'UdrtkgId', Undertaking8, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max2000Text, min=0, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='AdvsgPtyRefNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AmdmntSeqNb', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CnfrmrRefNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InitgPty', type=PartyIdentification43, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NclsdFile', type=Document9, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrgnlMsgDtls', type=OriginalMessage1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptdAmt', type=ReportedAmount1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sts', type=UndertakingStatus3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsCtgy', type=ExternalUndertakingStatusCategory1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsRsn', type=StatusReasonInformation8, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='UdrtkgId', type=Undertaking8, min=0, max=1, mutex_group=None, array=False),
	))