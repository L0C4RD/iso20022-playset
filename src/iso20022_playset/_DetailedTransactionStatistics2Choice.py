# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DetailedTransactionStatistics13
from . import ReportPeriodActivity1Code

class DetailedTransactionStatistics2Choice(base_types._BaseFieldType):

	__slots__ = ["_DataSetActn", "_DtldSttstcs"]
	@property
	def DataSetActn(self):
		return self._DataSetActn

	@DataSetActn.setter
	def DataSetActn(self, value):
		self._DataSetActn = value if value is not None else base_types.UninitialisedField(self, 'DataSetActn', ReportPeriodActivity1Code, False)

	@DataSetActn.deleter
	def DataSetActn(self):
		del self._DataSetActn
		self._DataSetActn = base_types.UninitialisedField(self, 'DataSetActn', ReportPeriodActivity1Code, False)

	@property
	def DtldSttstcs(self):
		return self._DtldSttstcs

	@DtldSttstcs.setter
	def DtldSttstcs(self, value):
		self._DtldSttstcs = value if value is not None else base_types.UninitialisedField(self, 'DtldSttstcs', DetailedTransactionStatistics13, False)

	@DtldSttstcs.deleter
	def DtldSttstcs(self):
		del self._DtldSttstcs
		self._DtldSttstcs = base_types.UninitialisedField(self, 'DtldSttstcs', DetailedTransactionStatistics13, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DataSetActn', type=ReportPeriodActivity1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='DtldSttstcs', type=DetailedTransactionStatistics13, min=0, max=1, mutex_group=1, array=False),
	))