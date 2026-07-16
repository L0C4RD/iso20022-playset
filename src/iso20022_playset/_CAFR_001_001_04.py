# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FraudReportingInitiationV04

class CAFR_001_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:cafr.001.001.04"
		_docname = "cafr.001.001.04"

		__slots__ = ["_FrdRptgInitn"]
		@property
		def FrdRptgInitn(self):
			return self._FrdRptgInitn

		@FrdRptgInitn.setter
		def FrdRptgInitn(self, value):
			self._FrdRptgInitn = value if value is not None else base_types.UninitialisedField(self, 'FrdRptgInitn', FraudReportingInitiationV04, False)

		@FrdRptgInitn.deleter
		def FrdRptgInitn(self):
			del self._FrdRptgInitn
			self._FrdRptgInitn = base_types.UninitialisedField(self, 'FrdRptgInitn', FraudReportingInitiationV04, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='FrdRptgInitn', type=FraudReportingInitiationV04, min=1, max=1, mutex_group=None, array=False),
		))