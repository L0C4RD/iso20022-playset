# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AccountHoldingInformationRequestV08 import AccountHoldingInformationRequestV08

class SESE_019_001_08():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:sese.019.001.08"
		_docname = "sese.019.001.08"

		__slots__ = ["_AcctHldgInfReq"]
		@property
		def AcctHldgInfReq(self):
			return self._AcctHldgInfReq

		@AcctHldgInfReq.setter
		def AcctHldgInfReq(self, value):
			self._AcctHldgInfReq = value if type(value) != base_types.auto else self.make_default("AcctHldgInfReq")

		@AcctHldgInfReq.deleter
		def AcctHldgInfReq(self):
			del self._AcctHldgInfReq
			self._AcctHldgInfReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctHldgInfReq', type=AccountHoldingInformationRequestV08, min=1, max=1, mutex_group=None, array=False),
		))