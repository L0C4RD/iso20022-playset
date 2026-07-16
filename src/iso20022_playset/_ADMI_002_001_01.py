# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import admi.002.001.01

class ADMI_002_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:admi.002.001.01"
		_docname = "admi.002.001.01"

		__slots__ = ["_admi.002.001.01"]
		@property
		def admi.002.001.01(self):
			return self._admi.002.001.01

		@admi.002.001.01.setter
		def admi.002.001.01(self, value):
			self._admi.002.001.01 = value if value is not None else base_types.UninitialisedField(self, 'admi.002.001.01', admi.002.001.01, False)

		@admi.002.001.01.deleter
		def admi.002.001.01(self):
			del self._admi.002.001.01
			self._admi.002.001.01 = base_types.UninitialisedField(self, 'admi.002.001.01', admi.002.001.01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='admi.002.001.01', type=admi.002.001.01, min=1, max=1, mutex_group=None, array=False),
		))