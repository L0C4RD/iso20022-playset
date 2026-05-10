from . import base_types
from .ReportingRecordStatus1Code import ReportingRecordStatus1Code
from .Max15NumericText import Max15NumericText

class NumberOfRecordsPerStatus1(base_types._BaseFieldType):

	__slots__ = ["_DtldNbOfRcrds", "_DtldSts"]
	@property
	def DtldNbOfRcrds(self):
		return self._DtldNbOfRcrds

	@DtldNbOfRcrds.setter
	def DtldNbOfRcrds(self, value):
		self._DtldNbOfRcrds = value if type(value) != base_types.auto else self.make_default("DtldNbOfRcrds")

	@DtldNbOfRcrds.deleter
	def DtldNbOfRcrds(self):
		del self._DtldNbOfRcrds
		self._DtldNbOfRcrds = None

	@property
	def DtldSts(self):
		return self._DtldSts

	@DtldSts.setter
	def DtldSts(self, value):
		self._DtldSts = value if type(value) != base_types.auto else self.make_default("DtldSts")

	@DtldSts.deleter
	def DtldSts(self):
		del self._DtldSts
		self._DtldSts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DtldNbOfRcrds', type=Max15NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtldSts', type=ReportingRecordStatus1Code, min=1, max=1, mutex_group=None, array=False),
	))

