# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SaleToPOIServiceResponseV07 import SaleToPOIServiceResponseV07

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
			self._SaleToPOISvcRspn = value if type(value) != base_types.auto else self.make_default("SaleToPOISvcRspn")

		@SaleToPOISvcRspn.deleter
		def SaleToPOISvcRspn(self):
			del self._SaleToPOISvcRspn
			self._SaleToPOISvcRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SaleToPOISvcRspn', type=SaleToPOIServiceResponseV07, min=1, max=1, mutex_group=None, array=False),
		))