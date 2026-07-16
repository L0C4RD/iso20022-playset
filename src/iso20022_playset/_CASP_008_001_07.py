# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SaleToPOIAdministrativeResponseV07

class CASP_008_001_07():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:casp.008.001.07"
		_docname = "casp.008.001.07"

		__slots__ = ["_SaleToPOIAdmstvRspn"]
		@property
		def SaleToPOIAdmstvRspn(self):
			return self._SaleToPOIAdmstvRspn

		@SaleToPOIAdmstvRspn.setter
		def SaleToPOIAdmstvRspn(self, value):
			self._SaleToPOIAdmstvRspn = value if value is not None else base_types.UninitialisedField(self, 'SaleToPOIAdmstvRspn', SaleToPOIAdministrativeResponseV07, False)

		@SaleToPOIAdmstvRspn.deleter
		def SaleToPOIAdmstvRspn(self):
			del self._SaleToPOIAdmstvRspn
			self._SaleToPOIAdmstvRspn = base_types.UninitialisedField(self, 'SaleToPOIAdmstvRspn', SaleToPOIAdministrativeResponseV07, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SaleToPOIAdmstvRspn', type=SaleToPOIAdministrativeResponseV07, min=1, max=1, mutex_group=None, array=False),
		))