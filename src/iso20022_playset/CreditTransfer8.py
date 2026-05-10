from . import base_types
import AccountIdentificationAndName5
import PartyIdentification113
import Max35Text
import FinancialInstitutionIdentification10

class CreditTransfer8(base_types._BaseFieldType):

	__slots__ = ["_Cdtr", "_IntrmyAgt2Acct", "_Ref", "_DbtrAgt", "_CdtrAcct", "_DbtrAgtAcct", "_Dbtr", "_IntrmyAgt1", "_DbtrAcct", "_IntrmyAgt2", "_CdtrAgtAcct", "_CdtrAgt", "_IntrmyAgt1Acct"]
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
	def IntrmyAgt2Acct(self):
		return self._IntrmyAgt2Acct

	@IntrmyAgt2Acct.setter
	def IntrmyAgt2Acct(self, value):
		self._IntrmyAgt2Acct = value if type(value) != auto else self.make_default("IntrmyAgt2Acct")

	@IntrmyAgt2Acct.deleter
	def IntrmyAgt2Acct(self):
		del self._IntrmyAgt2Acct
		self._IntrmyAgt2Acct = None

	@property
	def Ref(self):
		return self._Ref

	@Ref.setter
	def Ref(self, value):
		self._Ref = value if type(value) != auto else self.make_default("Ref")

	@Ref.deleter
	def Ref(self):
		del self._Ref
		self._Ref = None

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
	def DbtrAgtAcct(self):
		return self._DbtrAgtAcct

	@DbtrAgtAcct.setter
	def DbtrAgtAcct(self, value):
		self._DbtrAgtAcct = value if type(value) != auto else self.make_default("DbtrAgtAcct")

	@DbtrAgtAcct.deleter
	def DbtrAgtAcct(self):
		del self._DbtrAgtAcct
		self._DbtrAgtAcct = None

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
	def IntrmyAgt1(self):
		return self._IntrmyAgt1

	@IntrmyAgt1.setter
	def IntrmyAgt1(self, value):
		self._IntrmyAgt1 = value if type(value) != auto else self.make_default("IntrmyAgt1")

	@IntrmyAgt1.deleter
	def IntrmyAgt1(self):
		del self._IntrmyAgt1
		self._IntrmyAgt1 = None

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
	def IntrmyAgt2(self):
		return self._IntrmyAgt2

	@IntrmyAgt2.setter
	def IntrmyAgt2(self, value):
		self._IntrmyAgt2 = value if type(value) != auto else self.make_default("IntrmyAgt2")

	@IntrmyAgt2.deleter
	def IntrmyAgt2(self):
		del self._IntrmyAgt2
		self._IntrmyAgt2 = None

	@property
	def CdtrAgtAcct(self):
		return self._CdtrAgtAcct

	@CdtrAgtAcct.setter
	def CdtrAgtAcct(self, value):
		self._CdtrAgtAcct = value if type(value) != auto else self.make_default("CdtrAgtAcct")

	@CdtrAgtAcct.deleter
	def CdtrAgtAcct(self):
		del self._CdtrAgtAcct
		self._CdtrAgtAcct = None

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
	def IntrmyAgt1Acct(self):
		return self._IntrmyAgt1Acct

	@IntrmyAgt1Acct.setter
	def IntrmyAgt1Acct(self, value):
		self._IntrmyAgt1Acct = value if type(value) != auto else self.make_default("IntrmyAgt1Acct")

	@IntrmyAgt1Acct.deleter
	def IntrmyAgt1Acct(self):
		del self._IntrmyAgt1Acct
		self._IntrmyAgt1Acct = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cdtr', type=PartyIdentification113, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmyAgt2Acct', type=AccountIdentificationAndName5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ref', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrAgt', type=FinancialInstitutionIdentification10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrAcct', type=AccountIdentificationAndName5, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrAgtAcct', type=AccountIdentificationAndName5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dbtr', type=PartyIdentification113, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmyAgt1', type=FinancialInstitutionIdentification10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrAcct', type=AccountIdentificationAndName5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmyAgt2', type=FinancialInstitutionIdentification10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrAgtAcct', type=AccountIdentificationAndName5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrAgt', type=FinancialInstitutionIdentification10, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmyAgt1Acct', type=AccountIdentificationAndName5, min=0, max=1, mutex_group=None, array=False),
	))

