# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DerivativesTradePositionSetReportV02

class AUTH_090_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:auth.090.001.02"
		_docname = "auth.090.001.02"

		__slots__ = ["_DerivsTradPosSetRpt"]
		@property
		def DerivsTradPosSetRpt(self):
			return self._DerivsTradPosSetRpt

		@DerivsTradPosSetRpt.setter
		def DerivsTradPosSetRpt(self, value):
			self._DerivsTradPosSetRpt = value if value is not None else base_types.UninitialisedField(self, 'DerivsTradPosSetRpt', DerivativesTradePositionSetReportV02, False)

		@DerivsTradPosSetRpt.deleter
		def DerivsTradPosSetRpt(self):
			del self._DerivsTradPosSetRpt
			self._DerivsTradPosSetRpt = base_types.UninitialisedField(self, 'DerivsTradPosSetRpt', DerivativesTradePositionSetReportV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='DerivsTradPosSetRpt', type=DerivativesTradePositionSetReportV02, min=1, max=1, mutex_group=None, array=False),
		))