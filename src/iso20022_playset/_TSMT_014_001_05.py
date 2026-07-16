# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DataSetSubmissionV05

class TSMT_014_001_05():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:tsmt.014.001.05"
		_docname = "tsmt.014.001.05"

		__slots__ = ["_DataSetSubmissn"]
		@property
		def DataSetSubmissn(self):
			return self._DataSetSubmissn

		@DataSetSubmissn.setter
		def DataSetSubmissn(self, value):
			self._DataSetSubmissn = value if value is not None else base_types.UninitialisedField(self, 'DataSetSubmissn', DataSetSubmissionV05, False)

		@DataSetSubmissn.deleter
		def DataSetSubmissn(self):
			del self._DataSetSubmissn
			self._DataSetSubmissn = base_types.UninitialisedField(self, 'DataSetSubmissn', DataSetSubmissionV05, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='DataSetSubmissn', type=DataSetSubmissionV05, min=1, max=1, mutex_group=None, array=False),
		))