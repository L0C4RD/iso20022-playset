import base_types
import Party53Choice
import DebtorActivation5

class OriginalActivation3Choice(base_types._BaseFieldType):

	__slots__ = ["_OrgnlDbtrId", "_OrgnlActvtnData"]
	@property
	def OrgnlDbtrId(self):
		return self._OrgnlDbtrId

	@OrgnlDbtrId.setter
	def OrgnlDbtrId(self, value):
		self._OrgnlDbtrId = value if type(value) != auto else self.make_default("OrgnlDbtrId")

	@OrgnlDbtrId.deleter
	def OrgnlDbtrId(self):
		del self._OrgnlDbtrId
		self._OrgnlDbtrId = None

	@property
	def OrgnlActvtnData(self):
		return self._OrgnlActvtnData

	@OrgnlActvtnData.setter
	def OrgnlActvtnData(self, value):
		self._OrgnlActvtnData = value if type(value) != auto else self.make_default("OrgnlActvtnData")

	@OrgnlActvtnData.deleter
	def OrgnlActvtnData(self):
		del self._OrgnlActvtnData
		self._OrgnlActvtnData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgnlDbtrId', type=Party53Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='OrgnlActvtnData', type=DebtorActivation5, min=0, max=1, mutex_group=1, array=False),
	))

