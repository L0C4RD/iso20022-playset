# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CCPInteroperabilityReportV01 import CCPInteroperabilityReportV01

class AUTH_112_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:auth.112.001.01",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_CCPIntrprbltyRpt"]
		@property
		def CCPIntrprbltyRpt(self):
			return self._CCPIntrprbltyRpt

		@CCPIntrprbltyRpt.setter
		def CCPIntrprbltyRpt(self, value):
			self._CCPIntrprbltyRpt = value if type(value) != base_types.auto else self.make_default("CCPIntrprbltyRpt")

		@CCPIntrprbltyRpt.deleter
		def CCPIntrprbltyRpt(self):
			del self._CCPIntrprbltyRpt
			self._CCPIntrprbltyRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CCPIntrprbltyRpt', type=CCPInteroperabilityReportV01, min=1, max=1, mutex_group=None, array=False),
		))