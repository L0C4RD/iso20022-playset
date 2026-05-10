from . import base_types
from .PartyIdentification272 import PartyIdentification272
from .TrueFalseIndicator import TrueFalseIndicator
from .CashAccount40 import CashAccount40
from .Max1025Text import Max1025Text
from .ContentInformationType39 import ContentInformationType39

class CreditTransferContext1(base_types._BaseFieldType):

	__slots__ = ["_WaitForNtfctnBfrEndg", "_SysToNtfy", "_Cdtr", "_CdtrAcct", "_AutomtcNtfctnOfCshMvmnt", "_Dbtr", "_PrtctdCdtrAcct", "_PrtctdDbtrAcct", "_DbtrAcct"]
	@property
	def WaitForNtfctnBfrEndg(self):
		return self._WaitForNtfctnBfrEndg

	@WaitForNtfctnBfrEndg.setter
	def WaitForNtfctnBfrEndg(self, value):
		self._WaitForNtfctnBfrEndg = value if type(value) != auto else self.make_default("WaitForNtfctnBfrEndg")

	@WaitForNtfctnBfrEndg.deleter
	def WaitForNtfctnBfrEndg(self):
		del self._WaitForNtfctnBfrEndg
		self._WaitForNtfctnBfrEndg = None

	@property
	def SysToNtfy(self):
		return self._SysToNtfy

	@SysToNtfy.setter
	def SysToNtfy(self, value):
		self._SysToNtfy = value if type(value) != auto else self.make_default("SysToNtfy")

	@SysToNtfy.deleter
	def SysToNtfy(self):
		del self._SysToNtfy
		self._SysToNtfy = None

	@property
	def Cdtr(self):
		return self._Cdtr

	@Cdtr.setter
	def Cdtr(self, value):
		self._Cdtr = value if type(value) != auto else self.make_default("Cdtr")

	@Cdtr.deleter
	def Cdtr(self):
		del self._Cdtr
		self._Cdtr = None

	@property
	def CdtrAcct(self):
		return self._CdtrAcct

	@CdtrAcct.setter
	def CdtrAcct(self, value):
		self._CdtrAcct = value if type(value) != auto else self.make_default("CdtrAcct")

	@CdtrAcct.deleter
	def CdtrAcct(self):
		del self._CdtrAcct
		self._CdtrAcct = None

	@property
	def AutomtcNtfctnOfCshMvmnt(self):
		return self._AutomtcNtfctnOfCshMvmnt

	@AutomtcNtfctnOfCshMvmnt.setter
	def AutomtcNtfctnOfCshMvmnt(self, value):
		self._AutomtcNtfctnOfCshMvmnt = value if type(value) != auto else self.make_default("AutomtcNtfctnOfCshMvmnt")

	@AutomtcNtfctnOfCshMvmnt.deleter
	def AutomtcNtfctnOfCshMvmnt(self):
		del self._AutomtcNtfctnOfCshMvmnt
		self._AutomtcNtfctnOfCshMvmnt = None

	@property
	def Dbtr(self):
		return self._Dbtr

	@Dbtr.setter
	def Dbtr(self, value):
		self._Dbtr = value if type(value) != auto else self.make_default("Dbtr")

	@Dbtr.deleter
	def Dbtr(self):
		del self._Dbtr
		self._Dbtr = None

	@property
	def PrtctdCdtrAcct(self):
		return self._PrtctdCdtrAcct

	@PrtctdCdtrAcct.setter
	def PrtctdCdtrAcct(self, value):
		self._PrtctdCdtrAcct = value if type(value) != auto else self.make_default("PrtctdCdtrAcct")

	@PrtctdCdtrAcct.deleter
	def PrtctdCdtrAcct(self):
		del self._PrtctdCdtrAcct
		self._PrtctdCdtrAcct = None

	@property
	def PrtctdDbtrAcct(self):
		return self._PrtctdDbtrAcct

	@PrtctdDbtrAcct.setter
	def PrtctdDbtrAcct(self, value):
		self._PrtctdDbtrAcct = value if type(value) != auto else self.make_default("PrtctdDbtrAcct")

	@PrtctdDbtrAcct.deleter
	def PrtctdDbtrAcct(self):
		del self._PrtctdDbtrAcct
		self._PrtctdDbtrAcct = None

	@property
	def DbtrAcct(self):
		return self._DbtrAcct

	@DbtrAcct.setter
	def DbtrAcct(self, value):
		self._DbtrAcct = value if type(value) != auto else self.make_default("DbtrAcct")

	@DbtrAcct.deleter
	def DbtrAcct(self):
		del self._DbtrAcct
		self._DbtrAcct = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='WaitForNtfctnBfrEndg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SysToNtfy', type=Max1025Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cdtr', type=PartyIdentification272, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AutomtcNtfctnOfCshMvmnt', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dbtr', type=PartyIdentification272, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdCdtrAcct', type=ContentInformationType39, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdDbtrAcct', type=ContentInformationType39, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
	))

