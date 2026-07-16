# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ShareholderIdentificationDisclosureResponseStatusAdviceV01

class SEEV_049_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:seev.049.001.01"
		_docname = "seev.049.001.01"

		__slots__ = ["_ShrhldrIdDsclsrRspnStsAdvc"]
		@property
		def ShrhldrIdDsclsrRspnStsAdvc(self):
			return self._ShrhldrIdDsclsrRspnStsAdvc

		@ShrhldrIdDsclsrRspnStsAdvc.setter
		def ShrhldrIdDsclsrRspnStsAdvc(self, value):
			self._ShrhldrIdDsclsrRspnStsAdvc = value if value is not None else base_types.UninitialisedField(self, 'ShrhldrIdDsclsrRspnStsAdvc', ShareholderIdentificationDisclosureResponseStatusAdviceV01, False)

		@ShrhldrIdDsclsrRspnStsAdvc.deleter
		def ShrhldrIdDsclsrRspnStsAdvc(self):
			del self._ShrhldrIdDsclsrRspnStsAdvc
			self._ShrhldrIdDsclsrRspnStsAdvc = base_types.UninitialisedField(self, 'ShrhldrIdDsclsrRspnStsAdvc', ShareholderIdentificationDisclosureResponseStatusAdviceV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='ShrhldrIdDsclsrRspnStsAdvc', type=ShareholderIdentificationDisclosureResponseStatusAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))