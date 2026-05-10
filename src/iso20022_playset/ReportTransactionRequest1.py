from . import base_types
from .PositiveNumber import PositiveNumber
from .SearchCriteria1 import SearchCriteria1
from .TrueFalseIndicator import TrueFalseIndicator
from .SearchOutputOrder1 import SearchOutputOrder1

class ReportTransactionRequest1(base_types._BaseFieldType):

	__slots__ = ["_SchCrit", "_BlckStart", "_BlckStop", "_DscndgOrdr", "_SchOutptOrdr"]
	@property
	def SchCrit(self):
		return self._SchCrit

	@SchCrit.setter
	def SchCrit(self, value):
		self._SchCrit = value if type(value) != auto else self.make_default("SchCrit")

	@SchCrit.deleter
	def SchCrit(self):
		del self._SchCrit
		self._SchCrit = None

	@property
	def BlckStart(self):
		return self._BlckStart

	@BlckStart.setter
	def BlckStart(self, value):
		self._BlckStart = value if type(value) != auto else self.make_default("BlckStart")

	@BlckStart.deleter
	def BlckStart(self):
		del self._BlckStart
		self._BlckStart = None

	@property
	def BlckStop(self):
		return self._BlckStop

	@BlckStop.setter
	def BlckStop(self, value):
		self._BlckStop = value if type(value) != auto else self.make_default("BlckStop")

	@BlckStop.deleter
	def BlckStop(self):
		del self._BlckStop
		self._BlckStop = None

	@property
	def DscndgOrdr(self):
		return self._DscndgOrdr

	@DscndgOrdr.setter
	def DscndgOrdr(self, value):
		self._DscndgOrdr = value if type(value) != auto else self.make_default("DscndgOrdr")

	@DscndgOrdr.deleter
	def DscndgOrdr(self):
		del self._DscndgOrdr
		self._DscndgOrdr = None

	@property
	def SchOutptOrdr(self):
		return self._SchOutptOrdr

	@SchOutptOrdr.setter
	def SchOutptOrdr(self, value):
		self._SchOutptOrdr = value if type(value) != auto else self.make_default("SchOutptOrdr")

	@SchOutptOrdr.deleter
	def SchOutptOrdr(self):
		del self._SchOutptOrdr
		self._SchOutptOrdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SchCrit', type=SearchCriteria1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BlckStart', type=PositiveNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BlckStop', type=PositiveNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DscndgOrdr', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SchOutptOrdr', type=SearchOutputOrder1, min=0, max=1, mutex_group=None, array=False),
	))

