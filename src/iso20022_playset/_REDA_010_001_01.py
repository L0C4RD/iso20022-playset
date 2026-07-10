# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecurityQueryV01 import SecurityQueryV01

class REDA_010_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:reda.010.001.01"
		_docname = "reda.010.001.01"

		__slots__ = ["_SctyQry"]
		@property
		def SctyQry(self):
			return self._SctyQry

		@SctyQry.setter
		def SctyQry(self, value):
			self._SctyQry = value if type(value) != base_types.auto else self.make_default("SctyQry")

		@SctyQry.deleter
		def SctyQry(self):
			del self._SctyQry
			self._SctyQry = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctyQry', type=SecurityQueryV01, min=1, max=1, mutex_group=None, array=False),
		))