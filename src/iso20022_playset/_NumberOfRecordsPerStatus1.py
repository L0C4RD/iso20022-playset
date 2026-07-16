# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max15NumericText
from . import ReportingRecordStatus1Code

class NumberOfRecordsPerStatus1(base_types._BaseFieldType):

	__slots__ = ["_DtldNbOfRcrds", "_DtldSts"]
	@property
	def DtldNbOfRcrds(self):
		return self._DtldNbOfRcrds

	@DtldNbOfRcrds.setter
	def DtldNbOfRcrds(self, value):
		self._DtldNbOfRcrds = value if value is not None else base_types.UninitialisedField(self, 'DtldNbOfRcrds', Max15NumericText, False)

	@DtldNbOfRcrds.deleter
	def DtldNbOfRcrds(self):
		del self._DtldNbOfRcrds
		self._DtldNbOfRcrds = base_types.UninitialisedField(self, 'DtldNbOfRcrds', Max15NumericText, False)

	@property
	def DtldSts(self):
		return self._DtldSts

	@DtldSts.setter
	def DtldSts(self, value):
		self._DtldSts = value if value is not None else base_types.UninitialisedField(self, 'DtldSts', ReportingRecordStatus1Code, False)

	@DtldSts.deleter
	def DtldSts(self):
		del self._DtldSts
		self._DtldSts = base_types.UninitialisedField(self, 'DtldSts', ReportingRecordStatus1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DtldNbOfRcrds', type=Max15NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtldSts', type=ReportingRecordStatus1Code, min=1, max=1, mutex_group=None, array=False),
	))