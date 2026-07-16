# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SaleToPOIServiceResponseV07

class CASP_002_001_07():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:casp.002.001.07"
		_docname = "casp.002.001.07"

		__slots__ = ["_SaleToPOISvcRspn"]
		@property
		def SaleToPOISvcRspn(self):
			return self._SaleToPOISvcRspn

		@SaleToPOISvcRspn.setter
		def SaleToPOISvcRspn(self, value):
			self._SaleToPOISvcRspn = value if value is not None else base_types.UninitialisedField(self, 'SaleToPOISvcRspn', SaleToPOIServiceResponseV07, False)

		@SaleToPOISvcRspn.deleter
		def SaleToPOISvcRspn(self):
			del self._SaleToPOISvcRspn
			self._SaleToPOISvcRspn = base_types.UninitialisedField(self, 'SaleToPOISvcRspn', SaleToPOIServiceResponseV07, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SaleToPOISvcRspn', type=SaleToPOIServiceResponseV07, min=1, max=1, mutex_group=None, array=False),
		))