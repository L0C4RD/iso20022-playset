# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ChargeBackInitiationV04 import ChargeBackInitiationV04

class CAIN_027_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:cain.027.001.04"
		_docname = "cain.027.001.04"

		__slots__ = ["_ChrgBckInitn"]
		@property
		def ChrgBckInitn(self):
			return self._ChrgBckInitn

		@ChrgBckInitn.setter
		def ChrgBckInitn(self, value):
			self._ChrgBckInitn = value if type(value) != base_types.auto else self.make_default("ChrgBckInitn")

		@ChrgBckInitn.deleter
		def ChrgBckInitn(self):
			del self._ChrgBckInitn
			self._ChrgBckInitn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ChrgBckInitn', type=ChargeBackInitiationV04, min=1, max=1, mutex_group=None, array=False),
		))