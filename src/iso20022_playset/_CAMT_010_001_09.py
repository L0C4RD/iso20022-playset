# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ReturnLimitV09

class CAMT_010_001_09():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.010.001.09"
		_docname = "camt.010.001.09"

		__slots__ = ["_RtrLmt"]
		@property
		def RtrLmt(self):
			return self._RtrLmt

		@RtrLmt.setter
		def RtrLmt(self, value):
			self._RtrLmt = value if value is not None else base_types.UninitialisedField(self, 'RtrLmt', ReturnLimitV09, False)

		@RtrLmt.deleter
		def RtrLmt(self):
			del self._RtrLmt
			self._RtrLmt = base_types.UninitialisedField(self, 'RtrLmt', ReturnLimitV09, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='RtrLmt', type=ReturnLimitV09, min=1, max=1, mutex_group=None, array=False),
		))