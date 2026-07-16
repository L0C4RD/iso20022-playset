# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SaleToPOIDeviceRequestV07

class CASP_016_001_07():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:casp.016.001.07"
		_docname = "casp.016.001.07"

		__slots__ = ["_SaleToPOIDvcReq"]
		@property
		def SaleToPOIDvcReq(self):
			return self._SaleToPOIDvcReq

		@SaleToPOIDvcReq.setter
		def SaleToPOIDvcReq(self, value):
			self._SaleToPOIDvcReq = value if value is not None else base_types.UninitialisedField(self, 'SaleToPOIDvcReq', SaleToPOIDeviceRequestV07, False)

		@SaleToPOIDvcReq.deleter
		def SaleToPOIDvcReq(self):
			del self._SaleToPOIDvcReq
			self._SaleToPOIDvcReq = base_types.UninitialisedField(self, 'SaleToPOIDvcReq', SaleToPOIDeviceRequestV07, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SaleToPOIDvcReq', type=SaleToPOIDeviceRequestV07, min=1, max=1, mutex_group=None, array=False),
		))