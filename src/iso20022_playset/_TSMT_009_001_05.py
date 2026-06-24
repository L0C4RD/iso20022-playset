# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._BaselineAmendmentRequestV05 import BaselineAmendmentRequestV05

class TSMT_009_001_05():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:tsmt.009.001.05",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_BaselnAmdmntReq"]
		@property
		def BaselnAmdmntReq(self):
			return self._BaselnAmdmntReq

		@BaselnAmdmntReq.setter
		def BaselnAmdmntReq(self, value):
			self._BaselnAmdmntReq = value if type(value) != base_types.auto else self.make_default("BaselnAmdmntReq")

		@BaselnAmdmntReq.deleter
		def BaselnAmdmntReq(self):
			del self._BaselnAmdmntReq
			self._BaselnAmdmntReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='BaselnAmdmntReq', type=BaselineAmendmentRequestV05, min=1, max=1, mutex_group=None, array=False),
		))