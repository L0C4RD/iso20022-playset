# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CreateMemberV01 import CreateMemberV01

class CAMT_104_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.104.001.01"
		_docname = "camt.104.001.01"

		__slots__ = ["_CretMmb"]
		@property
		def CretMmb(self):
			return self._CretMmb

		@CretMmb.setter
		def CretMmb(self, value):
			self._CretMmb = value if type(value) != base_types.auto else self.make_default("CretMmb")

		@CretMmb.deleter
		def CretMmb(self):
			del self._CretMmb
			self._CretMmb = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CretMmb', type=CreateMemberV01, min=1, max=1, mutex_group=None, array=False),
		))