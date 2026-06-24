# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SaleToPOIReconciliationResponseV08 import SaleToPOIReconciliationResponseV08

class CASP_004_001_08():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:casp.004.001.08"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_SaleToPOIRcncltnRspn"]
		@property
		def SaleToPOIRcncltnRspn(self):
			return self._SaleToPOIRcncltnRspn

		@SaleToPOIRcncltnRspn.setter
		def SaleToPOIRcncltnRspn(self, value):
			self._SaleToPOIRcncltnRspn = value if type(value) != base_types.auto else self.make_default("SaleToPOIRcncltnRspn")

		@SaleToPOIRcncltnRspn.deleter
		def SaleToPOIRcncltnRspn(self):
			del self._SaleToPOIRcncltnRspn
			self._SaleToPOIRcncltnRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SaleToPOIRcncltnRspn', type=SaleToPOIReconciliationResponseV08, min=1, max=1, mutex_group=None, array=False),
		))