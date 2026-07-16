# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountHoldingInformationRequestV09

class SESE_019_001_09():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:sese.019.001.09"
		_docname = "sese.019.001.09"

		__slots__ = ["_AcctHldgInfReq"]
		@property
		def AcctHldgInfReq(self):
			return self._AcctHldgInfReq

		@AcctHldgInfReq.setter
		def AcctHldgInfReq(self, value):
			self._AcctHldgInfReq = value if value is not None else base_types.UninitialisedField(self, 'AcctHldgInfReq', AccountHoldingInformationRequestV09, False)

		@AcctHldgInfReq.deleter
		def AcctHldgInfReq(self):
			del self._AcctHldgInfReq
			self._AcctHldgInfReq = base_types.UninitialisedField(self, 'AcctHldgInfReq', AccountHoldingInformationRequestV09, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctHldgInfReq', type=AccountHoldingInformationRequestV09, min=1, max=1, mutex_group=None, array=False),
		))