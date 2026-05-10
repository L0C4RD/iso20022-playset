import base_types
import Max35Text

class ATMCustomerProfile2(base_types._BaseFieldType):

	__slots__ = ["_CstmrId", "_PrflRef"]
	@property
	def CstmrId(self):
		return self._CstmrId

	@CstmrId.setter
	def CstmrId(self, value):
		self._CstmrId = value if type(value) != auto else self.make_default("CstmrId")

	@CstmrId.deleter
	def CstmrId(self):
		del self._CstmrId
		self._CstmrId = None

	@property
	def PrflRef(self):
		return self._PrflRef

	@PrflRef.setter
	def PrflRef(self, value):
		self._PrflRef = value if type(value) != auto else self.make_default("PrflRef")

	@PrflRef.deleter
	def PrflRef(self):
		del self._PrflRef
		self._PrflRef = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CstmrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrflRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

