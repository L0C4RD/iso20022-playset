# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DocumentIdentification7
from . import Max70Text

class LineItemAndPOIdentification1(base_types._BaseFieldType):

	__slots__ = ["_LineItmId", "_PurchsOrdrRef"]
	@property
	def LineItmId(self):
		return self._LineItmId

	@LineItmId.setter
	def LineItmId(self, value):
		self._LineItmId = value if value is not None else base_types.UninitialisedField(self, 'LineItmId', Max70Text, True)

	@LineItmId.deleter
	def LineItmId(self):
		del self._LineItmId
		self._LineItmId = base_types.UninitialisedField(self, 'LineItmId', Max70Text, True)

	@property
	def PurchsOrdrRef(self):
		return self._PurchsOrdrRef

	@PurchsOrdrRef.setter
	def PurchsOrdrRef(self, value):
		self._PurchsOrdrRef = value if value is not None else base_types.UninitialisedField(self, 'PurchsOrdrRef', DocumentIdentification7, False)

	@PurchsOrdrRef.deleter
	def PurchsOrdrRef(self):
		del self._PurchsOrdrRef
		self._PurchsOrdrRef = base_types.UninitialisedField(self, 'PurchsOrdrRef', DocumentIdentification7, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='LineItmId', type=Max70Text, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PurchsOrdrRef', type=DocumentIdentification7, min=1, max=1, mutex_group=None, array=False),
	))