# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ChequeCancellationOrStopReportV02 import ChequeCancellationOrStopReportV02

class CAMT_109_001_02():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:camt.109.001.02",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_ChqCxlOrStopRpt"]
		@property
		def ChqCxlOrStopRpt(self):
			return self._ChqCxlOrStopRpt

		@ChqCxlOrStopRpt.setter
		def ChqCxlOrStopRpt(self, value):
			self._ChqCxlOrStopRpt = value if type(value) != base_types.auto else self.make_default("ChqCxlOrStopRpt")

		@ChqCxlOrStopRpt.deleter
		def ChqCxlOrStopRpt(self):
			del self._ChqCxlOrStopRpt
			self._ChqCxlOrStopRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ChqCxlOrStopRpt', type=ChequeCancellationOrStopReportV02, min=1, max=1, mutex_group=None, array=False),
		))