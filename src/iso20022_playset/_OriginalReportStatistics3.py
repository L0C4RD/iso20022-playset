from . import base_types
from .NumberOfRecordsPerStatus1 import NumberOfRecordsPerStatus1
from .Max15NumericText import Max15NumericText

class OriginalReportStatistics3(base_types._BaseFieldType):

	__slots__ = ["_TtlNbOfRcrds", "_NbOfRcrdsPerSts"]
	@property
	def TtlNbOfRcrds(self):
		return self._TtlNbOfRcrds

	@TtlNbOfRcrds.setter
	def TtlNbOfRcrds(self, value):
		self._TtlNbOfRcrds = value if type(value) != base_types.auto else self.make_default("TtlNbOfRcrds")

	@TtlNbOfRcrds.deleter
	def TtlNbOfRcrds(self):
		del self._TtlNbOfRcrds
		self._TtlNbOfRcrds = None

	@property
	def NbOfRcrdsPerSts(self):
		return self._NbOfRcrdsPerSts

	@NbOfRcrdsPerSts.setter
	def NbOfRcrdsPerSts(self, value):
		self._NbOfRcrdsPerSts = value if type(value) != base_types.auto else self.make_default("NbOfRcrdsPerSts")

	@NbOfRcrdsPerSts.deleter
	def NbOfRcrdsPerSts(self):
		del self._NbOfRcrdsPerSts
		self._NbOfRcrdsPerSts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TtlNbOfRcrds', type=Max15NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfRcrdsPerSts', type=NumberOfRecordsPerStatus1, min=1, max=None, mutex_group=None, array=True),
	))

