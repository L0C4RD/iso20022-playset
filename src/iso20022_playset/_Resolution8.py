# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Entitlement1Choice
from . import ItemDescription2
from . import Max2048Text
from . import Max35Text
from . import ResolutionStatus1Code
from . import ResolutionType2Code
from . import VoteInstruction5Code
from . import VoteInstructionType1
from . import VoteType1Code
from . import VotingRightsThreshold2
from . import YesNoIndicator

class Resolution8(base_types._BaseFieldType):

	__slots__ = ["_Desc", "_Entitlmnt", "_ForInfOnly", "_IssrLabl", "_ListgGrpRsltnLabl", "_MgmtRcmmndtn", "_NtifngPtyRcmmndtn", "_RghtToWdrwInd", "_Sts", "_SubmittdBySctyHldr", "_Tp", "_URLAdr", "_VoteInstrTp", "_VoteTp", "_VtngRghtsThrshldForApprvl"]
	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if value is not None else base_types.UninitialisedField(self, 'Desc', ItemDescription2, True)

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = base_types.UninitialisedField(self, 'Desc', ItemDescription2, True)

	@property
	def Entitlmnt(self):
		return self._Entitlmnt

	@Entitlmnt.setter
	def Entitlmnt(self, value):
		self._Entitlmnt = value if value is not None else base_types.UninitialisedField(self, 'Entitlmnt', Entitlement1Choice, False)

	@Entitlmnt.deleter
	def Entitlmnt(self):
		del self._Entitlmnt
		self._Entitlmnt = base_types.UninitialisedField(self, 'Entitlmnt', Entitlement1Choice, False)

	@property
	def ForInfOnly(self):
		return self._ForInfOnly

	@ForInfOnly.setter
	def ForInfOnly(self, value):
		self._ForInfOnly = value if value is not None else base_types.UninitialisedField(self, 'ForInfOnly', YesNoIndicator, False)

	@ForInfOnly.deleter
	def ForInfOnly(self):
		del self._ForInfOnly
		self._ForInfOnly = base_types.UninitialisedField(self, 'ForInfOnly', YesNoIndicator, False)

	@property
	def IssrLabl(self):
		return self._IssrLabl

	@IssrLabl.setter
	def IssrLabl(self, value):
		self._IssrLabl = value if value is not None else base_types.UninitialisedField(self, 'IssrLabl', Max35Text, False)

	@IssrLabl.deleter
	def IssrLabl(self):
		del self._IssrLabl
		self._IssrLabl = base_types.UninitialisedField(self, 'IssrLabl', Max35Text, False)

	@property
	def ListgGrpRsltnLabl(self):
		return self._ListgGrpRsltnLabl

	@ListgGrpRsltnLabl.setter
	def ListgGrpRsltnLabl(self, value):
		self._ListgGrpRsltnLabl = value if value is not None else base_types.UninitialisedField(self, 'ListgGrpRsltnLabl', Max35Text, False)

	@ListgGrpRsltnLabl.deleter
	def ListgGrpRsltnLabl(self):
		del self._ListgGrpRsltnLabl
		self._ListgGrpRsltnLabl = base_types.UninitialisedField(self, 'ListgGrpRsltnLabl', Max35Text, False)

	@property
	def MgmtRcmmndtn(self):
		return self._MgmtRcmmndtn

	@MgmtRcmmndtn.setter
	def MgmtRcmmndtn(self, value):
		self._MgmtRcmmndtn = value if value is not None else base_types.UninitialisedField(self, 'MgmtRcmmndtn', VoteInstruction5Code, False)

	@MgmtRcmmndtn.deleter
	def MgmtRcmmndtn(self):
		del self._MgmtRcmmndtn
		self._MgmtRcmmndtn = base_types.UninitialisedField(self, 'MgmtRcmmndtn', VoteInstruction5Code, False)

	@property
	def NtifngPtyRcmmndtn(self):
		return self._NtifngPtyRcmmndtn

	@NtifngPtyRcmmndtn.setter
	def NtifngPtyRcmmndtn(self, value):
		self._NtifngPtyRcmmndtn = value if value is not None else base_types.UninitialisedField(self, 'NtifngPtyRcmmndtn', VoteInstruction5Code, False)

	@NtifngPtyRcmmndtn.deleter
	def NtifngPtyRcmmndtn(self):
		del self._NtifngPtyRcmmndtn
		self._NtifngPtyRcmmndtn = base_types.UninitialisedField(self, 'NtifngPtyRcmmndtn', VoteInstruction5Code, False)

	@property
	def RghtToWdrwInd(self):
		return self._RghtToWdrwInd

	@RghtToWdrwInd.setter
	def RghtToWdrwInd(self, value):
		self._RghtToWdrwInd = value if value is not None else base_types.UninitialisedField(self, 'RghtToWdrwInd', YesNoIndicator, False)

	@RghtToWdrwInd.deleter
	def RghtToWdrwInd(self):
		del self._RghtToWdrwInd
		self._RghtToWdrwInd = base_types.UninitialisedField(self, 'RghtToWdrwInd', YesNoIndicator, False)

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if value is not None else base_types.UninitialisedField(self, 'Sts', ResolutionStatus1Code, False)

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = base_types.UninitialisedField(self, 'Sts', ResolutionStatus1Code, False)

	@property
	def SubmittdBySctyHldr(self):
		return self._SubmittdBySctyHldr

	@SubmittdBySctyHldr.setter
	def SubmittdBySctyHldr(self, value):
		self._SubmittdBySctyHldr = value if value is not None else base_types.UninitialisedField(self, 'SubmittdBySctyHldr', YesNoIndicator, False)

	@SubmittdBySctyHldr.deleter
	def SubmittdBySctyHldr(self):
		del self._SubmittdBySctyHldr
		self._SubmittdBySctyHldr = base_types.UninitialisedField(self, 'SubmittdBySctyHldr', YesNoIndicator, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', ResolutionType2Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', ResolutionType2Code, False)

	@property
	def URLAdr(self):
		return self._URLAdr

	@URLAdr.setter
	def URLAdr(self, value):
		self._URLAdr = value if value is not None else base_types.UninitialisedField(self, 'URLAdr', Max2048Text, False)

	@URLAdr.deleter
	def URLAdr(self):
		del self._URLAdr
		self._URLAdr = base_types.UninitialisedField(self, 'URLAdr', Max2048Text, False)

	@property
	def VoteInstrTp(self):
		return self._VoteInstrTp

	@VoteInstrTp.setter
	def VoteInstrTp(self, value):
		self._VoteInstrTp = value if value is not None else base_types.UninitialisedField(self, 'VoteInstrTp', VoteInstructionType1, True)

	@VoteInstrTp.deleter
	def VoteInstrTp(self):
		del self._VoteInstrTp
		self._VoteInstrTp = base_types.UninitialisedField(self, 'VoteInstrTp', VoteInstructionType1, True)

	@property
	def VoteTp(self):
		return self._VoteTp

	@VoteTp.setter
	def VoteTp(self, value):
		self._VoteTp = value if value is not None else base_types.UninitialisedField(self, 'VoteTp', VoteType1Code, False)

	@VoteTp.deleter
	def VoteTp(self):
		del self._VoteTp
		self._VoteTp = base_types.UninitialisedField(self, 'VoteTp', VoteType1Code, False)

	@property
	def VtngRghtsThrshldForApprvl(self):
		return self._VtngRghtsThrshldForApprvl

	@VtngRghtsThrshldForApprvl.setter
	def VtngRghtsThrshldForApprvl(self, value):
		self._VtngRghtsThrshldForApprvl = value if value is not None else base_types.UninitialisedField(self, 'VtngRghtsThrshldForApprvl', VotingRightsThreshold2, True)

	@VtngRghtsThrshldForApprvl.deleter
	def VtngRghtsThrshldForApprvl(self):
		del self._VtngRghtsThrshldForApprvl
		self._VtngRghtsThrshldForApprvl = base_types.UninitialisedField(self, 'VtngRghtsThrshldForApprvl', VotingRightsThreshold2, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Desc', type=ItemDescription2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Entitlmnt', type=Entitlement1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ForInfOnly', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssrLabl', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ListgGrpRsltnLabl', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MgmtRcmmndtn', type=VoteInstruction5Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtifngPtyRcmmndtn', type=VoteInstruction5Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RghtToWdrwInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sts', type=ResolutionStatus1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubmittdBySctyHldr', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=ResolutionType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='URLAdr', type=Max2048Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VoteInstrTp', type=VoteInstructionType1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='VoteTp', type=VoteType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VtngRghtsThrshldForApprvl', type=VotingRightsThreshold2, min=0, max=None, mutex_group=None, array=True),
	))