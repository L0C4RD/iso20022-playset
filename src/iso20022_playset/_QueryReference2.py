# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text

class QueryReference2(base_types._BaseFieldType):

	__slots__ = ["_QryNm", "_QryRef"]
	@property
	def QryNm(self):
		return self._QryNm

	@QryNm.setter
	def QryNm(self, value):
		self._QryNm = value if value is not None else base_types.UninitialisedField(self, 'QryNm', Max35Text, False)

	@QryNm.deleter
	def QryNm(self):
		del self._QryNm
		self._QryNm = base_types.UninitialisedField(self, 'QryNm', Max35Text, False)

	@property
	def QryRef(self):
		return self._QryRef

	@QryRef.setter
	def QryRef(self, value):
		self._QryRef = value if value is not None else base_types.UninitialisedField(self, 'QryRef', Max35Text, False)

	@QryRef.deleter
	def QryRef(self):
		del self._QryRef
		self._QryRef = base_types.UninitialisedField(self, 'QryRef', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='QryNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryRef', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))