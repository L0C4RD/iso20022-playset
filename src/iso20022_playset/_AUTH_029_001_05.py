# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._DerivativesTradeReportQueryV05 import DerivativesTradeReportQueryV05

class AUTH_029_001_05():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_DerivsTradRptQry"]
		@property
		def DerivsTradRptQry(self):
			return self._DerivsTradRptQry

		@DerivsTradRptQry.setter
		def DerivsTradRptQry(self, value):
			self._DerivsTradRptQry = value if type(value) != base_types.auto else self.make_default("DerivsTradRptQry")

		@DerivsTradRptQry.deleter
		def DerivsTradRptQry(self):
			del self._DerivsTradRptQry
			self._DerivsTradRptQry = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='DerivsTradRptQry', type=DerivativesTradeReportQueryV05, min=1, max=1, mutex_group=None, array=False),
		))