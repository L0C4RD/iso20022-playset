from . import base_types
from ._Max35Text import Max35Text

class QueryReference2(base_types._BaseFieldType):

	__slots__ = ["_QryNm", "_QryRef"]
	@property
	def QryNm(self):
		return self._QryNm

	@QryNm.setter
	def QryNm(self, value):
		self._QryNm = value if type(value) != base_types.auto else self.make_default("QryNm")

	@QryNm.deleter
	def QryNm(self):
		del self._QryNm
		self._QryNm = None

	@property
	def QryRef(self):
		return self._QryRef

	@QryRef.setter
	def QryRef(self, value):
		self._QryRef = value if type(value) != base_types.auto else self.make_default("QryRef")

	@QryRef.deleter
	def QryRef(self):
		del self._QryRef
		self._QryRef = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='QryNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryRef', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

