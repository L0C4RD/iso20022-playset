# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BranchAndFinancialInstitutionIdentification6
from . import CashAccount38
from . import Party40Choice

class TransactionParties8(base_types._BaseFieldType):

	__slots__ = ["_Cdtr", "_CdtrAcct", "_CdtrAgt", "_CdtrAgtAcct", "_Dbtr", "_DbtrAcct", "_DbtrAgt", "_DbtrAgtAcct", "_InitgPty", "_IntrmyAgt1", "_IntrmyAgt1Acct", "_IntrmyAgt2", "_IntrmyAgt2Acct", "_IntrmyAgt3", "_IntrmyAgt3Acct", "_PrvsInstgAgt1", "_PrvsInstgAgt1Acct", "_PrvsInstgAgt2", "_PrvsInstgAgt2Acct", "_PrvsInstgAgt3", "_PrvsInstgAgt3Acct", "_UltmtCdtr", "_UltmtDbtr"]
	@property
	def Cdtr(self):
		return self._Cdtr

	@Cdtr.setter
	def Cdtr(self, value):
		self._Cdtr = value if value is not None else base_types.UninitialisedField(self, 'Cdtr', Party40Choice, False)

	@Cdtr.deleter
	def Cdtr(self):
		del self._Cdtr
		self._Cdtr = base_types.UninitialisedField(self, 'Cdtr', Party40Choice, False)

	@property
	def CdtrAcct(self):
		return self._CdtrAcct

	@CdtrAcct.setter
	def CdtrAcct(self, value):
		self._CdtrAcct = value if value is not None else base_types.UninitialisedField(self, 'CdtrAcct', CashAccount38, False)

	@CdtrAcct.deleter
	def CdtrAcct(self):
		del self._CdtrAcct
		self._CdtrAcct = base_types.UninitialisedField(self, 'CdtrAcct', CashAccount38, False)

	@property
	def CdtrAgt(self):
		return self._CdtrAgt

	@CdtrAgt.setter
	def CdtrAgt(self, value):
		self._CdtrAgt = value if value is not None else base_types.UninitialisedField(self, 'CdtrAgt', BranchAndFinancialInstitutionIdentification6, False)

	@CdtrAgt.deleter
	def CdtrAgt(self):
		del self._CdtrAgt
		self._CdtrAgt = base_types.UninitialisedField(self, 'CdtrAgt', BranchAndFinancialInstitutionIdentification6, False)

	@property
	def CdtrAgtAcct(self):
		return self._CdtrAgtAcct

	@CdtrAgtAcct.setter
	def CdtrAgtAcct(self, value):
		self._CdtrAgtAcct = value if value is not None else base_types.UninitialisedField(self, 'CdtrAgtAcct', CashAccount38, False)

	@CdtrAgtAcct.deleter
	def CdtrAgtAcct(self):
		del self._CdtrAgtAcct
		self._CdtrAgtAcct = base_types.UninitialisedField(self, 'CdtrAgtAcct', CashAccount38, False)

	@property
	def Dbtr(self):
		return self._Dbtr

	@Dbtr.setter
	def Dbtr(self, value):
		self._Dbtr = value if value is not None else base_types.UninitialisedField(self, 'Dbtr', Party40Choice, False)

	@Dbtr.deleter
	def Dbtr(self):
		del self._Dbtr
		self._Dbtr = base_types.UninitialisedField(self, 'Dbtr', Party40Choice, False)

	@property
	def DbtrAcct(self):
		return self._DbtrAcct

	@DbtrAcct.setter
	def DbtrAcct(self, value):
		self._DbtrAcct = value if value is not None else base_types.UninitialisedField(self, 'DbtrAcct', CashAccount38, False)

	@DbtrAcct.deleter
	def DbtrAcct(self):
		del self._DbtrAcct
		self._DbtrAcct = base_types.UninitialisedField(self, 'DbtrAcct', CashAccount38, False)

	@property
	def DbtrAgt(self):
		return self._DbtrAgt

	@DbtrAgt.setter
	def DbtrAgt(self, value):
		self._DbtrAgt = value if value is not None else base_types.UninitialisedField(self, 'DbtrAgt', BranchAndFinancialInstitutionIdentification6, False)

	@DbtrAgt.deleter
	def DbtrAgt(self):
		del self._DbtrAgt
		self._DbtrAgt = base_types.UninitialisedField(self, 'DbtrAgt', BranchAndFinancialInstitutionIdentification6, False)

	@property
	def DbtrAgtAcct(self):
		return self._DbtrAgtAcct

	@DbtrAgtAcct.setter
	def DbtrAgtAcct(self, value):
		self._DbtrAgtAcct = value if value is not None else base_types.UninitialisedField(self, 'DbtrAgtAcct', CashAccount38, False)

	@DbtrAgtAcct.deleter
	def DbtrAgtAcct(self):
		del self._DbtrAgtAcct
		self._DbtrAgtAcct = base_types.UninitialisedField(self, 'DbtrAgtAcct', CashAccount38, False)

	@property
	def InitgPty(self):
		return self._InitgPty

	@InitgPty.setter
	def InitgPty(self, value):
		self._InitgPty = value if value is not None else base_types.UninitialisedField(self, 'InitgPty', Party40Choice, False)

	@InitgPty.deleter
	def InitgPty(self):
		del self._InitgPty
		self._InitgPty = base_types.UninitialisedField(self, 'InitgPty', Party40Choice, False)

	@property
	def IntrmyAgt1(self):
		return self._IntrmyAgt1

	@IntrmyAgt1.setter
	def IntrmyAgt1(self, value):
		self._IntrmyAgt1 = value if value is not None else base_types.UninitialisedField(self, 'IntrmyAgt1', BranchAndFinancialInstitutionIdentification6, False)

	@IntrmyAgt1.deleter
	def IntrmyAgt1(self):
		del self._IntrmyAgt1
		self._IntrmyAgt1 = base_types.UninitialisedField(self, 'IntrmyAgt1', BranchAndFinancialInstitutionIdentification6, False)

	@property
	def IntrmyAgt1Acct(self):
		return self._IntrmyAgt1Acct

	@IntrmyAgt1Acct.setter
	def IntrmyAgt1Acct(self, value):
		self._IntrmyAgt1Acct = value if value is not None else base_types.UninitialisedField(self, 'IntrmyAgt1Acct', CashAccount38, False)

	@IntrmyAgt1Acct.deleter
	def IntrmyAgt1Acct(self):
		del self._IntrmyAgt1Acct
		self._IntrmyAgt1Acct = base_types.UninitialisedField(self, 'IntrmyAgt1Acct', CashAccount38, False)

	@property
	def IntrmyAgt2(self):
		return self._IntrmyAgt2

	@IntrmyAgt2.setter
	def IntrmyAgt2(self, value):
		self._IntrmyAgt2 = value if value is not None else base_types.UninitialisedField(self, 'IntrmyAgt2', BranchAndFinancialInstitutionIdentification6, False)

	@IntrmyAgt2.deleter
	def IntrmyAgt2(self):
		del self._IntrmyAgt2
		self._IntrmyAgt2 = base_types.UninitialisedField(self, 'IntrmyAgt2', BranchAndFinancialInstitutionIdentification6, False)

	@property
	def IntrmyAgt2Acct(self):
		return self._IntrmyAgt2Acct

	@IntrmyAgt2Acct.setter
	def IntrmyAgt2Acct(self, value):
		self._IntrmyAgt2Acct = value if value is not None else base_types.UninitialisedField(self, 'IntrmyAgt2Acct', CashAccount38, False)

	@IntrmyAgt2Acct.deleter
	def IntrmyAgt2Acct(self):
		del self._IntrmyAgt2Acct
		self._IntrmyAgt2Acct = base_types.UninitialisedField(self, 'IntrmyAgt2Acct', CashAccount38, False)

	@property
	def IntrmyAgt3(self):
		return self._IntrmyAgt3

	@IntrmyAgt3.setter
	def IntrmyAgt3(self, value):
		self._IntrmyAgt3 = value if value is not None else base_types.UninitialisedField(self, 'IntrmyAgt3', BranchAndFinancialInstitutionIdentification6, False)

	@IntrmyAgt3.deleter
	def IntrmyAgt3(self):
		del self._IntrmyAgt3
		self._IntrmyAgt3 = base_types.UninitialisedField(self, 'IntrmyAgt3', BranchAndFinancialInstitutionIdentification6, False)

	@property
	def IntrmyAgt3Acct(self):
		return self._IntrmyAgt3Acct

	@IntrmyAgt3Acct.setter
	def IntrmyAgt3Acct(self, value):
		self._IntrmyAgt3Acct = value if value is not None else base_types.UninitialisedField(self, 'IntrmyAgt3Acct', CashAccount38, False)

	@IntrmyAgt3Acct.deleter
	def IntrmyAgt3Acct(self):
		del self._IntrmyAgt3Acct
		self._IntrmyAgt3Acct = base_types.UninitialisedField(self, 'IntrmyAgt3Acct', CashAccount38, False)

	@property
	def PrvsInstgAgt1(self):
		return self._PrvsInstgAgt1

	@PrvsInstgAgt1.setter
	def PrvsInstgAgt1(self, value):
		self._PrvsInstgAgt1 = value if value is not None else base_types.UninitialisedField(self, 'PrvsInstgAgt1', BranchAndFinancialInstitutionIdentification6, False)

	@PrvsInstgAgt1.deleter
	def PrvsInstgAgt1(self):
		del self._PrvsInstgAgt1
		self._PrvsInstgAgt1 = base_types.UninitialisedField(self, 'PrvsInstgAgt1', BranchAndFinancialInstitutionIdentification6, False)

	@property
	def PrvsInstgAgt1Acct(self):
		return self._PrvsInstgAgt1Acct

	@PrvsInstgAgt1Acct.setter
	def PrvsInstgAgt1Acct(self, value):
		self._PrvsInstgAgt1Acct = value if value is not None else base_types.UninitialisedField(self, 'PrvsInstgAgt1Acct', CashAccount38, False)

	@PrvsInstgAgt1Acct.deleter
	def PrvsInstgAgt1Acct(self):
		del self._PrvsInstgAgt1Acct
		self._PrvsInstgAgt1Acct = base_types.UninitialisedField(self, 'PrvsInstgAgt1Acct', CashAccount38, False)

	@property
	def PrvsInstgAgt2(self):
		return self._PrvsInstgAgt2

	@PrvsInstgAgt2.setter
	def PrvsInstgAgt2(self, value):
		self._PrvsInstgAgt2 = value if value is not None else base_types.UninitialisedField(self, 'PrvsInstgAgt2', BranchAndFinancialInstitutionIdentification6, False)

	@PrvsInstgAgt2.deleter
	def PrvsInstgAgt2(self):
		del self._PrvsInstgAgt2
		self._PrvsInstgAgt2 = base_types.UninitialisedField(self, 'PrvsInstgAgt2', BranchAndFinancialInstitutionIdentification6, False)

	@property
	def PrvsInstgAgt2Acct(self):
		return self._PrvsInstgAgt2Acct

	@PrvsInstgAgt2Acct.setter
	def PrvsInstgAgt2Acct(self, value):
		self._PrvsInstgAgt2Acct = value if value is not None else base_types.UninitialisedField(self, 'PrvsInstgAgt2Acct', CashAccount38, False)

	@PrvsInstgAgt2Acct.deleter
	def PrvsInstgAgt2Acct(self):
		del self._PrvsInstgAgt2Acct
		self._PrvsInstgAgt2Acct = base_types.UninitialisedField(self, 'PrvsInstgAgt2Acct', CashAccount38, False)

	@property
	def PrvsInstgAgt3(self):
		return self._PrvsInstgAgt3

	@PrvsInstgAgt3.setter
	def PrvsInstgAgt3(self, value):
		self._PrvsInstgAgt3 = value if value is not None else base_types.UninitialisedField(self, 'PrvsInstgAgt3', BranchAndFinancialInstitutionIdentification6, False)

	@PrvsInstgAgt3.deleter
	def PrvsInstgAgt3(self):
		del self._PrvsInstgAgt3
		self._PrvsInstgAgt3 = base_types.UninitialisedField(self, 'PrvsInstgAgt3', BranchAndFinancialInstitutionIdentification6, False)

	@property
	def PrvsInstgAgt3Acct(self):
		return self._PrvsInstgAgt3Acct

	@PrvsInstgAgt3Acct.setter
	def PrvsInstgAgt3Acct(self, value):
		self._PrvsInstgAgt3Acct = value if value is not None else base_types.UninitialisedField(self, 'PrvsInstgAgt3Acct', CashAccount38, False)

	@PrvsInstgAgt3Acct.deleter
	def PrvsInstgAgt3Acct(self):
		del self._PrvsInstgAgt3Acct
		self._PrvsInstgAgt3Acct = base_types.UninitialisedField(self, 'PrvsInstgAgt3Acct', CashAccount38, False)

	@property
	def UltmtCdtr(self):
		return self._UltmtCdtr

	@UltmtCdtr.setter
	def UltmtCdtr(self, value):
		self._UltmtCdtr = value if value is not None else base_types.UninitialisedField(self, 'UltmtCdtr', Party40Choice, False)

	@UltmtCdtr.deleter
	def UltmtCdtr(self):
		del self._UltmtCdtr
		self._UltmtCdtr = base_types.UninitialisedField(self, 'UltmtCdtr', Party40Choice, False)

	@property
	def UltmtDbtr(self):
		return self._UltmtDbtr

	@UltmtDbtr.setter
	def UltmtDbtr(self, value):
		self._UltmtDbtr = value if value is not None else base_types.UninitialisedField(self, 'UltmtDbtr', Party40Choice, False)

	@UltmtDbtr.deleter
	def UltmtDbtr(self):
		del self._UltmtDbtr
		self._UltmtDbtr = base_types.UninitialisedField(self, 'UltmtDbtr', Party40Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cdtr', type=Party40Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrAcct', type=CashAccount38, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrAgt', type=BranchAndFinancialInstitutionIdentification6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrAgtAcct', type=CashAccount38, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dbtr', type=Party40Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrAcct', type=CashAccount38, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrAgt', type=BranchAndFinancialInstitutionIdentification6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrAgtAcct', type=CashAccount38, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InitgPty', type=Party40Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmyAgt1', type=BranchAndFinancialInstitutionIdentification6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmyAgt1Acct', type=CashAccount38, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmyAgt2', type=BranchAndFinancialInstitutionIdentification6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmyAgt2Acct', type=CashAccount38, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmyAgt3', type=BranchAndFinancialInstitutionIdentification6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmyAgt3Acct', type=CashAccount38, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsInstgAgt1', type=BranchAndFinancialInstitutionIdentification6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsInstgAgt1Acct', type=CashAccount38, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsInstgAgt2', type=BranchAndFinancialInstitutionIdentification6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsInstgAgt2Acct', type=CashAccount38, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsInstgAgt3', type=BranchAndFinancialInstitutionIdentification6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsInstgAgt3Acct', type=CashAccount38, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UltmtCdtr', type=Party40Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UltmtDbtr', type=Party40Choice, min=0, max=1, mutex_group=None, array=False),
	))