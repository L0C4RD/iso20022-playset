# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max15NumericText
from . import NumberOfRecordsPerStatus1

class OriginalReportStatistics3(base_types._BaseFieldType):

	__slots__ = ["_NbOfRcrdsPerSts", "_TtlNbOfRcrds"]
	@property
	def NbOfRcrdsPerSts(self):
		return self._NbOfRcrdsPerSts

	@NbOfRcrdsPerSts.setter
	def NbOfRcrdsPerSts(self, value):
		self._NbOfRcrdsPerSts = value if value is not None else base_types.UninitialisedField(self, 'NbOfRcrdsPerSts', NumberOfRecordsPerStatus1, True)

	@NbOfRcrdsPerSts.deleter
	def NbOfRcrdsPerSts(self):
		del self._NbOfRcrdsPerSts
		self._NbOfRcrdsPerSts = base_types.UninitialisedField(self, 'NbOfRcrdsPerSts', NumberOfRecordsPerStatus1, True)

	@property
	def TtlNbOfRcrds(self):
		return self._TtlNbOfRcrds

	@TtlNbOfRcrds.setter
	def TtlNbOfRcrds(self, value):
		self._TtlNbOfRcrds = value if value is not None else base_types.UninitialisedField(self, 'TtlNbOfRcrds', Max15NumericText, False)

	@TtlNbOfRcrds.deleter
	def TtlNbOfRcrds(self):
		del self._TtlNbOfRcrds
		self._TtlNbOfRcrds = base_types.UninitialisedField(self, 'TtlNbOfRcrds', Max15NumericText, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='NbOfRcrdsPerSts', type=NumberOfRecordsPerStatus1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TtlNbOfRcrds', type=Max15NumericText, min=1, max=1, mutex_group=None, array=False),
	))