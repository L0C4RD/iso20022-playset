# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SaleToPOIServiceRequestV08

class CASP_001_001_08():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:casp.001.001.08"
		_docname = "casp.001.001.08"

		__slots__ = ["_SaleToPOISvcReq"]
		@property
		def SaleToPOISvcReq(self):
			return self._SaleToPOISvcReq

		@SaleToPOISvcReq.setter
		def SaleToPOISvcReq(self, value):
			self._SaleToPOISvcReq = value if value is not None else base_types.UninitialisedField(self, 'SaleToPOISvcReq', SaleToPOIServiceRequestV08, False)

		@SaleToPOISvcReq.deleter
		def SaleToPOISvcReq(self):
			del self._SaleToPOISvcReq
			self._SaleToPOISvcReq = base_types.UninitialisedField(self, 'SaleToPOISvcReq', SaleToPOIServiceRequestV08, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SaleToPOISvcReq', type=SaleToPOIServiceRequestV08, min=1, max=1, mutex_group=None, array=False),
		))