# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ShareholderIdentificationDisclosureResponseCancellationAdviceV01

class SEEV_048_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:seev.048.001.01"
		_docname = "seev.048.001.01"

		__slots__ = ["_ShrhldrIdDsclsrRspnCxlAdvc"]
		@property
		def ShrhldrIdDsclsrRspnCxlAdvc(self):
			return self._ShrhldrIdDsclsrRspnCxlAdvc

		@ShrhldrIdDsclsrRspnCxlAdvc.setter
		def ShrhldrIdDsclsrRspnCxlAdvc(self, value):
			self._ShrhldrIdDsclsrRspnCxlAdvc = value if value is not None else base_types.UninitialisedField(self, 'ShrhldrIdDsclsrRspnCxlAdvc', ShareholderIdentificationDisclosureResponseCancellationAdviceV01, False)

		@ShrhldrIdDsclsrRspnCxlAdvc.deleter
		def ShrhldrIdDsclsrRspnCxlAdvc(self):
			del self._ShrhldrIdDsclsrRspnCxlAdvc
			self._ShrhldrIdDsclsrRspnCxlAdvc = base_types.UninitialisedField(self, 'ShrhldrIdDsclsrRspnCxlAdvc', ShareholderIdentificationDisclosureResponseCancellationAdviceV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='ShrhldrIdDsclsrRspnCxlAdvc', type=ShareholderIdentificationDisclosureResponseCancellationAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))