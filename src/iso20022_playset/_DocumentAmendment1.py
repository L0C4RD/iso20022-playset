from . import base_types
from ._Number import Number
from ._Max35Text import Max35Text

class DocumentAmendment1(base_types._BaseFieldType):

	__slots__ = ["_CrrctnId", "_OrgnlDocId"]
	@property
	def CrrctnId(self):
		return self._CrrctnId

	@CrrctnId.setter
	def CrrctnId(self, value):
		self._CrrctnId = value if type(value) != base_types.auto else self.make_default("CrrctnId")

	@CrrctnId.deleter
	def CrrctnId(self):
		del self._CrrctnId
		self._CrrctnId = None

	@property
	def OrgnlDocId(self):
		return self._OrgnlDocId

	@OrgnlDocId.setter
	def OrgnlDocId(self, value):
		self._OrgnlDocId = value if type(value) != base_types.auto else self.make_default("OrgnlDocId")

	@OrgnlDocId.deleter
	def OrgnlDocId(self):
		del self._OrgnlDocId
		self._OrgnlDocId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CrrctnId', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlDocId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

