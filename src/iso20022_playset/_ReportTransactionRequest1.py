# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PositiveNumber
from . import SearchCriteria1
from . import SearchOutputOrder1
from . import TrueFalseIndicator

class ReportTransactionRequest1(base_types._BaseFieldType):

	__slots__ = ["_BlckStart", "_BlckStop", "_DscndgOrdr", "_SchCrit", "_SchOutptOrdr"]
	@property
	def BlckStart(self):
		return self._BlckStart

	@BlckStart.setter
	def BlckStart(self, value):
		self._BlckStart = value if value is not None else base_types.UninitialisedField(self, 'BlckStart', PositiveNumber, False)

	@BlckStart.deleter
	def BlckStart(self):
		del self._BlckStart
		self._BlckStart = base_types.UninitialisedField(self, 'BlckStart', PositiveNumber, False)

	@property
	def BlckStop(self):
		return self._BlckStop

	@BlckStop.setter
	def BlckStop(self, value):
		self._BlckStop = value if value is not None else base_types.UninitialisedField(self, 'BlckStop', PositiveNumber, False)

	@BlckStop.deleter
	def BlckStop(self):
		del self._BlckStop
		self._BlckStop = base_types.UninitialisedField(self, 'BlckStop', PositiveNumber, False)

	@property
	def DscndgOrdr(self):
		return self._DscndgOrdr

	@DscndgOrdr.setter
	def DscndgOrdr(self, value):
		self._DscndgOrdr = value if value is not None else base_types.UninitialisedField(self, 'DscndgOrdr', TrueFalseIndicator, False)

	@DscndgOrdr.deleter
	def DscndgOrdr(self):
		del self._DscndgOrdr
		self._DscndgOrdr = base_types.UninitialisedField(self, 'DscndgOrdr', TrueFalseIndicator, False)

	@property
	def SchCrit(self):
		return self._SchCrit

	@SchCrit.setter
	def SchCrit(self, value):
		self._SchCrit = value if value is not None else base_types.UninitialisedField(self, 'SchCrit', SearchCriteria1, True)

	@SchCrit.deleter
	def SchCrit(self):
		del self._SchCrit
		self._SchCrit = base_types.UninitialisedField(self, 'SchCrit', SearchCriteria1, True)

	@property
	def SchOutptOrdr(self):
		return self._SchOutptOrdr

	@SchOutptOrdr.setter
	def SchOutptOrdr(self, value):
		self._SchOutptOrdr = value if value is not None else base_types.UninitialisedField(self, 'SchOutptOrdr', SearchOutputOrder1, False)

	@SchOutptOrdr.deleter
	def SchOutptOrdr(self):
		del self._SchOutptOrdr
		self._SchOutptOrdr = base_types.UninitialisedField(self, 'SchOutptOrdr', SearchOutputOrder1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BlckStart', type=PositiveNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BlckStop', type=PositiveNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DscndgOrdr', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SchCrit', type=SearchCriteria1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SchOutptOrdr', type=SearchOutputOrder1, min=0, max=1, mutex_group=None, array=False),
	))