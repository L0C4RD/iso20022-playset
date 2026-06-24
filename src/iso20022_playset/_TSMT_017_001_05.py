# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ForwardDataSetSubmissionReportV05 import ForwardDataSetSubmissionReportV05

class TSMT_017_001_05():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:tsmt.017.001.05",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_FwdDataSetSubmissnRpt"]
		@property
		def FwdDataSetSubmissnRpt(self):
			return self._FwdDataSetSubmissnRpt

		@FwdDataSetSubmissnRpt.setter
		def FwdDataSetSubmissnRpt(self, value):
			self._FwdDataSetSubmissnRpt = value if type(value) != base_types.auto else self.make_default("FwdDataSetSubmissnRpt")

		@FwdDataSetSubmissnRpt.deleter
		def FwdDataSetSubmissnRpt(self):
			del self._FwdDataSetSubmissnRpt
			self._FwdDataSetSubmissnRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FwdDataSetSubmissnRpt', type=ForwardDataSetSubmissionReportV05, min=1, max=1, mutex_group=None, array=False),
		))