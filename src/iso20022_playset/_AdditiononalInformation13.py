from . import base_types
from ._PartyIdentification125Choice import PartyIdentification125Choice
from ._RestrictionStatus1Choice import RestrictionStatus1Choice
from ._Max35Text import Max35Text
from ._Max350Text import Max350Text
from ._DateTimePeriod2 import DateTimePeriod2

class AdditiononalInformation13(base_types._BaseFieldType):

	__slots__ = ["_Lmttn", "_Prd", "_Rgltr", "_AcctVldtn", "_AddtlInf", "_Sts", "_Tp"]
	@property
	def AcctVldtn(self):
		return self._AcctVldtn

	@AcctVldtn.setter
	def AcctVldtn(self, value):
		self._AcctVldtn = value if type(value) != base_types.auto else self.make_default("AcctVldtn")

	@AcctVldtn.deleter
	def AcctVldtn(self):
		del self._AcctVldtn
		self._AcctVldtn = None

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

	@property
	def Lmttn(self):
		return self._Lmttn

	@Lmttn.setter
	def Lmttn(self, value):
		self._Lmttn = value if type(value) != base_types.auto else self.make_default("Lmttn")

	@Lmttn.deleter
	def Lmttn(self):
		del self._Lmttn
		self._Lmttn = None

	@property
	def Prd(self):
		return self._Prd

	@Prd.setter
	def Prd(self, value):
		self._Prd = value if type(value) != base_types.auto else self.make_default("Prd")

	@Prd.deleter
	def Prd(self):
		del self._Prd
		self._Prd = None

	@property
	def Rgltr(self):
		return self._Rgltr

	@Rgltr.setter
	def Rgltr(self, value):
		self._Rgltr = value if type(value) != base_types.auto else self.make_default("Rgltr")

	@Rgltr.deleter
	def Rgltr(self):
		del self._Rgltr
		self._Rgltr = None

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if type(value) != base_types.auto else self.make_default("Sts")

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctVldtn', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lmttn', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prd', type=DateTimePeriod2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rgltr', type=PartyIdentification125Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sts', type=RestrictionStatus1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

