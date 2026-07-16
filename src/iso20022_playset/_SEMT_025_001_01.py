# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesAccountPositionQueryV01

class SEMT_025_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:semt.025.001.01"
		_docname = "semt.025.001.01"

		__slots__ = ["_SctiesAcctPosQry"]
		@property
		def SctiesAcctPosQry(self):
			return self._SctiesAcctPosQry

		@SctiesAcctPosQry.setter
		def SctiesAcctPosQry(self, value):
			self._SctiesAcctPosQry = value if value is not None else base_types.UninitialisedField(self, 'SctiesAcctPosQry', SecuritiesAccountPositionQueryV01, False)

		@SctiesAcctPosQry.deleter
		def SctiesAcctPosQry(self):
			del self._SctiesAcctPosQry
			self._SctiesAcctPosQry = base_types.UninitialisedField(self, 'SctiesAcctPosQry', SecuritiesAccountPositionQueryV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesAcctPosQry', type=SecuritiesAccountPositionQueryV01, min=1, max=1, mutex_group=None, array=False),
		))