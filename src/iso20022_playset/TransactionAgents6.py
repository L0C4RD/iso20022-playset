from . import base_types
from .BranchAndFinancialInstitutionIdentification8 import BranchAndFinancialInstitutionIdentification8
from .ProprietaryAgent5 import ProprietaryAgent5

class TransactionAgents6(base_types._BaseFieldType):

	__slots__ = ["_InstdAgt", "_IntrmyAgt2", "_DbtrAgt", "_IntrmyAgt3", "_IssgAgt", "_InstgAgt", "_CdtrAgt", "_SttlmPlc", "_RcvgAgt", "_IntrmyAgt1", "_DlvrgAgt", "_Prtry"]
	@property
	def InstdAgt(self):
		return self._InstdAgt

	@InstdAgt.setter
	def InstdAgt(self, value):
		self._InstdAgt = value if type(value) != base_types.auto else self.make_default("InstdAgt")

	@InstdAgt.deleter
	def InstdAgt(self):
		del self._InstdAgt
		self._InstdAgt = None

	@property
	def IntrmyAgt2(self):
		return self._IntrmyAgt2

	@IntrmyAgt2.setter
	def IntrmyAgt2(self, value):
		self._IntrmyAgt2 = value if type(value) != base_types.auto else self.make_default("IntrmyAgt2")

	@IntrmyAgt2.deleter
	def IntrmyAgt2(self):
		del self._IntrmyAgt2
		self._IntrmyAgt2 = None

	@property
	def DbtrAgt(self):
		return self._DbtrAgt

	@DbtrAgt.setter
	def DbtrAgt(self, value):
		self._DbtrAgt = value if type(value) != base_types.auto else self.make_default("DbtrAgt")

	@DbtrAgt.deleter
	def DbtrAgt(self):
		del self._DbtrAgt
		self._DbtrAgt = None

	@property
	def IntrmyAgt3(self):
		return self._IntrmyAgt3

	@IntrmyAgt3.setter
	def IntrmyAgt3(self, value):
		self._IntrmyAgt3 = value if type(value) != base_types.auto else self.make_default("IntrmyAgt3")

	@IntrmyAgt3.deleter
	def IntrmyAgt3(self):
		del self._IntrmyAgt3
		self._IntrmyAgt3 = None

	@property
	def IssgAgt(self):
		return self._IssgAgt

	@IssgAgt.setter
	def IssgAgt(self, value):
		self._IssgAgt = value if type(value) != base_types.auto else self.make_default("IssgAgt")

	@IssgAgt.deleter
	def IssgAgt(self):
		del self._IssgAgt
		self._IssgAgt = None

	@property
	def InstgAgt(self):
		return self._InstgAgt

	@InstgAgt.setter
	def InstgAgt(self, value):
		self._InstgAgt = value if type(value) != base_types.auto else self.make_default("InstgAgt")

	@InstgAgt.deleter
	def InstgAgt(self):
		del self._InstgAgt
		self._InstgAgt = None

	@property
	def CdtrAgt(self):
		return self._CdtrAgt

	@CdtrAgt.setter
	def CdtrAgt(self, value):
		self._CdtrAgt = value if type(value) != base_types.auto else self.make_default("CdtrAgt")

	@CdtrAgt.deleter
	def CdtrAgt(self):
		del self._CdtrAgt
		self._CdtrAgt = None

	@property
	def SttlmPlc(self):
		return self._SttlmPlc

	@SttlmPlc.setter
	def SttlmPlc(self, value):
		self._SttlmPlc = value if type(value) != base_types.auto else self.make_default("SttlmPlc")

	@SttlmPlc.deleter
	def SttlmPlc(self):
		del self._SttlmPlc
		self._SttlmPlc = None

	@property
	def RcvgAgt(self):
		return self._RcvgAgt

	@RcvgAgt.setter
	def RcvgAgt(self, value):
		self._RcvgAgt = value if type(value) != base_types.auto else self.make_default("RcvgAgt")

	@RcvgAgt.deleter
	def RcvgAgt(self):
		del self._RcvgAgt
		self._RcvgAgt = None

	@property
	def IntrmyAgt1(self):
		return self._IntrmyAgt1

	@IntrmyAgt1.setter
	def IntrmyAgt1(self, value):
		self._IntrmyAgt1 = value if type(value) != base_types.auto else self.make_default("IntrmyAgt1")

	@IntrmyAgt1.deleter
	def IntrmyAgt1(self):
		del self._IntrmyAgt1
		self._IntrmyAgt1 = None

	@property
	def DlvrgAgt(self):
		return self._DlvrgAgt

	@DlvrgAgt.setter
	def DlvrgAgt(self, value):
		self._DlvrgAgt = value if type(value) != base_types.auto else self.make_default("DlvrgAgt")

	@DlvrgAgt.deleter
	def DlvrgAgt(self):
		del self._DlvrgAgt
		self._DlvrgAgt = None

	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if type(value) != base_types.auto else self.make_default("Prtry")

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='InstdAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmyAgt2', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmyAgt3', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssgAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstgAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmPlc', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcvgAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmyAgt1', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvrgAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prtry', type=ProprietaryAgent5, min=0, max=None, mutex_group=None, array=True),
	))

