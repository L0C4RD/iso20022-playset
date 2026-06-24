# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CCPInvestmentsReportV02 import CCPInvestmentsReportV02

class AUTH_061_001_02():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:auth.061.001.02",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_CCPInvstmtsRpt"]
		@property
		def CCPInvstmtsRpt(self):
			return self._CCPInvstmtsRpt

		@CCPInvstmtsRpt.setter
		def CCPInvstmtsRpt(self, value):
			self._CCPInvstmtsRpt = value if type(value) != base_types.auto else self.make_default("CCPInvstmtsRpt")

		@CCPInvstmtsRpt.deleter
		def CCPInvstmtsRpt(self):
			del self._CCPInvstmtsRpt
			self._CCPInvstmtsRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CCPInvstmtsRpt', type=CCPInvestmentsReportV02, min=1, max=1, mutex_group=None, array=False),
		))