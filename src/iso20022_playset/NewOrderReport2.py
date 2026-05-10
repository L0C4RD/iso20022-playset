from . import base_types
import Max140Text
import OrderData3

class NewOrderReport2(base_types._BaseFieldType):

	__slots__ = ["_RptId", "_Ordr"]
	@property
	def RptId(self):
		return self._RptId

	@RptId.setter
	def RptId(self, value):
		self._RptId = value if type(value) != auto else self.make_default("RptId")

	@RptId.deleter
	def RptId(self):
		del self._RptId
		self._RptId = None

	@property
	def Ordr(self):
		return self._Ordr

	@Ordr.setter
	def Ordr(self, value):
		self._Ordr = value if type(value) != auto else self.make_default("Ordr")

	@Ordr.deleter
	def Ordr(self):
		del self._Ordr
		self._Ordr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RptId', type=Max140Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ordr', type=OrderData3, min=1, max=None, mutex_group=None, array=True),
	))

