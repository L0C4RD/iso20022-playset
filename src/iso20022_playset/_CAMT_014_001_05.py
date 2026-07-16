# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ReturnMemberV05

class CAMT_014_001_05():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.014.001.05"
		_docname = "camt.014.001.05"

		__slots__ = ["_RtrMmb"]
		@property
		def RtrMmb(self):
			return self._RtrMmb

		@RtrMmb.setter
		def RtrMmb(self, value):
			self._RtrMmb = value if value is not None else base_types.UninitialisedField(self, 'RtrMmb', ReturnMemberV05, False)

		@RtrMmb.deleter
		def RtrMmb(self):
			del self._RtrMmb
			self._RtrMmb = base_types.UninitialisedField(self, 'RtrMmb', ReturnMemberV05, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='RtrMmb', type=ReturnMemberV05, min=1, max=1, mutex_group=None, array=False),
		))