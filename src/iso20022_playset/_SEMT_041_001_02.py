# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesBalanceTransparencyReportV02

class SEMT_041_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:semt.041.001.02"
		_docname = "semt.041.001.02"

		__slots__ = ["_SctiesBalTrnsprncyRpt"]
		@property
		def SctiesBalTrnsprncyRpt(self):
			return self._SctiesBalTrnsprncyRpt

		@SctiesBalTrnsprncyRpt.setter
		def SctiesBalTrnsprncyRpt(self, value):
			self._SctiesBalTrnsprncyRpt = value if value is not None else base_types.UninitialisedField(self, 'SctiesBalTrnsprncyRpt', SecuritiesBalanceTransparencyReportV02, False)

		@SctiesBalTrnsprncyRpt.deleter
		def SctiesBalTrnsprncyRpt(self):
			del self._SctiesBalTrnsprncyRpt
			self._SctiesBalTrnsprncyRpt = base_types.UninitialisedField(self, 'SctiesBalTrnsprncyRpt', SecuritiesBalanceTransparencyReportV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesBalTrnsprncyRpt', type=SecuritiesBalanceTransparencyReportV02, min=1, max=1, mutex_group=None, array=False),
		))