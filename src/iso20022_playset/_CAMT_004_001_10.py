# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ReturnAccountV10

class CAMT_004_001_10():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10"
		_docname = "camt.004.001.10"

		__slots__ = ["_RtrAcct"]
		@property
		def RtrAcct(self):
			return self._RtrAcct

		@RtrAcct.setter
		def RtrAcct(self, value):
			self._RtrAcct = value if value is not None else base_types.UninitialisedField(self, 'RtrAcct', ReturnAccountV10, False)

		@RtrAcct.deleter
		def RtrAcct(self):
			del self._RtrAcct
			self._RtrAcct = base_types.UninitialisedField(self, 'RtrAcct', ReturnAccountV10, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='RtrAcct', type=ReturnAccountV10, min=1, max=1, mutex_group=None, array=False),
		))