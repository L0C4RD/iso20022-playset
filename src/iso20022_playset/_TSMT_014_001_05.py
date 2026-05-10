from . import base_types
from ._DataSetSubmissionV05 import DataSetSubmissionV05

class TSMT_014_001_05():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_DataSetSubmissn"]
		@property
		def DataSetSubmissn(self):
			return self._DataSetSubmissn

		@DataSetSubmissn.setter
		def DataSetSubmissn(self, value):
			self._DataSetSubmissn = value if type(value) != base_types.auto else self.make_default("DataSetSubmissn")

		@DataSetSubmissn.deleter
		def DataSetSubmissn(self):
			del self._DataSetSubmissn
			self._DataSetSubmissn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='DataSetSubmissn', type=DataSetSubmissionV05, min=1, max=1, mutex_group=None, array=False),
		))

