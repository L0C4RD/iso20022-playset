from . import base_types
from ._TrueFalseIndicator import TrueFalseIndicator
from ._AmountAndDirection102 import AmountAndDirection102
from ._GenericIdentification165 import GenericIdentification165

class PortfolioStressTestResult1(base_types._BaseFieldType):

	__slots__ = ["_RawStrssLoss", "_StrssLoss", "_PrtflId", "_Cover1Flg", "_Cover2Flg"]
	@property
	def Cover1Flg(self):
		return self._Cover1Flg

	@Cover1Flg.setter
	def Cover1Flg(self, value):
		self._Cover1Flg = value if type(value) != base_types.auto else self.make_default("Cover1Flg")

	@Cover1Flg.deleter
	def Cover1Flg(self):
		del self._Cover1Flg
		self._Cover1Flg = None

	@property
	def Cover2Flg(self):
		return self._Cover2Flg

	@Cover2Flg.setter
	def Cover2Flg(self, value):
		self._Cover2Flg = value if type(value) != base_types.auto else self.make_default("Cover2Flg")

	@Cover2Flg.deleter
	def Cover2Flg(self):
		del self._Cover2Flg
		self._Cover2Flg = None

	@property
	def PrtflId(self):
		return self._PrtflId

	@PrtflId.setter
	def PrtflId(self, value):
		self._PrtflId = value if type(value) != base_types.auto else self.make_default("PrtflId")

	@PrtflId.deleter
	def PrtflId(self):
		del self._PrtflId
		self._PrtflId = None

	@property
	def RawStrssLoss(self):
		return self._RawStrssLoss

	@RawStrssLoss.setter
	def RawStrssLoss(self, value):
		self._RawStrssLoss = value if type(value) != base_types.auto else self.make_default("RawStrssLoss")

	@RawStrssLoss.deleter
	def RawStrssLoss(self):
		del self._RawStrssLoss
		self._RawStrssLoss = None

	@property
	def StrssLoss(self):
		return self._StrssLoss

	@StrssLoss.setter
	def StrssLoss(self, value):
		self._StrssLoss = value if type(value) != base_types.auto else self.make_default("StrssLoss")

	@StrssLoss.deleter
	def StrssLoss(self):
		del self._StrssLoss
		self._StrssLoss = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cover1Flg', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cover2Flg', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtflId', type=GenericIdentification165, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RawStrssLoss', type=AmountAndDirection102, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StrssLoss', type=AmountAndDirection102, min=1, max=1, mutex_group=None, array=False),
	))

