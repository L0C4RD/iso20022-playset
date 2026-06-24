# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CollateralSubstitutionResponseV05 import CollateralSubstitutionResponseV05

class COLR_011_001_05():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:colr.011.001.05"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_CollSbstitnRspn"]
		@property
		def CollSbstitnRspn(self):
			return self._CollSbstitnRspn

		@CollSbstitnRspn.setter
		def CollSbstitnRspn(self, value):
			self._CollSbstitnRspn = value if type(value) != base_types.auto else self.make_default("CollSbstitnRspn")

		@CollSbstitnRspn.deleter
		def CollSbstitnRspn(self):
			del self._CollSbstitnRspn
			self._CollSbstitnRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CollSbstitnRspn', type=CollateralSubstitutionResponseV05, min=1, max=1, mutex_group=None, array=False),
		))