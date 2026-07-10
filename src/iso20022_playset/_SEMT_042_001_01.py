# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesBalanceTransparencyReportStatusAdviceV01 import SecuritiesBalanceTransparencyReportStatusAdviceV01

class SEMT_042_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:semt.042.001.01"
		_docname = "semt.042.001.01"

		__slots__ = ["_SctiesBalTrnsprncyRptStsAdvc"]
		@property
		def SctiesBalTrnsprncyRptStsAdvc(self):
			return self._SctiesBalTrnsprncyRptStsAdvc

		@SctiesBalTrnsprncyRptStsAdvc.setter
		def SctiesBalTrnsprncyRptStsAdvc(self, value):
			self._SctiesBalTrnsprncyRptStsAdvc = value if type(value) != base_types.auto else self.make_default("SctiesBalTrnsprncyRptStsAdvc")

		@SctiesBalTrnsprncyRptStsAdvc.deleter
		def SctiesBalTrnsprncyRptStsAdvc(self):
			del self._SctiesBalTrnsprncyRptStsAdvc
			self._SctiesBalTrnsprncyRptStsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesBalTrnsprncyRptStsAdvc', type=SecuritiesBalanceTransparencyReportStatusAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))