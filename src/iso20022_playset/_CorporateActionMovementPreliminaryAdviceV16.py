# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountIdentification70Choice
from . import CorporateAction69
from . import CorporateActionEventReference3
from . import CorporateActionGeneralInformation178
from . import CorporateActionNarrative56
from . import CorporateActionOption232
from . import CorporateActionPreliminaryAdviceType4
from . import CorporateActionReversalReason8
from . import DocumentIdentification31
from . import DocumentIdentification32
from . import DocumentIdentification9
from . import Pagination1
from . import PartyIdentification120Choice
from . import PartyIdentification129Choice
from . import SupplementaryData1

class CorporateActionMovementPreliminaryAdviceV16(base_types._BaseFieldType):

	__slots__ = ["_AcctDtls", "_AddtlInf", "_CorpActnDtls", "_CorpActnGnlInf", "_CorpActnMvmntDtls", "_DrpAgt", "_EvtsLkg", "_InfAgt", "_InstrId", "_Issr", "_IssrAgt", "_MvmntConfId", "_MvmntPrlimryAdvcGnlInf", "_NtfctnId", "_Offerr", "_OthrDocId", "_Pgntn", "_PhysSctiesAgt", "_PngAgt", "_PrvsMvmntPrlimryAdvcId", "_Regar", "_RsellngAgt", "_RvslRsn", "_SlctnAgt", "_SplmtryData", "_SubPngAgt", "_TrfAgt"]
	@property
	def AcctDtls(self):
		return self._AcctDtls

	@AcctDtls.setter
	def AcctDtls(self, value):
		self._AcctDtls = value if value is not None else base_types.UninitialisedField(self, 'AcctDtls', AccountIdentification70Choice, False)

	@AcctDtls.deleter
	def AcctDtls(self):
		del self._AcctDtls
		self._AcctDtls = base_types.UninitialisedField(self, 'AcctDtls', AccountIdentification70Choice, False)

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', CorporateActionNarrative56, False)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', CorporateActionNarrative56, False)

	@property
	def CorpActnDtls(self):
		return self._CorpActnDtls

	@CorpActnDtls.setter
	def CorpActnDtls(self, value):
		self._CorpActnDtls = value if value is not None else base_types.UninitialisedField(self, 'CorpActnDtls', CorporateAction69, False)

	@CorpActnDtls.deleter
	def CorpActnDtls(self):
		del self._CorpActnDtls
		self._CorpActnDtls = base_types.UninitialisedField(self, 'CorpActnDtls', CorporateAction69, False)

	@property
	def CorpActnGnlInf(self):
		return self._CorpActnGnlInf

	@CorpActnGnlInf.setter
	def CorpActnGnlInf(self, value):
		self._CorpActnGnlInf = value if value is not None else base_types.UninitialisedField(self, 'CorpActnGnlInf', CorporateActionGeneralInformation178, False)

	@CorpActnGnlInf.deleter
	def CorpActnGnlInf(self):
		del self._CorpActnGnlInf
		self._CorpActnGnlInf = base_types.UninitialisedField(self, 'CorpActnGnlInf', CorporateActionGeneralInformation178, False)

	@property
	def CorpActnMvmntDtls(self):
		return self._CorpActnMvmntDtls

	@CorpActnMvmntDtls.setter
	def CorpActnMvmntDtls(self, value):
		self._CorpActnMvmntDtls = value if value is not None else base_types.UninitialisedField(self, 'CorpActnMvmntDtls', CorporateActionOption232, True)

	@CorpActnMvmntDtls.deleter
	def CorpActnMvmntDtls(self):
		del self._CorpActnMvmntDtls
		self._CorpActnMvmntDtls = base_types.UninitialisedField(self, 'CorpActnMvmntDtls', CorporateActionOption232, True)

	@property
	def DrpAgt(self):
		return self._DrpAgt

	@DrpAgt.setter
	def DrpAgt(self, value):
		self._DrpAgt = value if value is not None else base_types.UninitialisedField(self, 'DrpAgt', PartyIdentification120Choice, False)

	@DrpAgt.deleter
	def DrpAgt(self):
		del self._DrpAgt
		self._DrpAgt = base_types.UninitialisedField(self, 'DrpAgt', PartyIdentification120Choice, False)

	@property
	def EvtsLkg(self):
		return self._EvtsLkg

	@EvtsLkg.setter
	def EvtsLkg(self, value):
		self._EvtsLkg = value if value is not None else base_types.UninitialisedField(self, 'EvtsLkg', CorporateActionEventReference3, True)

	@EvtsLkg.deleter
	def EvtsLkg(self):
		del self._EvtsLkg
		self._EvtsLkg = base_types.UninitialisedField(self, 'EvtsLkg', CorporateActionEventReference3, True)

	@property
	def InfAgt(self):
		return self._InfAgt

	@InfAgt.setter
	def InfAgt(self, value):
		self._InfAgt = value if value is not None else base_types.UninitialisedField(self, 'InfAgt', PartyIdentification120Choice, False)

	@InfAgt.deleter
	def InfAgt(self):
		del self._InfAgt
		self._InfAgt = base_types.UninitialisedField(self, 'InfAgt', PartyIdentification120Choice, False)

	@property
	def InstrId(self):
		return self._InstrId

	@InstrId.setter
	def InstrId(self, value):
		self._InstrId = value if value is not None else base_types.UninitialisedField(self, 'InstrId', DocumentIdentification9, False)

	@InstrId.deleter
	def InstrId(self):
		del self._InstrId
		self._InstrId = base_types.UninitialisedField(self, 'InstrId', DocumentIdentification9, False)

	@property
	def Issr(self):
		return self._Issr

	@Issr.setter
	def Issr(self, value):
		self._Issr = value if value is not None else base_types.UninitialisedField(self, 'Issr', PartyIdentification129Choice, False)

	@Issr.deleter
	def Issr(self):
		del self._Issr
		self._Issr = base_types.UninitialisedField(self, 'Issr', PartyIdentification129Choice, False)

	@property
	def IssrAgt(self):
		return self._IssrAgt

	@IssrAgt.setter
	def IssrAgt(self, value):
		self._IssrAgt = value if value is not None else base_types.UninitialisedField(self, 'IssrAgt', PartyIdentification129Choice, True)

	@IssrAgt.deleter
	def IssrAgt(self):
		del self._IssrAgt
		self._IssrAgt = base_types.UninitialisedField(self, 'IssrAgt', PartyIdentification129Choice, True)

	@property
	def MvmntConfId(self):
		return self._MvmntConfId

	@MvmntConfId.setter
	def MvmntConfId(self, value):
		self._MvmntConfId = value if value is not None else base_types.UninitialisedField(self, 'MvmntConfId', DocumentIdentification31, False)

	@MvmntConfId.deleter
	def MvmntConfId(self):
		del self._MvmntConfId
		self._MvmntConfId = base_types.UninitialisedField(self, 'MvmntConfId', DocumentIdentification31, False)

	@property
	def MvmntPrlimryAdvcGnlInf(self):
		return self._MvmntPrlimryAdvcGnlInf

	@MvmntPrlimryAdvcGnlInf.setter
	def MvmntPrlimryAdvcGnlInf(self, value):
		self._MvmntPrlimryAdvcGnlInf = value if value is not None else base_types.UninitialisedField(self, 'MvmntPrlimryAdvcGnlInf', CorporateActionPreliminaryAdviceType4, False)

	@MvmntPrlimryAdvcGnlInf.deleter
	def MvmntPrlimryAdvcGnlInf(self):
		del self._MvmntPrlimryAdvcGnlInf
		self._MvmntPrlimryAdvcGnlInf = base_types.UninitialisedField(self, 'MvmntPrlimryAdvcGnlInf', CorporateActionPreliminaryAdviceType4, False)

	@property
	def NtfctnId(self):
		return self._NtfctnId

	@NtfctnId.setter
	def NtfctnId(self, value):
		self._NtfctnId = value if value is not None else base_types.UninitialisedField(self, 'NtfctnId', DocumentIdentification31, False)

	@NtfctnId.deleter
	def NtfctnId(self):
		del self._NtfctnId
		self._NtfctnId = base_types.UninitialisedField(self, 'NtfctnId', DocumentIdentification31, False)

	@property
	def Offerr(self):
		return self._Offerr

	@Offerr.setter
	def Offerr(self, value):
		self._Offerr = value if value is not None else base_types.UninitialisedField(self, 'Offerr', PartyIdentification129Choice, True)

	@Offerr.deleter
	def Offerr(self):
		del self._Offerr
		self._Offerr = base_types.UninitialisedField(self, 'Offerr', PartyIdentification129Choice, True)

	@property
	def OthrDocId(self):
		return self._OthrDocId

	@OthrDocId.setter
	def OthrDocId(self, value):
		self._OthrDocId = value if value is not None else base_types.UninitialisedField(self, 'OthrDocId', DocumentIdentification32, True)

	@OthrDocId.deleter
	def OthrDocId(self):
		del self._OthrDocId
		self._OthrDocId = base_types.UninitialisedField(self, 'OthrDocId', DocumentIdentification32, True)

	@property
	def Pgntn(self):
		return self._Pgntn

	@Pgntn.setter
	def Pgntn(self, value):
		self._Pgntn = value if value is not None else base_types.UninitialisedField(self, 'Pgntn', Pagination1, False)

	@Pgntn.deleter
	def Pgntn(self):
		del self._Pgntn
		self._Pgntn = base_types.UninitialisedField(self, 'Pgntn', Pagination1, False)

	@property
	def PhysSctiesAgt(self):
		return self._PhysSctiesAgt

	@PhysSctiesAgt.setter
	def PhysSctiesAgt(self, value):
		self._PhysSctiesAgt = value if value is not None else base_types.UninitialisedField(self, 'PhysSctiesAgt', PartyIdentification120Choice, False)

	@PhysSctiesAgt.deleter
	def PhysSctiesAgt(self):
		del self._PhysSctiesAgt
		self._PhysSctiesAgt = base_types.UninitialisedField(self, 'PhysSctiesAgt', PartyIdentification120Choice, False)

	@property
	def PngAgt(self):
		return self._PngAgt

	@PngAgt.setter
	def PngAgt(self, value):
		self._PngAgt = value if value is not None else base_types.UninitialisedField(self, 'PngAgt', PartyIdentification120Choice, True)

	@PngAgt.deleter
	def PngAgt(self):
		del self._PngAgt
		self._PngAgt = base_types.UninitialisedField(self, 'PngAgt', PartyIdentification120Choice, True)

	@property
	def PrvsMvmntPrlimryAdvcId(self):
		return self._PrvsMvmntPrlimryAdvcId

	@PrvsMvmntPrlimryAdvcId.setter
	def PrvsMvmntPrlimryAdvcId(self, value):
		self._PrvsMvmntPrlimryAdvcId = value if value is not None else base_types.UninitialisedField(self, 'PrvsMvmntPrlimryAdvcId', DocumentIdentification31, False)

	@PrvsMvmntPrlimryAdvcId.deleter
	def PrvsMvmntPrlimryAdvcId(self):
		del self._PrvsMvmntPrlimryAdvcId
		self._PrvsMvmntPrlimryAdvcId = base_types.UninitialisedField(self, 'PrvsMvmntPrlimryAdvcId', DocumentIdentification31, False)

	@property
	def Regar(self):
		return self._Regar

	@Regar.setter
	def Regar(self, value):
		self._Regar = value if value is not None else base_types.UninitialisedField(self, 'Regar', PartyIdentification120Choice, False)

	@Regar.deleter
	def Regar(self):
		del self._Regar
		self._Regar = base_types.UninitialisedField(self, 'Regar', PartyIdentification120Choice, False)

	@property
	def RsellngAgt(self):
		return self._RsellngAgt

	@RsellngAgt.setter
	def RsellngAgt(self, value):
		self._RsellngAgt = value if value is not None else base_types.UninitialisedField(self, 'RsellngAgt', PartyIdentification120Choice, True)

	@RsellngAgt.deleter
	def RsellngAgt(self):
		del self._RsellngAgt
		self._RsellngAgt = base_types.UninitialisedField(self, 'RsellngAgt', PartyIdentification120Choice, True)

	@property
	def RvslRsn(self):
		return self._RvslRsn

	@RvslRsn.setter
	def RvslRsn(self, value):
		self._RvslRsn = value if value is not None else base_types.UninitialisedField(self, 'RvslRsn', CorporateActionReversalReason8, False)

	@RvslRsn.deleter
	def RvslRsn(self):
		del self._RvslRsn
		self._RvslRsn = base_types.UninitialisedField(self, 'RvslRsn', CorporateActionReversalReason8, False)

	@property
	def SlctnAgt(self):
		return self._SlctnAgt

	@SlctnAgt.setter
	def SlctnAgt(self, value):
		self._SlctnAgt = value if value is not None else base_types.UninitialisedField(self, 'SlctnAgt', PartyIdentification120Choice, True)

	@SlctnAgt.deleter
	def SlctnAgt(self):
		del self._SlctnAgt
		self._SlctnAgt = base_types.UninitialisedField(self, 'SlctnAgt', PartyIdentification120Choice, True)

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
	def SubPngAgt(self):
		return self._SubPngAgt

	@SubPngAgt.setter
	def SubPngAgt(self, value):
		self._SubPngAgt = value if value is not None else base_types.UninitialisedField(self, 'SubPngAgt', PartyIdentification120Choice, True)

	@SubPngAgt.deleter
	def SubPngAgt(self):
		del self._SubPngAgt
		self._SubPngAgt = base_types.UninitialisedField(self, 'SubPngAgt', PartyIdentification120Choice, True)

	@property
	def TrfAgt(self):
		return self._TrfAgt

	@TrfAgt.setter
	def TrfAgt(self, value):
		self._TrfAgt = value if value is not None else base_types.UninitialisedField(self, 'TrfAgt', PartyIdentification129Choice, False)

	@TrfAgt.deleter
	def TrfAgt(self):
		del self._TrfAgt
		self._TrfAgt = base_types.UninitialisedField(self, 'TrfAgt', PartyIdentification129Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctDtls', type=AccountIdentification70Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=CorporateActionNarrative56, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnDtls', type=CorporateAction69, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnGnlInf', type=CorporateActionGeneralInformation178, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnMvmntDtls', type=CorporateActionOption232, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DrpAgt', type=PartyIdentification120Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtsLkg', type=CorporateActionEventReference3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InfAgt', type=PartyIdentification120Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrId', type=DocumentIdentification9, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Issr', type=PartyIdentification129Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssrAgt', type=PartyIdentification129Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MvmntConfId', type=DocumentIdentification31, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MvmntPrlimryAdvcGnlInf', type=CorporateActionPreliminaryAdviceType4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtfctnId', type=DocumentIdentification31, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Offerr', type=PartyIdentification129Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OthrDocId', type=DocumentIdentification32, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Pgntn', type=Pagination1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PhysSctiesAgt', type=PartyIdentification120Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PngAgt', type=PartyIdentification120Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrvsMvmntPrlimryAdvcId', type=DocumentIdentification31, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Regar', type=PartyIdentification120Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsellngAgt', type=PartyIdentification120Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RvslRsn', type=CorporateActionReversalReason8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SlctnAgt', type=PartyIdentification120Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SubPngAgt', type=PartyIdentification120Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TrfAgt', type=PartyIdentification129Choice, min=0, max=1, mutex_group=None, array=False),
	))