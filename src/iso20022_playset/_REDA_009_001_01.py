# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecurityActivityAdviceV01

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
			self._SctyActvtyAdvc = value if value is not None else base_types.UninitialisedField(self, 'SctyActvtyAdvc', SecurityActivityAdviceV01, False)

		@SctyActvtyAdvc.deleter
		def SctyActvtyAdvc(self):
			del self._SctyActvtyAdvc
			self._SctyActvtyAdvc = base_types.UninitialisedField(self, 'SctyActvtyAdvc', SecurityActivityAdviceV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctyActvtyAdvc', type=SecurityActivityAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))