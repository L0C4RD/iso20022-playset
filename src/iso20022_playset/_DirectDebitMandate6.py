# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountIdentificationAndName5
from . import BranchData
from . import FinancialInstitutionIdentification10
from . import Max35Text
from . import PartyIdentification113

class DirectDebitMandate6(base_types._BaseFieldType):

	__slots__ = ["_Cdtr", "_CdtrAgt", "_CdtrAgtBrnch", "_Dbtr", "_DbtrAcct", "_DbtrAgt", "_DbtrAgtBrnch", "_DbtrNtlRegnNb", "_DbtrTaxIdNb", "_MndtId", "_RegnId"]
	@property
	def Cdtr(self):
		return self._Cdtr

	@Cdtr.setter
	def Cdtr(self, value):
		self._Cdtr = value if value is not None else base_types.UninitialisedField(self, 'Cdtr', PartyIdentification113, False)

	@Cdtr.deleter
	def Cdtr(self):
		del self._Cdtr
		self._Cdtr = base_types.UninitialisedField(self, 'Cdtr', PartyIdentification113, False)

	@property
	def CdtrAgt(self):
		return self._CdtrAgt

	@CdtrAgt.setter
	def CdtrAgt(self, value):
		self._CdtrAgt = value if value is not None else base_types.UninitialisedField(self, 'CdtrAgt', FinancialInstitutionIdentification10, False)

	@CdtrAgt.deleter
	def CdtrAgt(self):
		del self._CdtrAgt
		self._CdtrAgt = base_types.UninitialisedField(self, 'CdtrAgt', FinancialInstitutionIdentification10, False)

	@property
	def CdtrAgtBrnch(self):
		return self._CdtrAgtBrnch

	@CdtrAgtBrnch.setter
	def CdtrAgtBrnch(self, value):
		self._CdtrAgtBrnch = value if value is not None else base_types.UninitialisedField(self, 'CdtrAgtBrnch', BranchData, False)

	@CdtrAgtBrnch.deleter
	def CdtrAgtBrnch(self):
		del self._CdtrAgtBrnch
		self._CdtrAgtBrnch = base_types.UninitialisedField(self, 'CdtrAgtBrnch', BranchData, False)

	@property
	def Dbtr(self):
		return self._Dbtr

	@Dbtr.setter
	def Dbtr(self, value):
		self._Dbtr = value if value is not None else base_types.UninitialisedField(self, 'Dbtr', PartyIdentification113, False)

	@Dbtr.deleter
	def Dbtr(self):
		del self._Dbtr
		self._Dbtr = base_types.UninitialisedField(self, 'Dbtr', PartyIdentification113, False)

	@property
	def DbtrAcct(self):
		return self._DbtrAcct

	@DbtrAcct.setter
	def DbtrAcct(self, value):
		self._DbtrAcct = value if value is not None else base_types.UninitialisedField(self, 'DbtrAcct', AccountIdentificationAndName5, False)

	@DbtrAcct.deleter
	def DbtrAcct(self):
		del self._DbtrAcct
		self._DbtrAcct = base_types.UninitialisedField(self, 'DbtrAcct', AccountIdentificationAndName5, False)

	@property
	def DbtrAgt(self):
		return self._DbtrAgt

	@DbtrAgt.setter
	def DbtrAgt(self, value):
		self._DbtrAgt = value if value is not None else base_types.UninitialisedField(self, 'DbtrAgt', FinancialInstitutionIdentification10, False)

	@DbtrAgt.deleter
	def DbtrAgt(self):
		del self._DbtrAgt
		self._DbtrAgt = base_types.UninitialisedField(self, 'DbtrAgt', FinancialInstitutionIdentification10, False)

	@property
	def DbtrAgtBrnch(self):
		return self._DbtrAgtBrnch

	@DbtrAgtBrnch.setter
	def DbtrAgtBrnch(self, value):
		self._DbtrAgtBrnch = value if value is not None else base_types.UninitialisedField(self, 'DbtrAgtBrnch', BranchData, False)

	@DbtrAgtBrnch.deleter
	def DbtrAgtBrnch(self):
		del self._DbtrAgtBrnch
		self._DbtrAgtBrnch = base_types.UninitialisedField(self, 'DbtrAgtBrnch', BranchData, False)

	@property
	def DbtrNtlRegnNb(self):
		return self._DbtrNtlRegnNb

	@DbtrNtlRegnNb.setter
	def DbtrNtlRegnNb(self, value):
		self._DbtrNtlRegnNb = value if value is not None else base_types.UninitialisedField(self, 'DbtrNtlRegnNb', Max35Text, False)

	@DbtrNtlRegnNb.deleter
	def DbtrNtlRegnNb(self):
		del self._DbtrNtlRegnNb
		self._DbtrNtlRegnNb = base_types.UninitialisedField(self, 'DbtrNtlRegnNb', Max35Text, False)

	@property
	def DbtrTaxIdNb(self):
		return self._DbtrTaxIdNb

	@DbtrTaxIdNb.setter
	def DbtrTaxIdNb(self, value):
		self._DbtrTaxIdNb = value if value is not None else base_types.UninitialisedField(self, 'DbtrTaxIdNb', Max35Text, False)

	@DbtrTaxIdNb.deleter
	def DbtrTaxIdNb(self):
		del self._DbtrTaxIdNb
		self._DbtrTaxIdNb = base_types.UninitialisedField(self, 'DbtrTaxIdNb', Max35Text, False)

	@property
	def MndtId(self):
		return self._MndtId

	@MndtId.setter
	def MndtId(self, value):
		self._MndtId = value if value is not None else base_types.UninitialisedField(self, 'MndtId', Max35Text, False)

	@MndtId.deleter
	def MndtId(self):
		del self._MndtId
		self._MndtId = base_types.UninitialisedField(self, 'MndtId', Max35Text, False)

	@property
	def RegnId(self):
		return self._RegnId

	@RegnId.setter
	def RegnId(self, value):
		self._RegnId = value if value is not None else base_types.UninitialisedField(self, 'RegnId', Max35Text, False)

	@RegnId.deleter
	def RegnId(self):
		del self._RegnId
		self._RegnId = base_types.UninitialisedField(self, 'RegnId', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cdtr', type=PartyIdentification113, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrAgt', type=FinancialInstitutionIdentification10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrAgtBrnch', type=BranchData, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dbtr', type=PartyIdentification113, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrAcct', type=AccountIdentificationAndName5, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrAgt', type=FinancialInstitutionIdentification10, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrAgtBrnch', type=BranchData, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrNtlRegnNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrTaxIdNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MndtId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))