import base_types
import VoteInstruction5Code
import VoteInstructionType1
import Max2048Text
import YesNoIndicator
import ResolutionStatus1Code
import Entitlement1Choice
import Max35Text
import VotingRightsThreshold2
import ResolutionType2Code
import ItemDescription2
import VoteType1Code

class Resolution8(base_types._BaseFieldType):

	__slots__ = ["_IssrLabl", "_Desc", "_RghtToWdrwInd", "_ListgGrpRsltnLabl", "_NtifngPtyRcmmndtn", "_Tp", "_VoteTp", "_VoteInstrTp", "_URLAdr", "_Sts", "_Entitlmnt", "_MgmtRcmmndtn", "_VtngRghtsThrshldForApprvl", "_ForInfOnly", "_SubmittdBySctyHldr"]
	@property
	def IssrLabl(self):
		return self._IssrLabl

	@IssrLabl.setter
	def IssrLabl(self, value):
		self._IssrLabl = value if type(value) != auto else self.make_default("IssrLabl")

	@IssrLabl.deleter
	def IssrLabl(self):
		del self._IssrLabl
		self._IssrLabl = None

	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if type(value) != auto else self.make_default("Desc")

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = None

	@property
	def RghtToWdrwInd(self):
		return self._RghtToWdrwInd

	@RghtToWdrwInd.setter
	def RghtToWdrwInd(self, value):
		self._RghtToWdrwInd = value if type(value) != auto else self.make_default("RghtToWdrwInd")

	@RghtToWdrwInd.deleter
	def RghtToWdrwInd(self):
		del self._RghtToWdrwInd
		self._RghtToWdrwInd = None

	@property
	def ListgGrpRsltnLabl(self):
		return self._ListgGrpRsltnLabl

	@ListgGrpRsltnLabl.setter
	def ListgGrpRsltnLabl(self, value):
		self._ListgGrpRsltnLabl = value if type(value) != auto else self.make_default("ListgGrpRsltnLabl")

	@ListgGrpRsltnLabl.deleter
	def ListgGrpRsltnLabl(self):
		del self._ListgGrpRsltnLabl
		self._ListgGrpRsltnLabl = None

	@property
	def NtifngPtyRcmmndtn(self):
		return self._NtifngPtyRcmmndtn

	@NtifngPtyRcmmndtn.setter
	def NtifngPtyRcmmndtn(self, value):
		self._NtifngPtyRcmmndtn = value if type(value) != auto else self.make_default("NtifngPtyRcmmndtn")

	@NtifngPtyRcmmndtn.deleter
	def NtifngPtyRcmmndtn(self):
		del self._NtifngPtyRcmmndtn
		self._NtifngPtyRcmmndtn = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def VoteTp(self):
		return self._VoteTp

	@VoteTp.setter
	def VoteTp(self, value):
		self._VoteTp = value if type(value) != auto else self.make_default("VoteTp")

	@VoteTp.deleter
	def VoteTp(self):
		del self._VoteTp
		self._VoteTp = None

	@property
	def VoteInstrTp(self):
		return self._VoteInstrTp

	@VoteInstrTp.setter
	def VoteInstrTp(self, value):
		self._VoteInstrTp = value if type(value) != auto else self.make_default("VoteInstrTp")

	@VoteInstrTp.deleter
	def VoteInstrTp(self):
		del self._VoteInstrTp
		self._VoteInstrTp = None

	@property
	def URLAdr(self):
		return self._URLAdr

	@URLAdr.setter
	def URLAdr(self, value):
		self._URLAdr = value if type(value) != auto else self.make_default("URLAdr")

	@URLAdr.deleter
	def URLAdr(self):
		del self._URLAdr
		self._URLAdr = None

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

	@property
	def Entitlmnt(self):
		return self._Entitlmnt

	@Entitlmnt.setter
	def Entitlmnt(self, value):
		self._Entitlmnt = value if type(value) != auto else self.make_default("Entitlmnt")

	@Entitlmnt.deleter
	def Entitlmnt(self):
		del self._Entitlmnt
		self._Entitlmnt = None

	@property
	def MgmtRcmmndtn(self):
		return self._MgmtRcmmndtn

	@MgmtRcmmndtn.setter
	def MgmtRcmmndtn(self, value):
		self._MgmtRcmmndtn = value if type(value) != auto else self.make_default("MgmtRcmmndtn")

	@MgmtRcmmndtn.deleter
	def MgmtRcmmndtn(self):
		del self._MgmtRcmmndtn
		self._MgmtRcmmndtn = None

	@property
	def VtngRghtsThrshldForApprvl(self):
		return self._VtngRghtsThrshldForApprvl

	@VtngRghtsThrshldForApprvl.setter
	def VtngRghtsThrshldForApprvl(self, value):
		self._VtngRghtsThrshldForApprvl = value if type(value) != auto else self.make_default("VtngRghtsThrshldForApprvl")

	@VtngRghtsThrshldForApprvl.deleter
	def VtngRghtsThrshldForApprvl(self):
		del self._VtngRghtsThrshldForApprvl
		self._VtngRghtsThrshldForApprvl = None

	@property
	def ForInfOnly(self):
		return self._ForInfOnly

	@ForInfOnly.setter
	def ForInfOnly(self, value):
		self._ForInfOnly = value if type(value) != auto else self.make_default("ForInfOnly")

	@ForInfOnly.deleter
	def ForInfOnly(self):
		del self._ForInfOnly
		self._ForInfOnly = None

	@property
	def SubmittdBySctyHldr(self):
		return self._SubmittdBySctyHldr

	@SubmittdBySctyHldr.setter
	def SubmittdBySctyHldr(self, value):
		self._SubmittdBySctyHldr = value if type(value) != auto else self.make_default("SubmittdBySctyHldr")

	@SubmittdBySctyHldr.deleter
	def SubmittdBySctyHldr(self):
		del self._SubmittdBySctyHldr
		self._SubmittdBySctyHldr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='IssrLabl', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Desc', type=ItemDescription2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RghtToWdrwInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ListgGrpRsltnLabl', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtifngPtyRcmmndtn', type=VoteInstruction5Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=ResolutionType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VoteTp', type=VoteType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VoteInstrTp', type=VoteInstructionType1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='URLAdr', type=Max2048Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sts', type=ResolutionStatus1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Entitlmnt', type=Entitlement1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MgmtRcmmndtn', type=VoteInstruction5Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VtngRghtsThrshldForApprvl', type=VotingRightsThreshold2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ForInfOnly', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubmittdBySctyHldr', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
	))

