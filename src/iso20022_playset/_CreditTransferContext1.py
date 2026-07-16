# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CashAccount40
from . import ContentInformationType39
from . import Max1025Text
from . import PartyIdentification272
from . import TrueFalseIndicator

class CreditTransferContext1(base_types._BaseFieldType):

	__slots__ = ["_AutomtcNtfctnOfCshMvmnt", "_Cdtr", "_CdtrAcct", "_Dbtr", "_DbtrAcct", "_PrtctdCdtrAcct", "_PrtctdDbtrAcct", "_SysToNtfy", "_WaitForNtfctnBfrEndg"]
	@property
	def AutomtcNtfctnOfCshMvmnt(self):
		return self._AutomtcNtfctnOfCshMvmnt

	@AutomtcNtfctnOfCshMvmnt.setter
	def AutomtcNtfctnOfCshMvmnt(self, value):
		self._AutomtcNtfctnOfCshMvmnt = value if value is not None else base_types.UninitialisedField(self, 'AutomtcNtfctnOfCshMvmnt', TrueFalseIndicator, False)

	@AutomtcNtfctnOfCshMvmnt.deleter
	def AutomtcNtfctnOfCshMvmnt(self):
		del self._AutomtcNtfctnOfCshMvmnt
		self._AutomtcNtfctnOfCshMvmnt = base_types.UninitialisedField(self, 'AutomtcNtfctnOfCshMvmnt', TrueFalseIndicator, False)

	@property
	def Cdtr(self):
		return self._Cdtr

	@Cdtr.setter
	def Cdtr(self, value):
		self._Cdtr = value if value is not None else base_types.UninitialisedField(self, 'Cdtr', PartyIdentification272, False)

	@Cdtr.deleter
	def Cdtr(self):
		del self._Cdtr
		self._Cdtr = base_types.UninitialisedField(self, 'Cdtr', PartyIdentification272, False)

	@property
	def CdtrAcct(self):
		return self._CdtrAcct

	@CdtrAcct.setter
	def CdtrAcct(self, value):
		self._CdtrAcct = value if value is not None else base_types.UninitialisedField(self, 'CdtrAcct', CashAccount40, False)

	@CdtrAcct.deleter
	def CdtrAcct(self):
		del self._CdtrAcct
		self._CdtrAcct = base_types.UninitialisedField(self, 'CdtrAcct', CashAccount40, False)

	@property
	def Dbtr(self):
		return self._Dbtr

	@Dbtr.setter
	def Dbtr(self, value):
		self._Dbtr = value if value is not None else base_types.UninitialisedField(self, 'Dbtr', PartyIdentification272, False)

	@Dbtr.deleter
	def Dbtr(self):
		del self._Dbtr
		self._Dbtr = base_types.UninitialisedField(self, 'Dbtr', PartyIdentification272, False)

	@property
	def DbtrAcct(self):
		return self._DbtrAcct

	@DbtrAcct.setter
	def DbtrAcct(self, value):
		self._DbtrAcct = value if value is not None else base_types.UninitialisedField(self, 'DbtrAcct', CashAccount40, False)

	@DbtrAcct.deleter
	def DbtrAcct(self):
		del self._DbtrAcct
		self._DbtrAcct = base_types.UninitialisedField(self, 'DbtrAcct', CashAccount40, False)

	@property
	def PrtctdCdtrAcct(self):
		return self._PrtctdCdtrAcct

	@PrtctdCdtrAcct.setter
	def PrtctdCdtrAcct(self, value):
		self._PrtctdCdtrAcct = value if value is not None else base_types.UninitialisedField(self, 'PrtctdCdtrAcct', ContentInformationType39, False)

	@PrtctdCdtrAcct.deleter
	def PrtctdCdtrAcct(self):
		del self._PrtctdCdtrAcct
		self._PrtctdCdtrAcct = base_types.UninitialisedField(self, 'PrtctdCdtrAcct', ContentInformationType39, False)

	@property
	def PrtctdDbtrAcct(self):
		return self._PrtctdDbtrAcct

	@PrtctdDbtrAcct.setter
	def PrtctdDbtrAcct(self, value):
		self._PrtctdDbtrAcct = value if value is not None else base_types.UninitialisedField(self, 'PrtctdDbtrAcct', ContentInformationType39, False)

	@PrtctdDbtrAcct.deleter
	def PrtctdDbtrAcct(self):
		del self._PrtctdDbtrAcct
		self._PrtctdDbtrAcct = base_types.UninitialisedField(self, 'PrtctdDbtrAcct', ContentInformationType39, False)

	@property
	def SysToNtfy(self):
		return self._SysToNtfy

	@SysToNtfy.setter
	def SysToNtfy(self, value):
		self._SysToNtfy = value if value is not None else base_types.UninitialisedField(self, 'SysToNtfy', Max1025Text, False)

	@SysToNtfy.deleter
	def SysToNtfy(self):
		del self._SysToNtfy
		self._SysToNtfy = base_types.UninitialisedField(self, 'SysToNtfy', Max1025Text, False)

	@property
	def WaitForNtfctnBfrEndg(self):
		return self._WaitForNtfctnBfrEndg

	@WaitForNtfctnBfrEndg.setter
	def WaitForNtfctnBfrEndg(self, value):
		self._WaitForNtfctnBfrEndg = value if value is not None else base_types.UninitialisedField(self, 'WaitForNtfctnBfrEndg', TrueFalseIndicator, False)

	@WaitForNtfctnBfrEndg.deleter
	def WaitForNtfctnBfrEndg(self):
		del self._WaitForNtfctnBfrEndg
		self._WaitForNtfctnBfrEndg = base_types.UninitialisedField(self, 'WaitForNtfctnBfrEndg', TrueFalseIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AutomtcNtfctnOfCshMvmnt', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cdtr', type=PartyIdentification272, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dbtr', type=PartyIdentification272, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdCdtrAcct', type=ContentInformationType39, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdDbtrAcct', type=ContentInformationType39, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SysToNtfy', type=Max1025Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WaitForNtfctnBfrEndg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
	))