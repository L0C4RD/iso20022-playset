# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesAccountQueryV01

class REDA_019_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:reda.019.001.01"
		_docname = "reda.019.001.01"

		__slots__ = ["_SctiesAcctQry"]
		@property
		def SctiesAcctQry(self):
			return self._SctiesAcctQry

		@SctiesAcctQry.setter
		def SctiesAcctQry(self, value):
			self._SctiesAcctQry = value if value is not None else base_types.UninitialisedField(self, 'SctiesAcctQry', SecuritiesAccountQueryV01, False)

		@SctiesAcctQry.deleter
		def SctiesAcctQry(self):
			del self._SctiesAcctQry
			self._SctiesAcctQry = base_types.UninitialisedField(self, 'SctiesAcctQry', SecuritiesAccountQueryV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesAcctQry', type=SecuritiesAccountQueryV01, min=1, max=1, mutex_group=None, array=False),
		))