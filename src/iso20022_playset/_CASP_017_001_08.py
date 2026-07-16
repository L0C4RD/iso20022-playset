# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SaleToPOIDeviceResponseV08

class CASP_017_001_08():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:casp.017.001.08"
		_docname = "casp.017.001.08"

		__slots__ = ["_SaleToPOIDvcRspn"]
		@property
		def SaleToPOIDvcRspn(self):
			return self._SaleToPOIDvcRspn

		@SaleToPOIDvcRspn.setter
		def SaleToPOIDvcRspn(self, value):
			self._SaleToPOIDvcRspn = value if value is not None else base_types.UninitialisedField(self, 'SaleToPOIDvcRspn', SaleToPOIDeviceResponseV08, False)

		@SaleToPOIDvcRspn.deleter
		def SaleToPOIDvcRspn(self):
			del self._SaleToPOIDvcRspn
			self._SaleToPOIDvcRspn = base_types.UninitialisedField(self, 'SaleToPOIDvcRspn', SaleToPOIDeviceResponseV08, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SaleToPOIDvcRspn', type=SaleToPOIDeviceResponseV08, min=1, max=1, mutex_group=None, array=False),
		))