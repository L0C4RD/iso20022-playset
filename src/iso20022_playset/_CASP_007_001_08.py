# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SaleToPOIAdministrativeRequestV08

class CASP_007_001_08():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:casp.007.001.08"
		_docname = "casp.007.001.08"

		__slots__ = ["_SaleToPOIAdmstvReq"]
		@property
		def SaleToPOIAdmstvReq(self):
			return self._SaleToPOIAdmstvReq

		@SaleToPOIAdmstvReq.setter
		def SaleToPOIAdmstvReq(self, value):
			self._SaleToPOIAdmstvReq = value if value is not None else base_types.UninitialisedField(self, 'SaleToPOIAdmstvReq', SaleToPOIAdministrativeRequestV08, False)

		@SaleToPOIAdmstvReq.deleter
		def SaleToPOIAdmstvReq(self):
			del self._SaleToPOIAdmstvReq
			self._SaleToPOIAdmstvReq = base_types.UninitialisedField(self, 'SaleToPOIAdmstvReq', SaleToPOIAdministrativeRequestV08, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SaleToPOIAdmstvReq', type=SaleToPOIAdministrativeRequestV08, min=1, max=1, mutex_group=None, array=False),
		))