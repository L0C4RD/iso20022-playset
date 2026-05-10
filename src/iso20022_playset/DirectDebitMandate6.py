import base_types
import Max35Text
import PartyIdentification113
import BranchData
import FinancialInstitutionIdentification10
import AccountIdentificationAndName5

class DirectDebitMandate6(base_types._BaseFieldType):

	__slots__ = ["_RegnId", "_DbtrAgt", "_CdtrAgtBrnch", "_CdtrAgt", "_Dbtr", "_DbtrAgtBrnch", "_Cdtr", "_DbtrTaxIdNb", "_DbtrNtlRegnNb", "_DbtrAcct", "_MndtId"]
	@property
	def RegnId(self):
		return self._RegnId

	@RegnId.setter
	def RegnId(self, value):
		self._RegnId = value if type(value) != auto else self.make_default("RegnId")

	@RegnId.deleter
	def RegnId(self):
		del self._RegnId
		self._RegnId = None

	@property
	def DbtrAgt(self):
		return self._DbtrAgt

	@DbtrAgt.setter
	def DbtrAgt(self, value):
		self._DbtrAgt = value if type(value) != auto else self.make_default("DbtrAgt")

	@DbtrAgt.deleter
	def DbtrAgt(self):
		del self._DbtrAgt
		self._DbtrAgt = None

	@property
	def CdtrAgtBrnch(self):
		return self._CdtrAgtBrnch

	@CdtrAgtBrnch.setter
	def CdtrAgtBrnch(self, value):
		self._CdtrAgtBrnch = value if type(value) != auto else self.make_default("CdtrAgtBrnch")

	@CdtrAgtBrnch.deleter
	def CdtrAgtBrnch(self):
		del self._CdtrAgtBrnch
		self._CdtrAgtBrnch = None

	@property
	def CdtrAgt(self):
		return self._CdtrAgt

	@CdtrAgt.setter
	def CdtrAgt(self, value):
		self._CdtrAgt = value if type(value) != auto else self.make_default("CdtrAgt")

	@CdtrAgt.deleter
	def CdtrAgt(self):
		del self._CdtrAgt
		self._CdtrAgt = None

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
	def DbtrAgtBrnch(self):
		return self._DbtrAgtBrnch

	@DbtrAgtBrnch.setter
	def DbtrAgtBrnch(self, value):
		self._DbtrAgtBrnch = value if type(value) != auto else self.make_default("DbtrAgtBrnch")

	@DbtrAgtBrnch.deleter
	def DbtrAgtBrnch(self):
		del self._DbtrAgtBrnch
		self._DbtrAgtBrnch = None

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
	def DbtrTaxIdNb(self):
		return self._DbtrTaxIdNb

	@DbtrTaxIdNb.setter
	def DbtrTaxIdNb(self, value):
		self._DbtrTaxIdNb = value if type(value) != auto else self.make_default("DbtrTaxIdNb")

	@DbtrTaxIdNb.deleter
	def DbtrTaxIdNb(self):
		del self._DbtrTaxIdNb
		self._DbtrTaxIdNb = None

	@property
	def DbtrNtlRegnNb(self):
		return self._DbtrNtlRegnNb

	@DbtrNtlRegnNb.setter
	def DbtrNtlRegnNb(self, value):
		self._DbtrNtlRegnNb = value if type(value) != auto else self.make_default("DbtrNtlRegnNb")

	@DbtrNtlRegnNb.deleter
	def DbtrNtlRegnNb(self):
		del self._DbtrNtlRegnNb
		self._DbtrNtlRegnNb = None

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

	@property
	def MndtId(self):
		return self._MndtId

	@MndtId.setter
	def MndtId(self, value):
		self._MndtId = value if type(value) != auto else self.make_default("MndtId")

	@MndtId.deleter
	def MndtId(self):
		del self._MndtId
		self._MndtId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RegnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrAgt', type=FinancialInstitutionIdentification10, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrAgtBrnch', type=BranchData, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrAgt', type=FinancialInstitutionIdentification10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dbtr', type=PartyIdentification113, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrAgtBrnch', type=BranchData, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cdtr', type=PartyIdentification113, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrTaxIdNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrNtlRegnNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrAcct', type=AccountIdentificationAndName5, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MndtId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

