# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._FraudReportingInitiationV03 import FraudReportingInitiationV03

class CAFR_001_001_03():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:cafr.001.001.03"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_FrdRptgInitn"]
		@property
		def FrdRptgInitn(self):
			return self._FrdRptgInitn

		@FrdRptgInitn.setter
		def FrdRptgInitn(self, value):
			self._FrdRptgInitn = value if type(value) != base_types.auto else self.make_default("FrdRptgInitn")

		@FrdRptgInitn.deleter
		def FrdRptgInitn(self):
			del self._FrdRptgInitn
			self._FrdRptgInitn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FrdRptgInitn', type=FraudReportingInitiationV03, min=1, max=1, mutex_group=None, array=False),
		))