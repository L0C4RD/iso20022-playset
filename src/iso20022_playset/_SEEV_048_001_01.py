# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ShareholderIdentificationDisclosureResponseCancellationAdviceV01 import ShareholderIdentificationDisclosureResponseCancellationAdviceV01

class SEEV_048_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:seev.048.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_ShrhldrIdDsclsrRspnCxlAdvc"]
		@property
		def ShrhldrIdDsclsrRspnCxlAdvc(self):
			return self._ShrhldrIdDsclsrRspnCxlAdvc

		@ShrhldrIdDsclsrRspnCxlAdvc.setter
		def ShrhldrIdDsclsrRspnCxlAdvc(self, value):
			self._ShrhldrIdDsclsrRspnCxlAdvc = value if type(value) != base_types.auto else self.make_default("ShrhldrIdDsclsrRspnCxlAdvc")

		@ShrhldrIdDsclsrRspnCxlAdvc.deleter
		def ShrhldrIdDsclsrRspnCxlAdvc(self):
			del self._ShrhldrIdDsclsrRspnCxlAdvc
			self._ShrhldrIdDsclsrRspnCxlAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ShrhldrIdDsclsrRspnCxlAdvc', type=ShareholderIdentificationDisclosureResponseCancellationAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))