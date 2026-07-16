# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GetGeneralBusinessInformationV04

class CAMT_020_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.020.001.04"
		_docname = "camt.020.001.04"

		__slots__ = ["_GetGnlBizInf"]
		@property
		def GetGnlBizInf(self):
			return self._GetGnlBizInf

		@GetGnlBizInf.setter
		def GetGnlBizInf(self, value):
			self._GetGnlBizInf = value if value is not None else base_types.UninitialisedField(self, 'GetGnlBizInf', GetGeneralBusinessInformationV04, False)

		@GetGnlBizInf.deleter
		def GetGnlBizInf(self):
			del self._GetGnlBizInf
			self._GetGnlBizInf = base_types.UninitialisedField(self, 'GetGnlBizInf', GetGeneralBusinessInformationV04, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='GetGnlBizInf', type=GetGeneralBusinessInformationV04, min=1, max=1, mutex_group=None, array=False),
		))