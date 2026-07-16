# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import StatusReportV15

class CATM_001_001_15():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:catm.001.001.15"
		_docname = "catm.001.001.15"

		__slots__ = ["_StsRpt"]
		@property
		def StsRpt(self):
			return self._StsRpt

		@StsRpt.setter
		def StsRpt(self, value):
			self._StsRpt = value if value is not None else base_types.UninitialisedField(self, 'StsRpt', StatusReportV15, False)

		@StsRpt.deleter
		def StsRpt(self):
			del self._StsRpt
			self._StsRpt = base_types.UninitialisedField(self, 'StsRpt', StatusReportV15, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='StsRpt', type=StatusReportV15, min=1, max=1, mutex_group=None, array=False),
		))