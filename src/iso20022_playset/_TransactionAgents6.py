# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BranchAndFinancialInstitutionIdentification8
from . import ProprietaryAgent5

class TransactionAgents6(base_types._BaseFieldType):

	__slots__ = ["_CdtrAgt", "_DbtrAgt", "_DlvrgAgt", "_InstdAgt", "_InstgAgt", "_IntrmyAgt1", "_IntrmyAgt2", "_IntrmyAgt3", "_IssgAgt", "_Prtry", "_RcvgAgt", "_SttlmPlc"]
	@property
	def CdtrAgt(self):
		return self._CdtrAgt

	@CdtrAgt.setter
	def CdtrAgt(self, value):
		self._CdtrAgt = value if value is not None else base_types.UninitialisedField(self, 'CdtrAgt', BranchAndFinancialInstitutionIdentification8, False)

	@CdtrAgt.deleter
	def CdtrAgt(self):
		del self._CdtrAgt
		self._CdtrAgt = base_types.UninitialisedField(self, 'CdtrAgt', BranchAndFinancialInstitutionIdentification8, False)

	@property
	def DbtrAgt(self):
		return self._DbtrAgt

	@DbtrAgt.setter
	def DbtrAgt(self, value):
		self._DbtrAgt = value if value is not None else base_types.UninitialisedField(self, 'DbtrAgt', BranchAndFinancialInstitutionIdentification8, False)

	@DbtrAgt.deleter
	def DbtrAgt(self):
		del self._DbtrAgt
		self._DbtrAgt = base_types.UninitialisedField(self, 'DbtrAgt', BranchAndFinancialInstitutionIdentification8, False)

	@property
	def DlvrgAgt(self):
		return self._DlvrgAgt

	@DlvrgAgt.setter
	def DlvrgAgt(self, value):
		self._DlvrgAgt = value if value is not None else base_types.UninitialisedField(self, 'DlvrgAgt', BranchAndFinancialInstitutionIdentification8, False)

	@DlvrgAgt.deleter
	def DlvrgAgt(self):
		del self._DlvrgAgt
		self._DlvrgAgt = base_types.UninitialisedField(self, 'DlvrgAgt', BranchAndFinancialInstitutionIdentification8, False)

	@property
	def InstdAgt(self):
		return self._InstdAgt

	@InstdAgt.setter
	def InstdAgt(self, value):
		self._InstdAgt = value if value is not None else base_types.UninitialisedField(self, 'InstdAgt', BranchAndFinancialInstitutionIdentification8, False)

	@InstdAgt.deleter
	def InstdAgt(self):
		del self._InstdAgt
		self._InstdAgt = base_types.UninitialisedField(self, 'InstdAgt', BranchAndFinancialInstitutionIdentification8, False)

	@property
	def InstgAgt(self):
		return self._InstgAgt

	@InstgAgt.setter
	def InstgAgt(self, value):
		self._InstgAgt = value if value is not None else base_types.UninitialisedField(self, 'InstgAgt', BranchAndFinancialInstitutionIdentification8, False)

	@InstgAgt.deleter
	def InstgAgt(self):
		del self._InstgAgt
		self._InstgAgt = base_types.UninitialisedField(self, 'InstgAgt', BranchAndFinancialInstitutionIdentification8, False)

	@property
	def IntrmyAgt1(self):
		return self._IntrmyAgt1

	@IntrmyAgt1.setter
	def IntrmyAgt1(self, value):
		self._IntrmyAgt1 = value if value is not None else base_types.UninitialisedField(self, 'IntrmyAgt1', BranchAndFinancialInstitutionIdentification8, False)

	@IntrmyAgt1.deleter
	def IntrmyAgt1(self):
		del self._IntrmyAgt1
		self._IntrmyAgt1 = base_types.UninitialisedField(self, 'IntrmyAgt1', BranchAndFinancialInstitutionIdentification8, False)

	@property
	def IntrmyAgt2(self):
		return self._IntrmyAgt2

	@IntrmyAgt2.setter
	def IntrmyAgt2(self, value):
		self._IntrmyAgt2 = value if value is not None else base_types.UninitialisedField(self, 'IntrmyAgt2', BranchAndFinancialInstitutionIdentification8, False)

	@IntrmyAgt2.deleter
	def IntrmyAgt2(self):
		del self._IntrmyAgt2
		self._IntrmyAgt2 = base_types.UninitialisedField(self, 'IntrmyAgt2', BranchAndFinancialInstitutionIdentification8, False)

	@property
	def IntrmyAgt3(self):
		return self._IntrmyAgt3

	@IntrmyAgt3.setter
	def IntrmyAgt3(self, value):
		self._IntrmyAgt3 = value if value is not None else base_types.UninitialisedField(self, 'IntrmyAgt3', BranchAndFinancialInstitutionIdentification8, False)

	@IntrmyAgt3.deleter
	def IntrmyAgt3(self):
		del self._IntrmyAgt3
		self._IntrmyAgt3 = base_types.UninitialisedField(self, 'IntrmyAgt3', BranchAndFinancialInstitutionIdentification8, False)

	@property
	def IssgAgt(self):
		return self._IssgAgt

	@IssgAgt.setter
	def IssgAgt(self, value):
		self._IssgAgt = value if value is not None else base_types.UninitialisedField(self, 'IssgAgt', BranchAndFinancialInstitutionIdentification8, False)

	@IssgAgt.deleter
	def IssgAgt(self):
		del self._IssgAgt
		self._IssgAgt = base_types.UninitialisedField(self, 'IssgAgt', BranchAndFinancialInstitutionIdentification8, False)

	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if value is not None else base_types.UninitialisedField(self, 'Prtry', ProprietaryAgent5, True)

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = base_types.UninitialisedField(self, 'Prtry', ProprietaryAgent5, True)

	@property
	def RcvgAgt(self):
		return self._RcvgAgt

	@RcvgAgt.setter
	def RcvgAgt(self, value):
		self._RcvgAgt = value if value is not None else base_types.UninitialisedField(self, 'RcvgAgt', BranchAndFinancialInstitutionIdentification8, False)

	@RcvgAgt.deleter
	def RcvgAgt(self):
		del self._RcvgAgt
		self._RcvgAgt = base_types.UninitialisedField(self, 'RcvgAgt', BranchAndFinancialInstitutionIdentification8, False)

	@property
	def SttlmPlc(self):
		return self._SttlmPlc

	@SttlmPlc.setter
	def SttlmPlc(self, value):
		self._SttlmPlc = value if value is not None else base_types.UninitialisedField(self, 'SttlmPlc', BranchAndFinancialInstitutionIdentification8, False)

	@SttlmPlc.deleter
	def SttlmPlc(self):
		del self._SttlmPlc
		self._SttlmPlc = base_types.UninitialisedField(self, 'SttlmPlc', BranchAndFinancialInstitutionIdentification8, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CdtrAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvrgAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstdAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstgAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmyAgt1', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmyAgt2', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmyAgt3', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssgAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prtry', type=ProprietaryAgent5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RcvgAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmPlc', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
	))