import base_types
import Max35Text

class GeneralCollateral2(base_types._BaseFieldType):

	__slots__ = ["_ElgblFinInstrmId"]
	@property
	def ElgblFinInstrmId(self):
		return self._ElgblFinInstrmId

	@ElgblFinInstrmId.setter
	def ElgblFinInstrmId(self, value):
		self._ElgblFinInstrmId = value if type(value) != auto else self.make_default("ElgblFinInstrmId")

	@ElgblFinInstrmId.deleter
	def ElgblFinInstrmId(self):
		del self._ElgblFinInstrmId
		self._ElgblFinInstrmId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ElgblFinInstrmId', type=Max35Text, min=1, max=None, mutex_group=None, array=True),
	))

