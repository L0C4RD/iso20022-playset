# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max140Text
from . import Max350Text
from . import Max35Text

class ElementIdentification3(base_types._BaseFieldType):

	__slots__ = ["_ElmtNm", "_ElmtPth", "_ElmtVal"]
	@property
	def ElmtNm(self):
		return self._ElmtNm

	@ElmtNm.setter
	def ElmtNm(self, value):
		self._ElmtNm = value if value is not None else base_types.UninitialisedField(self, 'ElmtNm', Max35Text, False)

	@ElmtNm.deleter
	def ElmtNm(self):
		del self._ElmtNm
		self._ElmtNm = base_types.UninitialisedField(self, 'ElmtNm', Max35Text, False)

	@property
	def ElmtPth(self):
		return self._ElmtPth

	@ElmtPth.setter
	def ElmtPth(self, value):
		self._ElmtPth = value if value is not None else base_types.UninitialisedField(self, 'ElmtPth', Max350Text, False)

	@ElmtPth.deleter
	def ElmtPth(self):
		del self._ElmtPth
		self._ElmtPth = base_types.UninitialisedField(self, 'ElmtPth', Max350Text, False)

	@property
	def ElmtVal(self):
		return self._ElmtVal

	@ElmtVal.setter
	def ElmtVal(self, value):
		self._ElmtVal = value if value is not None else base_types.UninitialisedField(self, 'ElmtVal', Max140Text, False)

	@ElmtVal.deleter
	def ElmtVal(self):
		del self._ElmtVal
		self._ElmtVal = base_types.UninitialisedField(self, 'ElmtVal', Max140Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ElmtNm', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ElmtPth', type=Max350Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ElmtVal', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
	))