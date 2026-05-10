from . import base_types
from ._DocumentIdentification7 import DocumentIdentification7
from ._Max70Text import Max70Text

class LineItemAndPOIdentification1(base_types._BaseFieldType):

	__slots__ = ["_PurchsOrdrRef", "_LineItmId"]
	@property
	def PurchsOrdrRef(self):
		return self._PurchsOrdrRef

	@PurchsOrdrRef.setter
	def PurchsOrdrRef(self, value):
		self._PurchsOrdrRef = value if type(value) != base_types.auto else self.make_default("PurchsOrdrRef")

	@PurchsOrdrRef.deleter
	def PurchsOrdrRef(self):
		del self._PurchsOrdrRef
		self._PurchsOrdrRef = None

	@property
	def LineItmId(self):
		return self._LineItmId

	@LineItmId.setter
	def LineItmId(self, value):
		self._LineItmId = value if type(value) != base_types.auto else self.make_default("LineItmId")

	@LineItmId.deleter
	def LineItmId(self):
		del self._LineItmId
		self._LineItmId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PurchsOrdrRef', type=DocumentIdentification7, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LineItmId', type=Max70Text, min=1, max=None, mutex_group=None, array=True),
	))

