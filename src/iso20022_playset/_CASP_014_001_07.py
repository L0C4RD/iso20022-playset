# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SaleToPOIMessageStatusRequestV07

class CASP_014_001_07():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:casp.014.001.07"
		_docname = "casp.014.001.07"

		__slots__ = ["_SaleToPOIMsgStsReq"]
		@property
		def SaleToPOIMsgStsReq(self):
			return self._SaleToPOIMsgStsReq

		@SaleToPOIMsgStsReq.setter
		def SaleToPOIMsgStsReq(self, value):
			self._SaleToPOIMsgStsReq = value if value is not None else base_types.UninitialisedField(self, 'SaleToPOIMsgStsReq', SaleToPOIMessageStatusRequestV07, False)

		@SaleToPOIMsgStsReq.deleter
		def SaleToPOIMsgStsReq(self):
			del self._SaleToPOIMsgStsReq
			self._SaleToPOIMsgStsReq = base_types.UninitialisedField(self, 'SaleToPOIMsgStsReq', SaleToPOIMessageStatusRequestV07, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SaleToPOIMsgStsReq', type=SaleToPOIMessageStatusRequestV07, min=1, max=1, mutex_group=None, array=False),
		))