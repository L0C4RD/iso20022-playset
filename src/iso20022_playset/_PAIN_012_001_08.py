# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._MandateAcceptanceReportV08 import MandateAcceptanceReportV08

class PAIN_012_001_08():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:pain.012.001.08",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_MndtAccptncRpt"]
		@property
		def MndtAccptncRpt(self):
			return self._MndtAccptncRpt

		@MndtAccptncRpt.setter
		def MndtAccptncRpt(self, value):
			self._MndtAccptncRpt = value if type(value) != base_types.auto else self.make_default("MndtAccptncRpt")

		@MndtAccptncRpt.deleter
		def MndtAccptncRpt(self):
			del self._MndtAccptncRpt
			self._MndtAccptncRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='MndtAccptncRpt', type=MandateAcceptanceReportV08, min=1, max=1, mutex_group=None, array=False),
		))