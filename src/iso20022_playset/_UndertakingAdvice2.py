# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Document9
from . import Max2000Text
from . import Max35Text
from . import PartyIdentification43
from . import PresentationMedium1Code
from . import UndertakingIssuanceMessage

class UndertakingAdvice2(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_ApplcntRefNb", "_NclsdFile", "_Oblgr", "_OrgnlIssdMdm", "_UdrtkgIssncMsg"]
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
	def ApplcntRefNb(self):
		return self._ApplcntRefNb

	@ApplcntRefNb.setter
	def ApplcntRefNb(self, value):
		self._ApplcntRefNb = value if value is not None else base_types.UninitialisedField(self, 'ApplcntRefNb', Max35Text, False)

	@ApplcntRefNb.deleter
	def ApplcntRefNb(self):
		del self._ApplcntRefNb
		self._ApplcntRefNb = base_types.UninitialisedField(self, 'ApplcntRefNb', Max35Text, False)

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
	def Oblgr(self):
		return self._Oblgr

	@Oblgr.setter
	def Oblgr(self, value):
		self._Oblgr = value if value is not None else base_types.UninitialisedField(self, 'Oblgr', PartyIdentification43, False)

	@Oblgr.deleter
	def Oblgr(self):
		del self._Oblgr
		self._Oblgr = base_types.UninitialisedField(self, 'Oblgr', PartyIdentification43, False)

	@property
	def OrgnlIssdMdm(self):
		return self._OrgnlIssdMdm

	@OrgnlIssdMdm.setter
	def OrgnlIssdMdm(self, value):
		self._OrgnlIssdMdm = value if value is not None else base_types.UninitialisedField(self, 'OrgnlIssdMdm', PresentationMedium1Code, False)

	@OrgnlIssdMdm.deleter
	def OrgnlIssdMdm(self):
		del self._OrgnlIssdMdm
		self._OrgnlIssdMdm = base_types.UninitialisedField(self, 'OrgnlIssdMdm', PresentationMedium1Code, False)

	@property
	def UdrtkgIssncMsg(self):
		return self._UdrtkgIssncMsg

	@UdrtkgIssncMsg.setter
	def UdrtkgIssncMsg(self, value):
		self._UdrtkgIssncMsg = value if value is not None else base_types.UninitialisedField(self, 'UdrtkgIssncMsg', UndertakingIssuanceMessage, False)

	@UdrtkgIssncMsg.deleter
	def UdrtkgIssncMsg(self):
		del self._UdrtkgIssncMsg
		self._UdrtkgIssncMsg = base_types.UninitialisedField(self, 'UdrtkgIssncMsg', UndertakingIssuanceMessage, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max2000Text, min=0, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='ApplcntRefNb', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NclsdFile', type=Document9, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Oblgr', type=PartyIdentification43, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlIssdMdm', type=PresentationMedium1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UdrtkgIssncMsg', type=UndertakingIssuanceMessage, min=1, max=1, mutex_group=None, array=False),
	))