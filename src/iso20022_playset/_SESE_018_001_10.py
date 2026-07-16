# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountHoldingInformationV10

class SESE_018_001_10():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:sese.018.001.10"
		_docname = "sese.018.001.10"

		__slots__ = ["_AcctHldgInf"]
		@property
		def AcctHldgInf(self):
			return self._AcctHldgInf

		@AcctHldgInf.setter
		def AcctHldgInf(self, value):
			self._AcctHldgInf = value if value is not None else base_types.UninitialisedField(self, 'AcctHldgInf', AccountHoldingInformationV10, False)

		@AcctHldgInf.deleter
		def AcctHldgInf(self):
			del self._AcctHldgInf
			self._AcctHldgInf = base_types.UninitialisedField(self, 'AcctHldgInf', AccountHoldingInformationV10, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctHldgInf', type=AccountHoldingInformationV10, min=1, max=1, mutex_group=None, array=False),
		))