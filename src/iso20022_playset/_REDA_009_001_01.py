# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecurityActivityAdviceV01 import SecurityActivityAdviceV01

class REDA_009_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:reda.009.001.01"
		_docname = "reda.009.001.01"

		__slots__ = ["_SctyActvtyAdvc"]
		@property
		def SctyActvtyAdvc(self):
			return self._SctyActvtyAdvc

		@SctyActvtyAdvc.setter
		def SctyActvtyAdvc(self, value):
			self._SctyActvtyAdvc = value if type(value) != base_types.auto else self.make_default("SctyActvtyAdvc")

		@SctyActvtyAdvc.deleter
		def SctyActvtyAdvc(self):
			del self._SctyActvtyAdvc
			self._SctyActvtyAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctyActvtyAdvc', type=SecurityActivityAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))