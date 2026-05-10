from . import base_types
from ._UndertakingIssuanceMessage import UndertakingIssuanceMessage
from ._PresentationMedium1Code import PresentationMedium1Code
from ._Document9 import Document9
from ._Max35Text import Max35Text
from ._Max2000Text import Max2000Text
from ._PartyIdentification43 import PartyIdentification43

class UndertakingAdvice2(base_types._BaseFieldType):

	__slots__ = ["_OrgnlIssdMdm", "_ApplcntRefNb", "_Oblgr", "_NclsdFile", "_UdrtkgIssncMsg", "_AddtlInf"]
	@property
	def OrgnlIssdMdm(self):
		return self._OrgnlIssdMdm

	@OrgnlIssdMdm.setter
	def OrgnlIssdMdm(self, value):
		self._OrgnlIssdMdm = value if type(value) != base_types.auto else self.make_default("OrgnlIssdMdm")

	@OrgnlIssdMdm.deleter
	def OrgnlIssdMdm(self):
		del self._OrgnlIssdMdm
		self._OrgnlIssdMdm = None

	@property
	def ApplcntRefNb(self):
		return self._ApplcntRefNb

	@ApplcntRefNb.setter
	def ApplcntRefNb(self, value):
		self._ApplcntRefNb = value if type(value) != base_types.auto else self.make_default("ApplcntRefNb")

	@ApplcntRefNb.deleter
	def ApplcntRefNb(self):
		del self._ApplcntRefNb
		self._ApplcntRefNb = None

	@property
	def Oblgr(self):
		return self._Oblgr

	@Oblgr.setter
	def Oblgr(self, value):
		self._Oblgr = value if type(value) != base_types.auto else self.make_default("Oblgr")

	@Oblgr.deleter
	def Oblgr(self):
		del self._Oblgr
		self._Oblgr = None

	@property
	def NclsdFile(self):
		return self._NclsdFile

	@NclsdFile.setter
	def NclsdFile(self, value):
		self._NclsdFile = value if type(value) != base_types.auto else self.make_default("NclsdFile")

	@NclsdFile.deleter
	def NclsdFile(self):
		del self._NclsdFile
		self._NclsdFile = None

	@property
	def UdrtkgIssncMsg(self):
		return self._UdrtkgIssncMsg

	@UdrtkgIssncMsg.setter
	def UdrtkgIssncMsg(self, value):
		self._UdrtkgIssncMsg = value if type(value) != base_types.auto else self.make_default("UdrtkgIssncMsg")

	@UdrtkgIssncMsg.deleter
	def UdrtkgIssncMsg(self):
		del self._UdrtkgIssncMsg
		self._UdrtkgIssncMsg = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgnlIssdMdm', type=PresentationMedium1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ApplcntRefNb', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Oblgr', type=PartyIdentification43, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NclsdFile', type=Document9, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='UdrtkgIssncMsg', type=UndertakingIssuanceMessage, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=Max2000Text, min=0, max=5, mutex_group=None, array=True),
	))

